data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

listina = []

def maxvrednost():
    for k, v in data.items():
        listina.append(max(v))
    print(listina)

stupid = maxvrednost()
