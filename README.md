# Bitcoin Market Sentiment vs Hyperliquid Trader Performance Analysis

## Project Overview
This project analyzes the relationship between Bitcoin market sentiment (Fear & Greed Index) and Hyperliquid trader performance using historical trade data and sentiment scores.

## Objective
- Understand how sentiment affects trader profitability.
- Compare PnL, win rate, position size, and fees across sentiment classes.
- Prepare a professional notebook and report for assignment submission.

## Dataset Description
- `data/historical_data.csv`: Hyperliquid trade records including account, coin, execution price, size, side, timestamps, PnL, fee, and trade id.
- `data/fear_greed_index.csv`: Fear & Greed Index daily sentiment values with `value`, `classification`, and date.

## Methodology
1. Load datasets with pandas.
2. Clean timestamps and create merge keys.
3. Merge sentiment labels onto trade records.
4. Compute performance metrics by sentiment.
5. Visualize patterns with matplotlib and seaborn.

## Results
The notebook provides the baseline workflow for sentiment-based analysis, including win-rate, PnL, position size, and fee analysis.

## Visualizations
- Sentiment vs average PnL
- Sentiment vs win rate
- Sentiment vs position size
- Sentiment vs fees
- Buy vs sell performance
- Top coins and traders

## Technologies Used
- Python
- pandas
- numpy
- matplotlib
- seaborn
- Jupyter Notebook

## Installation
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

## Repository Structure
```text
bitcoin-sentiment-analysis/
├── data/
│   ├── historical_data.csv
│   └── fear_greed_index.csv
├── notebook.ipynb
├── report.pdf
├── requirements.txt
├── README.md
└── .gitignore
```
