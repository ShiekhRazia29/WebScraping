from bs4 import BeautifulSoup 
import requests
import pprint
import json
my_url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(my_url)
soup=BeautifulSoup(page.text,'html.parser')
def scrape_top_list():
    main_div=soup.find('div',class_='lister')
    tbody=main_div.find('tbody',class_='lister-list')
    trs=tbody.find_all("tr")
    movie_rating=[]
    movie_name=[]
    year_of_release=[]
    movie_ranks=[]
    movie_urls=[]
    s=0
    for tr in trs:
        position=tr.find('td',class_="titleColumn").get_text().strip()
        rank=0
        for i in position:
            if '.' not in i:
                rank+=1
            else:
                break
        movie_ranks.append(rank)
        title=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(title)
        year=tr.find('td',class_="titleColumn").span.get_text()
        year_of_release.append(year)
        # imbd_rating=tr.find('td',class_="ratingColumn imbdRating").strong.get_text()
        # movie_rating.append(imbd_rating)
        link=tr.find('td',class_="titleCoumn").a['href']
        movies_link="https://www.imbd.com" +link
        movie_urls.append(movies_link)
        print(s+1,movie_name,year_of_release)
        s+=1
    Top_Movies=[]
    details={'position':'','name':'','year':'','rating':'','url':''}
    for i in range(0,len(movie_ranks)):
        details['position']=int(movie_ranks[i])
        details['name']=str(movie_name[i])
        year_of_release[i]=year_of_release[i][1:5]
        details['year']=int(year_of_release[i])
        details['rating']=float(movie_rating[i])
        details['url']=movie_urls[i]
        Top_Movies.append(details.copy()) #to create new dictionary for all the movies we use copy
        with open("Movies.json","w") as f:
            json.dump(Top_Movies,f,indent=4)
    return(Top_Movies)
# pprint.pprint(scrape_top_list())
# def group_by_year(movies):
#     years=[]
#     for i in movies:
#         year=i["year"]
#     movie_dict={i:[]for i in years}
#     for i in movies:
#         year=i["year"]
#         for x in movie_dict:
#             if str(x)==str(year):
#                 movie_dict[x].append(i)
#         return movie_dict
# print(group_by_year(scrape_top_list))
def sort_by_year():
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
    list=[]
    num=0
    for i in tr:
        num=num+1
        name = i.find("td",class_="titleColumn").a.get_text()
        #print(k+1,".",name)
        # a.append(name)
        name_1=name
        year = i.find("td",class_="titleColumn").span.get_text()[1:5]
        #print(year)
        list.append(year)
        year_1=int(year)
        movie_dict=[{"movies year":year_1,"name":name_1}]
        list.append(movie_dict)
        pprint(movie_dict)
        with open ("year.json","w") as f:
            json.dump(list,f,indent=4)
    return list
sort_by_year()