import requests,json
from bs4 import BeautifulSoup
# import pprint
url="https://www.imdb.com/india/top-rated-indian-movies/"
data=requests.get(url)
# print(data)
soup=BeautifulSoup(data.text,"html.parser")
# print(soup)

def scrape_top_list():
    main_div=soup.find("tbody",class_="lister-list")
    # print(main_div)
    Tr=main_div.find_all("tr")
    # #print(Tr)
    movies_list=[]
    movie_position=[]
    movie_title=[]
    movie_year=[]
    movie_rating=[]
    movie_url=[]
    for i in Tr:
        # print(i.text)
        # print(i.text)
        position=i.find("td",class_="titleColumn").get_text().strip()
        # print(position)
        Rank=" "
        for j in position:
            dic={}
            if "." not in  j:
                Rank+=j
            else:
                break
            # print(Rank)
            movie_position.append(Rank)
    #         # pprint(movie_position)
    # # ##### i find position here ####
        title=i.find("td",class_="titleColumn").a.get_text()
    #     # print(title)
        movie_title.append(title)
    #     # print(movie_title)
        year=i.find("td",class_="titleColumn").span.get_text().strip("()")
        print(year)
        movie_year.append(year)
    #     # print(movie_year)
        rate=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
    #     # print(rate)
        movie_rating.append(rate)
    # #     # #print(movie_rating)
        link=i.find("td",class_="titleColumn").a['href']
        # print(link)
        url2="https://www.imdb.com"+link
    #     # print(url2)
        movie_url.append(url2)
        dic["position"]=int(Rank)
        dic["title"]=title
        dic["year"]=int(year)
        dic["rating"]=float(rate)
        dic["url2"]=url2
    #     # pprint(dic)
        movies_list.append(dic)
        file=open("all_movies","w")
        json.dump(movies_list,file,indent=4)
        # pprint(movies_list)
        file.close()               
scrape_top_list()
