import json
# from pprint import pprint
with open("all_movies","r")as file:
    movies=json.load(file)
    # pprint(movies)

def group_by_year():
    dict1={}
    for i in movies:
        # print(i)
        a=i["year"]
        # print(a)
        if a not in dict1:
            dict1[a]=[]
        else:
            dict1[a].append(i)
        # pprint(dict1)
    file=open("all_ group_movie","w")
    json.dump(dict1,file,indent=4)
    # pprint(dict1)
    file.close()
group_by_year()    
    
    

