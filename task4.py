import json
from unicodedata import name
import requests
from pprint import pprint
from bs4 import BeautifulSoup
with open("all_movies","r")as file:
    b=json.load(file)
    # pprint(b)
def scrape_movie_details():
    dic={}
    name_details=[]
    director_details=[]
    country_details=[]
    language_details=[]
    poster_details=[]
    bio_details=[]
    minuts_details=[]
    for i in b[:1]:
        # print(i)
        url=i["url2"]
        # pprint(url)
        response=requests.get(url)
        # print(response)
        soup=BeautifulSoup(response.text,"html.parser")
        name=soup.find("div",class_="sc-80d4314-0 fjPRnj").h1.text
        # pprint(name)
        name_details.append(name)
        director=soup.find("li",class_="ipc-metadata-list__item")
        d=director.find("a").text
        # pprint(d)
        director_details.append(d)
        country=soup.find("li",attrs={"data-testid": "title-details-origin"})
        c=country.find("a").text
        # pprint(c)
        country_details.append(c)
        language=soup.find("li",attrs={"data-testid":"title-details-languages"})
        # pprint(language)
        l=language.find("a").text
        language_details.append(l)
        poster_image_url=soup.find("img",class_="ipc-image")["src"]
        # pprint(poster_image_url)
        poster_details.append(poster_image_url)
        bio=soup.find("span",class_="sc-16ede01-0 fMPjMP").text
        # pprint(bio)
        bio_details.append(bio)
        runtime=soup.find("li",attrs={"data-testid":"title-techspec_runtime"})
        # pprint(runtime)
        
        r=runtime.find("div").text
        # pprint(r)
        run=r.split(' ')
        # print(run)
        if len(run)==4:
            minuts=int(run[0])*60+int(run[2])
        else:
            minuts=int(minuts[0])*60
        # pprint(minuts)
        minuts_details.append(minuts)
        # genre=soup.find("div",class_="poster")
        # pprint(genre)
        dic["name"]=name
        dic["director"]=director_details
        dic["country"]=country_details
        dic["language"]=language
        dic[""]
        
        pprint(dic)
        
        
        

        
scrape_movie_details()
