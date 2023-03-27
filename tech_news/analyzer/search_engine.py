# Requisito 7
# from tech_news.database import db
from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
