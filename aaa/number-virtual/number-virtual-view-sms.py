import requests, sys
try:
	countryId = sys.argv[1]
	number = sys.argv[2]
	APIKEY = sys.argv[3]
except Exception:
	print(f"Ejecuta {sys.argv[0]} <countryId> <number> <API-KEY>")
	exit()

url = "https://virtual-number.p.rapidapi.com/api/v1/e-sim/view-messages"

querystring = {
	"countryId":countryId,
	"number": str(number)
}

headers = {
	"X-RapidAPI-Key": str(APIKEY),
	"X-RapidAPI-Host": "virtual-number.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)