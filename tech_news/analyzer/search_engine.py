# Requisito 7
# from tech_news.database import db
from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    # resolvendo com append e search_news
    search_criteria = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(search_criteria)
    response = []
    for new in news:
        response.append((new["title"], new["url"]))
    return response

    # resolvendo com retorno inserido no for loop
    # news = search_news({"title": {"$regex": f"{title}", "$options": "i"}})
    # return [(new["title"], new["url"]) for new in news]

    # resolvendo com método find direto no db
    # tuplas = []
    # news = db.news.find()
    # for new in news:
    #     if title.lower() in new["title"].lower():
    #         tuplas.append((new["title"], new["url"]))
    # return tuplas


# Requisito 8
def search_by_date(date):
    try:
        # https://docs.python.org/3/library/datetime.html?highlight=fromisoformat#datetime.date.fromisoformat
        # https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.datetime.strftime
        date_converted = datetime.fromisoformat(date).strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError('Data inválida')
    search_criteria = {"timestamp": date_converted}
    response = []
    news = search_news(search_criteria)
    for new in news:
        response.append((new["title"], new["url"]))
    return response


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
