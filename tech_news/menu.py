import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_title
from tech_news.scraper import get_tech_news


# Requisitos 11 e 12
def news_qtt():
    qtt = input("Digite quantas notícias serão buscadas:")
    print(get_tech_news(qtt))


def search_title():
    title = input("Digite o título:")
    print(search_by_title(title))


def search_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(date))


def search_category():
    category = input("Digite a categoria:")
    print(search_by_category(category))


# def saida():
#     print("Encerrando script")


# https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
# https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
def analyzer_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )

    options = {
        "0": news_qtt,
        "1": search_title,
        "2": search_date,
        "3": search_category,
        "4": lambda: top_5_categories(),
        "5": lambda: print("Encerrando script"),
    }

    try:
        print(options[user_input]())
    except KeyError:
        sys.stderr.write("Opção inválida\n")
