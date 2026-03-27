from api_client import history_price
from transform import transform_data
from db_writer import writer
import argparse

parser = argparse.ArgumentParser(description='Stock Data Pipeline: API data collection, data transformation, and writing to table')
parser.add_argument('ticker')
parser.add_argument('period')
args = parser.parse_args()

def collect (ticker, period):
    print(f'Collecting {ticker} fro {period}')
    data = history_price(ticker, period)
    df = transform_data(data, ticker)
    writer(df)


if __name__ == '__main__':
    collect(args.ticker, args.period)