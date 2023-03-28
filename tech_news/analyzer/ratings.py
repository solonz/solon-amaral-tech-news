from tech_news.database import find_news
import pandas as pd


# Requisito 10
# https://datagy.io/python-count-occurrences-in-list/
# https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
# https://towardsdatascience.com/3-ways-to-count-the-item-frequencies-in-a-python-list-89975f118899
def top_5_categories():
    categories = []
    news = find_news()

    for new in news:
        categories.append(new["category"])

# https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html?highlight=value_counts#pandas.Series.value_counts
    ranking = pd.Series(categories).value_counts().sort_index()

# https://www.w3schools.com/python/pandas/ref_df_nlargest.asp
# https://www.geeksforgeeks.org/python-pandas-series-tolist/
    return ranking.nlargest(5).index.tolist()
