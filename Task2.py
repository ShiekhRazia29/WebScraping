import json
from Task1 import movies
r=movies()
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["movies year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        year=i["movies year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
                # print(movie_dict)
                with open("years.json","w") as t:
                   json.dump(movie_dict,t,indent=4)
    return movie_dict
group_by_year(r)
        
