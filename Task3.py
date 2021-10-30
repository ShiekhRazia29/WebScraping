from bs4 import BeautifulSoup
import requests 
import json
from Task2 import *
#d=group_by_year(movies)
dec_arg=group_by_year(r)
def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:#takes year from the movies
        mod=index%10 #gets the movies after moding 
        decade=index-mod #eg index=1959 mod=9 decade=1959-9=1950
        if decade not in list1:
            list1.append(decade) #appends if not found in list
    list1.sort() #sorts the year list of movies
    #print(list1)
    for i in list1:
        moviedec[i]=[] #creates a list for each yea
    for i in moviedec:
         dec10=i+9
         for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
            with open("Decade.json","w") as y:
                json.dump(moviedec,y,indent=4) 
         #print(moviedec)   
    return(moviedec)
group_by_decade(dec_arg)