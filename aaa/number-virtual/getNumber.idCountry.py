import requests,sys
try:
	id = sys.argv[1]
	APIKEY = sys.argv[2]
except Exception:
	print(f"Ejecuta: {sys.argv[0]} <id> <API-KEY>")
	exit()

url = "https://virtual-number.p.rapidapi.com/api/v1/e-sim/country-numbers"

querystring = {"countryId":id} # Id a cambiar

headers = {
	"X-RapidAPI-Key": str(APIKEY),
	"X-RapidAPI-Host": "virtual-number.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)