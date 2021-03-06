import requests
from bs4 import BeautifulSoup as bs


def getData():
    BASE_URL = "https://www.pcgamer.com/news/"
    try:
        r = requests.get(BASE_URL)
    except Exception as e:
        print(e)
        exit(-1)
    soup = bs(r.content, "lxml")
    dataList = soup.findAll("div", {"data-page": 1})
    news = []
    for data in dataList:
        #        title = data.find("a").get("aria-label")
        try:
            title = data.find("h3", class_="article-name").text
        except BaseException:
            title = ""
        try:
            url = data.find("a").get("href")
        except BaseException:
            url = ""
        try:
            content = data.find(
                "p",
                class_="synopsis").text.replace("news","").replace("Deals","").replace("News\n","")
        except BaseException:
            content = ""
        try:
            img = data.find(
                "div", class_="image-remove-reflow-container landscape").get("data-original")
        except BaseException:
            img = ""

        newsData = {
                "title": title,
                "content": content,
                "imageUrl": img,
                "newsUrl": url}
        news.append(newsData)
    return news

# print(getData())
# print(len(getData()))
