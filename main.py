import requests, json

location = input("Enter the country name: ")

complete_api_link = "https://disease.sh/v3/covid-19/countries/"+location
api_link = requests.get(complete_api_link)
api_data = api_link.json()

cases = ((api_data['cases']))
recovered = api_data['recovered']
deaths = api_data['deaths']
country = api_data['country']

print("---------------------------------------------------------------")
print("Covid Stats for - {}".format(country.upper()))
print("---------------------------------------------------------------")

resCases = print("Cases     :", cases)
resRecovered = print("Recovered :", recovered)
resDeaths = print("Deaths    :", deaths)
