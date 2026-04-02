from database.querys import q_returns
from cli.cli import get_ticker_period
from feature_engineering.volatility import historic_simple_volatility
from feature_engineering.returns import log_return_digit
from feature_engineering.returns import log_return

def sharpe_ratio(df, rf=0.05):
    return_log = log_return(df)
    rf_period = (1 + rf)**(len(df)/252)-1

    rp = log_return_digit(df)
    sigma =  historic_simple_volatility(return_log)

    sharpe = (rp - rf_period) / sigma
    return sharpe

def sortino_ratio(df, rf=0.05):
    return_log = log_return(df)
    negative_return_log = return_log[return_log < 0]
    rf_period = (1 + rf)**(len(df)/252)-1

    rp = log_return_digit(df)
    sigma =  historic_simple_volatility(negative_return_log)

    sortino = (rp - rf_period) / sigma
    return sortino

if __name__ == "__main__":
    ticker, period = get_ticker_period()
    read = q_returns(ticker,period)

    print('SHARPE RATIO:')
    sharpe = sharpe_ratio(read)
    print(sharpe)
    print()
    print('SORTINO RATIO:')
    sortino = sortino_ratio(read)
    print(sortino)
