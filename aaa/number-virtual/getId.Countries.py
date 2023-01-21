import requests, sys
try:
	APIKEY = sys.argv[1]
except Exception:
	print(f"Ejecuta {sys.argv} <API-KEY>")
	exit()

url = "https://virtual-number.p.rapidapi.com/api/v1/e-sim/all-countries"

headers = {
	"X-RapidAPI-Key": str(APIKEY),
	"X-RapidAPI-Host": "virtual-number.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)