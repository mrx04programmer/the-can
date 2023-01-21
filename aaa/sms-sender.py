import requests,sys
try:
	number = sys.argv[1]
	APIKEY = sys.argv[2]
except Exception:
	print(f"Ejecuta {sys.argv} <number> <API-KEY>")
	exit()

url = "https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp"

querystring = {"number":f"{number}","country":"CO"}

headers = {
	"X-RapidAPI-Key": str(APIKEY),
	"X-RapidAPI-Host": "phonenumbervalidatefree.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)