import key
from binance.client import Client

class BinanceAPI:
    
    def __init__(self, test_flag):
        print('-----init-----')

        if test_flag == 'test':
            api_key = key.api_key_test
            api_secret = key.api_key_test
        elif test_flag == 'real':
            api_key = key.api_key_real
            api_secret = key.api_key_real
        else:
            raise Exception('check test flag', test_flag)

        self.client = Client(api_key, api_secret)

        ## Set test URL
        if test_flag == 'test':
            self.client.API_URL = 'https://testnet.binance.vision/api'
            print('-----running in test mode-----')
    
    def get_ticker(self , pair):
        try:
            value = self.client.get_ticker(symbol=pair)
            return value
        except Exception as e:
            print('Exception Message : {}'.format(e))
            return
        
    def get_asset(self, symbol):
        try:
            value = self.client.get_asset_balance(asset=symbol)
            return value
        except Exception as e:
            print('Exception Message : {}'.format(e))
            return

def main():
    ## set 'test' or 'real'
    binance_set = BinanceAPI('test')

    ticker = binance_set.get_ticker('BTCUSDT')

    for ticker_key, ticker_value in ticker.items():
        print(ticker_key, ':', ticker_value)

if __name__ == '__main__':
    main()