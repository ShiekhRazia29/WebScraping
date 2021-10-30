from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

def movies():
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    page = requests.get(url)
    # print(page)
    htmlcontent=page.content
    # print(htmlcontent)
    soup=BeautifulSoup(htmlcontent,"html.parser")
    # print(soup)
    main_div=soup.find("div",class_="lister")
    # print(main_div)
    div = main_div.find("tbody",class_="lister-list")
    # print(div)
    tr = div.find_all("tr")
    # print(tr)

    a = []
    number=0
    k=0
    for i in tr:
        number=number+1
        name = i.find("td",class_="titleColumn").a.get_text()
        #print(k+1,".",name)
        k=k+1
        # a.append(name)
        name_1=name
        year = i.find("td",class_="titleColumn").span.get_text()[1:5]
        #print(k+1,".",name,"   ",year)
        #print(year)
        #a.append(year)
        year_1=int(year)
        rating = i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        # a.append(rating)
        rating_1=float(rating)
        url = i.find("td",class_="posterColumn").a ["href"]
        # a.append(url)
        url_1="https://www.imdb.com"+url
        position={"position":number,"movies name":name_1,"movies year":year_1,"movie rating":url_1,"rating":rating_1}
        a.append(position)
        with open ("movie.json","w") as f:
            json.dump(a,f,indent=4)
    #pprint(a)
    return a
movies()
