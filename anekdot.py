import requests
from bs4 import BeautifulSoup

def get_anekdot():
	url = "https://www.anekdot.ru/random/anekdot/"
	headers = {
    "User-Agent": "Mozilla/5.0"
}
	response = requests.get(url,headers = headers)
	soup = BeautifulSoup(response.text, "html.parser")
	jokes = soup.find_all("div", class_="text")
	for joke in jokes[:1]:
		return joke.text.strip()
	if response.status.code != 200:
		joke = "что-то пошло не так"
		return joke
if __name__=="__main__":
	joke = get_anekdot()