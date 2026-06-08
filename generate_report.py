import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

historical_df = pd.read_csv('data/historical_data.csv')
fear_greed_df = pd.read_csv('data/fear_greed_index.csv')

historical_df['Timestamp IST'] = pd.to_datetime(historical_df['Timestamp IST'], errors='coerce')
fear_greed_df['timestamp'] = pd.to_datetime(fear_greed_df['timestamp'], errors='coerce')
historical_df['trade_date'] = historical_df['Timestamp IST'].dt.normalize()
fear_greed_df['trade_date'] = fear_greed_df['timestamp'].dt.normalize()

merged = pd.merge(
    historical_df,
    fear_greed_df[['trade_date', 'value', 'classification']],
    on='trade_date',
    how='left'
)
merged['Win'] = merged['Closed PnL'] > 0

sentiment_summary = (
    merged.groupby('classification', dropna=False)
    .agg(avg_pnl=('Closed PnL', 'mean'), total_pnl=('Closed PnL', 'sum'), win_rate=('Win', 'mean'), trade_count=('Trade ID', 'count'))
    .sort_values('total_pnl', ascending=False)
)

coin_summary = (
    merged.groupby('Coin')
    .agg(total_pnl=('Closed PnL', 'sum'), avg_pnl=('Closed PnL', 'mean'))
    .sort_values('total_pnl', ascending=False)
)

trader_summary = (
    merged.groupby('Account')
    .agg(total_pnl=('Closed PnL', 'sum'), trade_count=('Trade ID', 'count'))
    .sort_values('total_pnl', ascending=False)
)

fig = plt.figure(figsize=(8.27, 11.69))
fig.suptitle('Bitcoin Market Sentiment vs Hyperliquid Trader Performance Analysis', fontsize=16, fontweight='bold', y=0.98)

ax1 = fig.add_axes([0.08, 0.78, 0.84, 0.16])
ax1.axis('off')
ax1.text(0.0, 1.0, 'Executive Summary', fontsize=13, fontweight='bold', va='top')
ax1.text(0.0, 0.72, 'This report analyzes the relationship between market sentiment and trader performance using the Hyperliquid trade dataset and Fear & Greed Index labels.', fontsize=10, va='top')
ax1.text(0.0, 0.46, f'Total trades: {len(merged)} | Total PnL: {merged["Closed PnL"].sum():.2f} | Average PnL: {merged["Closed PnL"].mean():.2f}', fontsize=10, va='top')
ax1.text(0.0, 0.20, 'Top sentiment by total PnL: ' + str(sentiment_summary.index[0]) + ' with ' + f"{sentiment_summary.iloc[0]['total_pnl']:.2f}", fontsize=10, va='top')

ax2 = fig.add_axes([0.08, 0.60, 0.84, 0.16])
ax2.bar(sentiment_summary.index.astype(str), sentiment_summary['avg_pnl'], color='tab:blue')
ax2.set_title('Average PnL by Sentiment')
ax2.set_ylabel('Average PnL')
ax2.tick_params(axis='x', rotation=30)

ax3 = fig.add_axes([0.08, 0.42, 0.84, 0.16])
ax3.bar(sentiment_summary.index.astype(str), sentiment_summary['win_rate'], color='tab:green')
ax3.set_title('Win Rate by Sentiment')
ax3.set_ylabel('Win Rate')
ax3.tick_params(axis='x', rotation=30)

ax4 = fig.add_axes([0.08, 0.24, 0.84, 0.16])
ax4.bar(coin_summary.index.astype(str), coin_summary['total_pnl'], color='tab:orange')
ax4.set_title('Top Coins by Total PnL')
ax4.set_ylabel('Total PnL')
ax4.tick_params(axis='x', rotation=30)

ax5 = fig.add_axes([0.08, 0.06, 0.84, 0.16])
ax5.bar(trader_summary.index.astype(str), trader_summary['total_pnl'], color='tab:red')
ax5.set_title('Top Traders by Total PnL')
ax5.set_ylabel('Total PnL')
ax5.tick_params(axis='x', rotation=30)

fig.savefig('report.pdf', bbox_inches='tight')
print('saved report.pdf with analysis summary and charts')
