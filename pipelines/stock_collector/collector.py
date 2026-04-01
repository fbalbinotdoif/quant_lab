from api_client import history_price
from transform import transform_data
from db_writer import writer
from cli import get_ticker_period

def collect (ticker, period):
    print(f'Collecting {ticker} fro {period}')
    data = history_price(ticker, period)
    df = transform_data(data, ticker)
    writer(df)


if __name__ == '__main__':
    ticker, period = get_ticker_period()
    collect(ticker, period)