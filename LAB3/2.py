with open('LAB3/productsTask2.txt', 'r') as fileProducts:
    lines = fileProducts.readlines()
    productDict = {}

    for line in lines:
        item = line.replace('\n', '').split(' ')
        productDict[item[0]] = int(item[1])
    
    print('Товары стоимостью от 10 до 50:')
    for item in productDict:
        if productDict[item] > 10 and productDict[item] < 50:
            print(item, productDict[item])
            
    print('Товар с наибольшей стоимостью:')
    print(max(productDict, key = productDict.get), max(productDict.values()))