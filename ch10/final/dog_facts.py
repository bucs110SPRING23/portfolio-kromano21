import requests

class DogFacts:
    def __init__(self):
        self.api_url = "http://dog-api.kinduff.com/api/facts"
    
    def __str__(self):
        '''
        This method provides a readable string representation of the instance
        args: None
        return: str
        '''
        return "DogFacts"
    
    def get(self):
        '''
        This method pulls a dog fact from a dog fact API and returns it in a string.
        args: None
        return: str
        '''
        retrieval = requests.get(self.api_url)
        response = retrieval.json() 
        return str(response)
