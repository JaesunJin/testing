import key
from binance.client import Client

class get_client :

    def get_client(self, mode):
        print('----- GET CLIENT -----')

        if mode == 'real' :
            api_key = key.api_key_real
            api_secret = key.api_secret_real
        elif mode == 'test' :
            api_key = key.api_key_test
            api_secret = key.api_secret_test
        else :
            raise Exception('CHECK MODE : ', mode)

        self.client = Client(api_key, api_secret)

        ## Set test URL
        if mode == 'test' :
            self.client.API_URL = 'https://testnet.binance.vision/api'
            print('----- RUNNING IN TEST MODE -----')
        
        return self.client