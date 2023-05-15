import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.data = []

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Encontre aqui os elementos HTML que deseja coletar os dados
        for element in soup.find_all('div', class_='example'):
            data_point = element.get_text()
            self.data.append(data_point)

    def print_data(self):
        for data_point in self.data:
            print(data_point)

# Exemplo de uso
url = 'https://www.example.com'
scraper = WebScraper(url)
scraper.scrape()
scraper.print_data()
