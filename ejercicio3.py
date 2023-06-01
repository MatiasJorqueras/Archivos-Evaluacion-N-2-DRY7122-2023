import requests

url = "https://dummyjson.com/quotes"
archivo = "endpoint.csv"
url2 = requests.get(url)
pagina = url2.json()
infos = pagina.get("quotes", [])
autor = [info.get("author", "") for info in infos]
texto = [info.get("text", "") for info in infos]

datos = []
for author, text in zip(autor, texto):
    linea = f"{author}\t{text}"
    datos.append(linea)
with open(archivo, "w") as info:
    info.write ("\n".join(datos))

print(f"Los datos han sido insertados dentro del archivo {archivo}")
with open(archivo, "r") as prueba:
    print("\n")
    print(f"Comprobación de los datos insertados en {archivo}")
    print(prueba.read())
