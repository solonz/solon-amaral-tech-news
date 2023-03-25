def scrape_news(html_content):
    sel = Selector(text=html_content)
    url = sel.css("head > link:nth-child(10)").get()
    print(url)