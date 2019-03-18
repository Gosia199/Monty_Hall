import random
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import seaborn as sns

A = "A"
B = "B"
C = "C"

defeat = 0
win = 1

def game():
    drzwi = [A, B, C]
    bolean = [True, False]
    winning = random.choice(drzwi)
    choice = random.choice(drzwi)
    change = random.choice(bolean)

    if winning == choice:
        if change:
            return defeat, change
        else:
            return win, change
    if winning != choice:
        if change:
            return win, change
        else:
            return defeat, change
game()

n = int(input("Podaj ilość rozegranych gier:"))
results = []
for i in range(n):
    results.append(game())

uzyskane_wyniki = dict(Counter(results))
print("uzyskane wyniki = ", uzyskane_wyniki)

wyniki = []
ilosc = []
for k, v in uzyskane_wyniki.items():
    wyniki.append(list(k))
    ilosc.append(v)

wygrana = []
zmiana = []
for k, v in wyniki:
    wygrana.append(k)
    zmiana.append(v)

def percent(x):
    return round((x / n) * 100, 2)

df = pd.DataFrame()
df["wynik"] = wyniki
df["wygrana"] = wygrana
df["zmiana"] = zmiana
df["ilość"] = ilosc
df["procent"] = df["ilość"].apply(percent)
x = df.sort_values(by='ilość', ascending=False)
x.index = ["a", "b", "c", "d"]
x

sns.set(style="darkgrid")
abc = x['wygrana'].map(str) +" "+ x['zmiana'].map(str)
plt.bar(abc,x["procent"],align='center')
plt.show()
plt.pie(df['procent'], labels = abc, shadow = True, explode=[0.1,0.1,0,0] )
plt.show()
