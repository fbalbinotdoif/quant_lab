import requests
import yfinance as yf

VALID_PERIODS = { "1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"}

def history_price (name, period):

    if period not in VALID_PERIODS:
        print("Error: Period Not Valid")
        return None

    try:
        ticker = yf.Ticker(name)
        df = ticker.history(period=period, auto_adjust=False)

    except requests.exceptions.ConnectionError:
        print("Error Connection")
        return None
    except requests.exceptions.Timeout:
        print("Time Out Error")
        return None
    except Exception:
        print("Error")
        return None
    
    if df.empty:
        print("Error: No Data Returned")
        return None

    return df


