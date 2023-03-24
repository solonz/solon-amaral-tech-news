from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    headers = {"User-Agent": "Fake user-agent"}
    time.sleep(1)
    try:
        # equivalente a fetch e enviando tambem o header e timeout no parametro
        response = requests.get(url, headers=headers, timeout=3)
        # retorna o conteudo html
        # conteudo_html = response.headers["Content-Type"]
        # retorna o conteudo em texto
        conteudo_texto = response.text
        if response.status_code == 200:
            return conteudo_texto
        else:
            return None
    except requests.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news = selector.css(".entry-title a::attr(href)").getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
