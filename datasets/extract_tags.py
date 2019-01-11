import json
import csv
arqName = "championFull"
arq = open(arqName+".json", "r")
jsonStr = arq.read()
dicJson = json.loads(jsonStr)
champions = dicJson["data"].keys()
filterDic = {}
for champ in champions:
    champData = dicJson["data"][champ]
    filterDic[champ] = {"champion_Name": champ,
                        "tags": champData["tags"], "stats": champData["stats"]}

with open(arqName+'.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, filterDic["Aatrox"].keys())
    w.writeheader()
    for key in filterDic.keys():
        w.writerow(filterDic[key])
