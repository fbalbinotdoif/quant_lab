from cli.cli import get_window
from database.querys import q_returns


def rolling_mean(df, window):
    adj_close = df['adj_close']
    mean_rolling = adj_close.rolling(window).mean()
    return mean_rolling

def rolling_std(df, window):
    adj_close = df['adj_close']
    std_rolling = adj_close.rolling(window).std()
    return std_rolling

def rolling_min(df, window):
    adj_close = df['adj_close']
    min_rolling = adj_close.rolling(window).min()
    return min_rolling

def rolling_max(df, window):
    adj_close = df['adj_close']
    max_rolling = adj_close.rolling(window).max()
    return max_rolling

if __name__ == "__main__":

    ticker, period, window = get_window()
    df = q_returns(ticker,period) 

    print('ROLLING MEAN:')
    mean_rolling = rolling_mean(df, window)
    print(mean_rolling)
    print()
    print('ROLLING STD:')
    std_rolling = rolling_std(df, window)
    print(std_rolling)
    print()
    print('ROLLING MIN:')
    min_rolling = rolling_min(df, window)
    print(min_rolling)
    print()
    print('ROLLING MAX:')
    max_rolling = rolling_max(df, window)
    print(max_rolling)