# I need to add the first letter of the country to the JSON lists
import json
import psycopg2
from psycopg2.extras import execute_values
import base64


 # adding the first letter of each country to the list being formed from the JSON
def beginning():
    inputJSON = open('api_countries_trimmed.json', "r", encoding="utf-8")
    inputData = json.load(inputJSON)

    for i in range(len(inputData)):
        first_letter = inputData[i]["country_name"][0]
        inputData[i].update({'country_first_letter': first_letter}) 

    insertiontodatabase(inputData) # calling the insertion

# inserting to the database
def insertiontodatabase(countries_list): 
    
    conn = psycopg2.connect(
        database="COUNTRY_GUESSER",
        user="postgres",
        password="amir",
        host="127.0.0.1",
        port=5432,
    )
    cursor = conn.cursor()

    columns = countries_list[0].keys()
    query = "INSERT INTO countries ({}) VALUES %s".format(','.join(columns))
    values = [[value for value in country.values()] for country in countries_list]
    print(values)
    execute_values(cursor,query,values)
    conn.commit()



def main():
    beginning()


main()