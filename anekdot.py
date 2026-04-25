import requests
from bs4 import BeautifulSoup

def get_anekdot():
	url = "https://www.anekdot.ru/random/anekdot/"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	jokes = soup.find_all("div", class_="text")
	for joke in jokes[:1]:
		return joke.text.strip()
if __name__=="__main__":
	joke = get_anekdot()