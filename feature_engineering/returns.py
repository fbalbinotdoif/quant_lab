import numpy as np
from database.querys import q_returns
from cli.cli import get_ticker_period


def log_return(df):
    return_log = np.log(df['adj_close']/df['adj_close'].shift(1))
    return return_log

def log_return_digit(df):
    return_log = np.log(df['adj_close']/df['adj_close'].shift(1))
    return return_log.sum()

def simple_return(df):
    return_log = np.log(df['adj_close']/df['adj_close'].shift(1))
    return_simple = np.exp(return_log.sum()) - 1
    return return_simple

def aritmetic_return(df):
   adj_close_column = df['adj_close']
   return_aritmetic = adj_close_column.pct_change()
   return return_aritmetic

def aritmetic_return_digit(df):
    adj_close_column = df['adj_close']
    return_aritmetic = adj_close_column.pct_change()
    return return_aritmetic.add(1).prod() - 1


if __name__ == "__main__":

    ticker, period = get_ticker_period()
    read = q_returns(ticker,period)
    
    print('LOG RETURN:')
    print(log_return(read))
    print()
    print('LOG RETURN DIGIT:')
    print(log_return_digit(read))
    print()
    print('SIMPLE RETURN:')
    print(simple_return(read))
    print()
    print('ARITMETIC RETURN')
    print(aritmetic_return(read))
    print()
    print("ARITMETIC RETURN DIGIT")
    print(aritmetic_return_digit(read))

