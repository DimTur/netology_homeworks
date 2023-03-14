import requests
import bs4

from fake_useragent import UserAgent
ua = UserAgent()


HEADERS = {"User-Agent": ua.random}
KEYWORDS = ["дизайн", "web", "python", "виртуализация", "Производство и разработка электроники", "алгоритмы", "схемотехника"]

base_url = "https://habr.com"
url = base_url + "/ru/all/"

response = requests.get(url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")


for article in articles:
    hubs = article.find_all("a", class_="tm-article-snippet__hubs-item-link")
    hubs = set(hub.find("span").text for hub in hubs)
    # print(hubs)
    time_id = article.find_all("time")
    # print(time_id1)
    for hub in hubs:
        if hub in KEYWORDS:
            date = list(time_id[0])
            title = article.find("a", class_="tm-article-snippet__title-link")
            span_title = title.find("span").text
            href = title.attrs["href"]
            link = base_url + href
            print(f"Дата: {date} - Заголовок: {span_title} - Ссылка: {link}")