# I need to add the first letter of the country to the JSON lists
import json

# with open("api_countries_trimmed.json","r", encoding = "utf-8") as f:
#     for line in f:
#         json_data = json.loads(line)

inputJSON = open('api_countries_trimmed.json')
inputData = json.load(inputJSON)

for i in range(len(inputData)):
    first_letter = inputData[i]["name"][0]
    inputData[i].update({'country_first_letter': first_letter})
    print(inputData[0])
    break