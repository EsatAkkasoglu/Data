#Bu program imdb2020 verilerini kullanarak ilk 1000 (film değerlendirmelerine göre) süre bazlı olarak adet tayininde kullanılır.


import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
film = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv")
pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv")
plt.style.use("Solarize_Light2")
bins = np.arange(50,260,15)
plt.xticks(bins)
plt.hist(film.duration, edgecolor="black", color="w" ,bins=bins, histtype='bar' )
plt.title("imdb film süreleri")
plt.xlabel("Süreleri")
plt.ylabel("aynı süreye sahip film sayısı") 



