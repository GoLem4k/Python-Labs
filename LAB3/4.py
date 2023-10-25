import json

with open('LAB3/firmsTask4.txt', 'r') as fileFirms:
    dictFirmsProfit = {}
    dictAverageProfit = {'average_profit': 0}
    for line in fileFirms:
        name = line.split(' ')[0]
        revenue = int(line.split(' ')[2])
        losses = int(line.split(' ')[3])
        profit = revenue - losses
        if profit >= 0:
            dictFirmsProfit[name] = profit
    dictAverageProfit['average_profit'] = sum(dictFirmsProfit.values()) / len(dictFirmsProfit)
    firmsInfo = [dictFirmsProfit, dictAverageProfit]
    
with open('firmsInfo.json', 'w') as jsonFirms:
    json.dump(firmsInfo, jsonFirms)