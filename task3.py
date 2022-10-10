import json
from task2 import movies
# from pprint import pprint

def group_by_decade(movies):
    dic={}
    for i in movies:
        year=i["year"]
        decade=" "
        a=0
        for k in str(year):
            if a==3:
                j=0
                decade+=str(j)
            else:
                decade+=k
                a=a+1
            # print(decade)
        deca = decade
        # print(deca)
        if deca not in dic:
            dic[deca]=[]
            dic[deca].append(i)    
        else:
            dic[deca].append(i)
        # pprint(dic)
    # return dic
    file=open("group_by_decade","w")
    json.dump(dic,file,indent=4)
    file.close()

group_by_decade(movies)
# pprint(group_by_decade(movies))



