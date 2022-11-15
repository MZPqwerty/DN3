emso = input("Vnesite emso: ")
leto = 2022
starost = []

def izracun():
    for i in range(len(emso)):
        if i == 4:
            if int(emso[i]) > 0:
                starost.append('1')
                starost.append(emso[i])
            else:
                starost.append('2')
                starost.append(emso[i])
        elif i == 5 or i == 6:
            starost.append(emso[i])
    print("Stari ste " + str(leto - int(''.join(starost))) + " let.")

letostarosti = izracun()