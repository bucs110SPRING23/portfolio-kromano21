import requests

class ValorantAPI:
    def __init__(self):
        self.url = "https://valorant-api.com/v1"
    
    def get_agents(self):
        recieved = requests.get(f'{self.url}/agents?isPlayableCharacter=true')
        response = recieved.json()
        print(response)

test = ValorantAPI()
test.get_agents()



    