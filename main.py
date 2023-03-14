import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

text = input('Type text')
reqwest = text.replace(' ', '%20').replace('?', '%3F')

payload = "q=English%20is%20hard%2C%20but%20detectably%20so"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "7b71078c26mshb289dd9d0777c30p1861ddjsn110e7b907b12",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
