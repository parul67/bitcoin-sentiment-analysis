import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8.27, 11.69))
ax.text(0.05, 0.95, 'Bitcoin Market Sentiment vs Hyperliquid Trader Performance Analysis', ha='left', va='top', fontsize=16, weight='bold')
ax.text(0.05, 0.88, 'Project report placeholder generated for assignment submission.', ha='left', va='top', fontsize=11)
ax.text(0.05, 0.80, 'Contents:\n- Data loading and cleaning\n- Sentiment-based metrics\n- Visualizations and insights', ha='left', va='top', fontsize=11)
ax.axis('off')
fig.savefig('report.pdf', bbox_inches='tight')
print('saved report.pdf')
