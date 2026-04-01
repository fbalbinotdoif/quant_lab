from cli.cli import get_window
from database.querys import q_returns
from feature_engineering.returns import log_return
from feature_engineering.rolling import rolling_mean, rolling_std

def z_score_historic(df):
    returns = log_return(df)
    mean = returns.mean()
    std = returns.std()
    z_score = (returns - mean) / std

    return z_score

def z_score_mobile(df, window):
    returns = log_return(df)
    mean = rolling_mean(returns, window)
    std = rolling_std(returns, window)
    z_score = (returns - mean) / std

    return z_score

if __name__ == "__main__":

    ticker, period, window = get_window()
    df = q_returns(ticker,period)

    print("Z-SCORE HISTORIC:")
    z_score_h = z_score_historic(df)
    print(z_score_h)
    print()
    print("Z-SCORE MOBILE:")
    z_score_m = z_score_mobile(df, window)
    print(z_score_m)
