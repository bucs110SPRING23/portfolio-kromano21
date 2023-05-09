import requests

class MonterHunterAPI:
    def __init__(self):
        self.api_url = "https://mhw-db.com/monsters/"
        self.monster = str(input("What Monster do you want to Learn the Weaknesses of? (Make sure to Include Proper Capitalization and Punctuation!)\n"))
    
    def __str__(self):
        '''
        This method provides a readable string representation of the instance
        args: None
        return: str
        '''
        return "MonsterHunterAPI"
       
    def get(self):
        '''
        This method matches the user's requested monster to the name of the monster from the Monster Hunter World API and returns its respective weaknesses.
        args: None
        return: str
        '''
        for i in range(1, 46):
            retrieval = requests.get(self.api_url + str(i))
            response = retrieval.json()
            name = response["name"]
            if name == self.monster:
                weaknesses = response["weaknesses"]
                break
        
        result = "\nHere are the Monster's Weaknesses: " + str(weaknesses)
        return result 



