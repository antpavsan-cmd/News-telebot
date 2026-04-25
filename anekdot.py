import requests
from bs4 import BeautifulSoup

def get_anekdot():
	url = "https://www.anekdot.ru/random/anekdot/"
	headers = {
    "User-Agent": "Mozilla/5.0"
}
	try:
		response = requests.get(url,headers = headers)
		if response.status_code != 200:
			return "беда при загрузке"
		soup = BeautifulSoup(response.text, "html.parser")
		joke = soup.find("div", class_="text")
		if joke:
			return joke.text.strip()
		else:
			return "беда"
	except Exception as e:
		return f"Ошибка: {e}"
if __name__=="__main__":
	joke = get_anekdot()