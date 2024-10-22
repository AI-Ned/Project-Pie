import requests
import time

# used the following list to reduce my API calls  https://www.jojhelfer.com/lettercombos
class DictApi:
   

    api_base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def wordtest(word):
        #check to ensure a value has been provided
        if len(word) <= 0:
            print("Error no word provided")
            
       
        api_url = DictApi.api_base_url + word

        response = requests.get(api_url)
        
        #check the status codes for a response
        if response.status_code == 429:
            time.sleep(10.5)
        
        if response.status_code == 200:
            print(response.json()[0]['word'])
            
            return True
        elif response.status_code == 404:
            return False
       
        else:
            print("Something went wrong "+str(response.status_code))
            print(response.headers)