import argparse

def get_ticker_period():
    parser = argparse.ArgumentParser(description='Stock Data Pipeline: API data collection, data transformation, and writing to table')
    parser.add_argument('ticker')
    parser.add_argument('period')
    args = parser.parse_args()

    ticker = args.ticker
    period = args.period

    return ticker, period

def get_window():
    parser = argparse.ArgumentParser(description='Feature Engineering: calculate rolling volatility')
    parser.add_argument('ticker')
    parser.add_argument('period')
    parser.add_argument('window', type=int)
    args = parser.parse_args()

    ticker = args.ticker
    period = args.period
    window = args.window

    return ticker, period, window