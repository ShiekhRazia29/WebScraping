from bs4 import BeautifulSoup
import requests
import json
import pprint
import time
def scrape_pickle():
    url_link="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    data=requests.get(url_link)
    soup=BeautifulSoup(data.text,'html.parser')
    #print(soup)
    main_div=soup.find("div", class_="_1gX7")
    #print(main_div)\
    products= main_div.span.get_text()
    #print(products)
    split_list=products.split(" ")
        #print(split_list)
    a=int(split_list[1])
    #print(a)
    page_num=a//32+1
    #print(page_num)
    pickle_list=[]
    number = 0
    pickle_index = 1
    while pickle_index<=page_num:
        pickles_api="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(pickle_index)
        pickles_url = requests.get(pickles_api)
        pickles_soup= BeautifulSoup(pickles_url.text,"html.parser")
        #print(pickles_soup)
        pickles_div=pickles_soup.find("div",class_="_3RA-")
        pickle_name= pickles_div.find_all("div",class_= "UGUy") #finds all the names of the pickle
        #print(pickle_name)
        pickles_price=pickles_div.find_all("div",class_="_1kMS") #find all the pickle prices data
        pickles_link=pickles_div.find_all("div",class_="_3WhJ") #finds the individual link for each item
        #print(pickles_link)
        i=0
        k=0 
        while i<len(pickle_name):
            number+=1
            pickle2_name= pickle_name[i].get_text()
            pickle_link = pickles_link[i].a["href"]
            print(k+1,".",pickle2_name)
            k+=1
            # print(pickle_link)
            pickle_price=pickles_price[1].get_text()
            # print(pickle_rate)
            pickel_url="https://paytmmall.com"+pickle_link
            pickle_details={"position":number,"name":pickle2_name,"price":pickle_price,"url":pickel_url}
            pickle_list.append(pickle_details.copy())
            i=i+1
        with open ("pickel_data.json","w") as file:
                json.dump(pickle_list,file,indent=4)
        #print(pickle_list)
        pickle_index+=1
        time.sleep(3)

    return pickle_list

scrape_pickle()

