from bs4 import BeautifulSoup
from parsel import Selector
import requests
import time

from tech_news.database import create_news


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
    try:
        selector = Selector(text=html_content)
        next_pg = selector.css(".next::attr(href)").get()
    except (next_pg == ""):
        return None
    return next_pg


# Requisito 4
def scrape_news(html_content):
    sel = Selector(text=html_content)
    # https://scrapfly.io/blog/how-to-find-html-elements-by-class-with-beautifulsoup/
    soup = BeautifulSoup(html_content, 'html.parser')
    # url = sel.css("head link[rel=canonical]::attr(href)").get()
    url = sel.css("head link[rel=canonical]::attr(href)").get()
    # https://www.programiz.com/python-programming/methods/string/strip
    title = sel.css("h1.entry-title::text").get().strip()
    timestamp = sel.css("li.meta-date::text").get()
    writer = sel.css("span.author a.url::text").get()
    read_ti = int(soup.find('li', class_='meta-reading-time').text.strip()[:2])
    summary = soup.find('div', class_='entry-content').find('p').text.strip()
    category = soup.find('span', class_='label').text
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": read_ti,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = 'https://blog.betrybe.com/'
    news = []

    while len(news) < amount:
        html_content = fetch(url)
        news_links = scrape_updates(html_content)
        url = scrape_next_page_link(html_content)

        for link in news_links:
            if len(news) == amount:
                pass
            else:
                html_content = fetch(link)
                news.append(scrape_news(html_content))

    create_news(news)
    return news
