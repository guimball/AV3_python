import requests
from bs4 import BeautifulSoup


class Parser:

  def parse(self, html):
    raise NotImplementedError


class DataExtractor:

  def extract(self, soup):
    raise NotImplementedError


class BeautifulSoupParser(Parser):

  def parse(self, html):
    return BeautifulSoup(html, 'html.parser')


class CustomDataExtractor(DataExtractor):

  def extract(self, soup):
    data = []
    h3_tags = soup.find_all('h3')
    for tag in h3_tags:
      data.append(tag.text)
    return data


class Scraper:

  def __init__(self, parser, data_extractor):
    self.parser = parser
    self.data_extractor = data_extractor

  def scrape(self, url):
    response = requests.get(url)
    if response.status_code == 200:
      html = response.text
      soup = self.parser.parse(html)
      data = self.data_extractor.extract(soup)
      return data
    else:
      print(f"Erro ao acessar a URL: {response.status_code}")
      return None


# Exemplo de uso
if __name__ == "__main__":
  parser = BeautifulSoupParser()
  data_extractor = CustomDataExtractor()
  scraper = Scraper(parser, data_extractor)

  url = "https://guimball.github.io/projectCecilia/"
  data = scraper.scrape(url)
  print(data)
