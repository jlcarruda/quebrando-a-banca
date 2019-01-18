import json
import csv
arqName = "dicSkills"
arq = open(arqName+".txt", "r")
jsonStr = arq.read()
dicJson = json.loads(jsonStr)
with open(arqName+'.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, dicJson["Dragon's Descent"].keys())
    w.writeheader()
    for key in filterDic.keys():
        w.writerow(filterDic[key])
