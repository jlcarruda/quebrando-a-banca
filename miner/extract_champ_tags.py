import json
import csv
arqName = "championFull"
arq = open('../datasets/'+arqName+".json", "r")
jsonStr = arq.read()
dicJson = json.loads(jsonStr)
champions = dicJson["data"].keys()
filterDic = {}
for champ in champions:
    champData = dicJson["data"][champ]
    filterDic[champ] = {"champion": champ,
                        "tags": champData["tags"]}

with open('../treasures/'+arqName+'.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, filterDic["Aatrox"].keys())
    w.writeheader()
    for key in filterDic.keys():
        w.writerow(filterDic[key])
