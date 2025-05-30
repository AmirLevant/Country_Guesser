import random

def random_country_selection():
    random_country_id = random.randint(0,200)
    

 
# the text that reveals the attributes and dictates the responses of the game
def ingame_text(): 
    print("A random country has been selected! \n")

def beginning_text():
    print("Welcome to the country guesser game!")


    print("A country has the following attributes: ")
    print(" - Continent")
    print(" - Capital City")
    print(" - Flag Colors")
    print(" - First Letter")
    print(" - Language")
    print(" - Population Size")

    

    print("\n you will be given two attributes to start and begin a round")
    print("a round consists of 3 attempts, after 3 wrong attempts, an additional attribute will be revealed \n ")
    print("Are you ready to begin? Y/N")
    




def main():
    beginning_text()




main()