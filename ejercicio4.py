import requests
import string
from collections import Counter

url = "https://dummyjson.com/quotes"
url2 = requests.get(url)
pagina = url2.json()
infos = pagina.get("quotes", [])
texto = " ".join(info.get("quote", "") for info in infos)
texto = texto.lower()
eliminar = ["a", "an", "the", "and", "but", "or", "for", "nor", "on", "in", "to", "at", "by", "of", "with"]
for puntuacion in string.punctuation:
    texto = texto.replace(puntuacion, "")
palabras = texto.split()
palabras_eliminar = [palabra for palabra in palabras if palabra not in eliminar]
cant = Counter(palabras_eliminar)
ranking = cant.most_common(10)
print("Ranking Top Ten de palabras más repetidas:")
if ranking:
    i=1
    for palabra, s in ranking:
        print(f"{i}°.{palabra} : {s}")




