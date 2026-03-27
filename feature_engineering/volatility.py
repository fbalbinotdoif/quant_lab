import numpy as np

from cli.cli import get_window
from database.querys import q_returns
from feature_engineering.returns import log_return


def historic_simple_volatility (return_log):
    hs_volatility = return_log.std()
    return hs_volatility

def anualized_volatility(hs_volatility):
    volatility_anual = hs_volatility * np.sqrt(252)
    return volatility_anual

def rolling_volatility(return_log, window):
    volatility_rolling = return_log.rolling(window).std()
    return volatility_rolling

def ewma_volatility(return_log, lam=0.94):
    volatility_ewma = return_log.ewm(span=2/(1-lam)-1).std()
    return volatility_ewma

if __name__ == "__main__":

    ticker, period, window = get_window()
    read = q_returns(ticker,period)

    return_log = log_return(read)
    hs_volatility = historic_simple_volatility(return_log)
    print('HISTORIC SIMPLE VOLATILITY:')
    print(hs_volatility)
    print()
    volatility_anual = anualized_volatility(hs_volatility)
    print('ANUZALIZED VOLATILITY:')
    print(volatility_anual)
    print()
    volatility_rolling = rolling_volatility(return_log, window)
    print('ROLLING VOLATILITY:')
    print(volatility_rolling)
    print()
    volatility_ewma = ewma_volatility(return_log, lam=0.94)
    print('EWMA VOLATILITY:')
    print(volatility_ewma)
    