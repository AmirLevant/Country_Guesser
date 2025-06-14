import json
import psycopg2

# i only need common name, capital, region, flag, population
def postgresstuff():
    def get_connection():
        try:
            return psycopg2.connect(
                database="COUNTRY_GUESSER",
                user="postgres",
                password="amir",
                host="127.0.0.1",
                port=5432,
            )
        except:
            return False
    conn = get_connection()
    if conn:
        print("Connection to the PostgreSQL established successfully.")
    else:
        print("Connection to the PostgreSQL encountered and error.")

    cursor = conn.cursor()


with open("api_countries_untrimmed.txt", "r", encoding="utf-8") as f:
   for line in f:
        json_data = json.loads(line) # we load the data to json_data
        parsed_countries = []
        for i in range(len(json_data)):
            parsed_countries.append(json_data[i])
            temp = parsed_countries[i]['name']['common']
            parsed_countries[i]['name'] = temp

            capital_unsanitized = ""
            capital_unsanitized = str(parsed_countries[i]['capital'])
            capital_sanitized = capital_unsanitized.strip("[]'")
            parsed_countries[i]['capital'] = capital_sanitized
    
        print(parsed_countries[0])
            




