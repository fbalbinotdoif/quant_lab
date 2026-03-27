from database.db_connection import connection_database

def writer (df):
    connection = connection_database()
    cursor =connection.cursor()

    for index, row in df.iterrows():
        cursor.execute("""
        INSERT INTO stock_prices (ticker, date, open, high, low, close, adj_close, volume)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT DO NOTHING
        """, (row['ticker'], row['date'], row['open'], row['high'], row['low'], row['close'], row['adj_close'], row['volume']))

    connection.commit()     #transaction
    cursor.close()


if __name__ == '__main__':
    from api_client import history_price
    from transform import transform_data
    data = history_price('META','1y')
    df = transform_data(data,ticker='META')
    print(df)
    writer(df)