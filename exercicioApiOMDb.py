import requests
r = requests.get(url='http://www.omdbapi.com/?s=matrix&type=Movie&apikey=e7333fd3')
pesquisa = r.json()
filmes = pesquisa["Search"]

# for i in range(len(filmes)):
#   if(filmes[i]["Title"]=="The Matrix Revolutions"):

for filme in filmes:

  if(filme["Title"]=="The Matrix Revolutions"):
    resultado1 = filme["Year"]

  if(filme["imdbID"]=="tt0133093"):
    resultado2 = filme["Title"]

print(resultado1, resultado2)