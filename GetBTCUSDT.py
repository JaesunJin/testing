import key
from binance.client import Client

class BinanceAPI:
    
    def __init__(self):
        print('-----init-----')
        api_key = key.api_key
        api_secret = key.api_secret

        self.client = Client(api_key, api_secret)
        ## Set test URL
        self.client.API_URL = 'https://testnet.binance.vision/api'

        # print(self.client.get_account())
        # get balance for a specific asset only (BTC)
        print('BTCASSET : ', self.client.get_asset_balance(asset='BTC'))
        # get balances for futures account
        # print('Futures Balance : ', self.client.futures_account_balance())

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
    binance_set = BinanceAPI()
    
    ticker = binance_set.get_ticker('BTCUSDT')
    
    for ticker_key, ticker_value in ticker.items():
        print(ticker_key, ':', ticker_value)

    ## asset_dict = prv_set.get_asset('BTC')
    ## print(asset_dict['free'])

if __name__ == '__main__':
    main()