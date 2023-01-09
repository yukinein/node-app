import pandas as pd
import time
import random

start = time.time()
'''Data girişi'''
data = pd.read_csv('winequality-red.csv', sep=';')
'''Datalardan kullanacağımız sütunları ve cevap sütununu ayırdık'''
a = data['fixed acidity'].values.tolist()
b = data['volatile acidity'].values.tolist()
c = data['quality'].values.tolist()

ab = list(zip(a, b))

def OklidUzakligi(nokta1, nokta2):
    return pow(((nokta1[0] - nokta2[0]) ** 2) + ((nokta1[1] - nokta2[1]) ** 2), 1 / 2)

def NoktalariBul(veri):
    K = 5
    C = [None] * K
    for Kmeans in range(0, K):
        rastgele = random.randint(0, len(a))
        C[Kmeans] = (a[rastgele], b[rastgele])
    print(C)
    for tirt in range(0, len(veri)):
        kListeleri = [[] for i in range(K)]
        for i in range(0, len(a)):
            tempListe = [[]] * K
            for z in range (0, K):
                tempListe[z] = ((OklidUzakligi(veri[i], C[z])), z)
            tempListe = (min(tempListe))
            for acem in range(0, K):
                if tempListe[1] == acem:
                    kListeleri[acem].append(veri[i])
        Ctemp = [None] * K
        for vov in range(0, K):
            newC = [sum(x) for x in zip(*kListeleri[vov])]
            newC[0] = newC[0] / len(kListeleri[vov])
            newC[1] = newC[1] / len(kListeleri[vov])
            Ctemp[vov] = newC
        if Ctemp == C:
            break
        C = Ctemp

    C.sort(key=lambda x: x[0])
    print(C)


NoktalariBul(ab)


end = time.time()
print("Algoritma icra süresi", end - start, "saniye")