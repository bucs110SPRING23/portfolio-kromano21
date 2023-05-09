from monster_hunter_api import MonterHunterAPI
from dog_facts import DogFacts

def main():
    weakness_finder = MonterHunterAPI()
    monster_weaknesses = weakness_finder.get()
    print(monster_weaknesses)
    fact_finder = DogFacts()
    dog_fact = fact_finder.get()
    cool_monsters = ["Jagras", "Anjanath", "Kirin", "Pukei-Pukei", "Diablos"]
    match_found = False
    for i in cool_monsters:
        if i == weakness_finder.monster:
            print("\nThat's a Cool Monster! Here's a Fact about Dogs: " + dog_fact)
            match_found = True
            break
    
    if match_found == False:
        print("\nThat's not a Cool Monster! No Dog Fact for you Loser!")
    

main()
    
        
