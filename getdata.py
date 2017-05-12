def get_historical(symbol, fromdate, todate):
    '''
    Get the historical trading data of stock given a date range
    :param symbol: Symbol of a trading stock
    :param fromdate:string start date of the data in the format of 'yyyy-mm-dd'
    :param todate:string end date of the data in the format of 'yyyy-mm-dd' 
    :return: A pandas dataframe
    '''
    import pandas as pd
    import json
    import yahoo_finance as yf
    yahoo_data = yf.Share(symbol)
    historical_data = yahoo_data.get_historical(fromdate, todate)
    return pd.read_json(json.dumps(historical_data), orient='records').iloc[::-1]