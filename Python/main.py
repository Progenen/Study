Tovar = {
    "Table": 3,
    "Chair": 1,
    "TV": 10
}

Cart = {}

def startDiscount (per, tovar):
    for item in tovar:
        tovar[item] = tovar[item] - (tovar[item] / 100 * per)
        print(tovar[item])
     
startDiscount(10, Tovar)



print('Максимальная цена: ', max(Tovar.items(), key=lambda k_v: k_v[1])[0])
print('Минимальная цена:', min(Tovar.items(), key=lambda k_v: k_v[1])[0])