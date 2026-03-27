def transform_data (df, ticker):

    df = df.drop(columns=['Dividends','Stock Splits'])

    df['ticker'] = ticker

    df.index = df.index.tz_convert(None).normalize()

    df = df.reset_index()

    df = df.rename(columns={'Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adj_close','Volume':'volume','Date':'date'})

    return df


if __name__ == "__main__":
    from api_client import history_price
    data = history_price('ASML','1y')
    df = transform_data(data,ticker='ASML')
    print(transform_data(data,ticker='ASML'))