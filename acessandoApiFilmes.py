import requests
r = requests.get(url='http://www.omdbapi.com/?s=matrix&type=Movie&apikey={API key}')
pesquisa = r.json()
filmes = pesquisa["Search"]
for filme in filmes:

  if(filme["Title"]=="The Matrix Revolutions"):
    resultado1=filme["Year"]

  if(filme["imdbID"]=="tt0133093"):
    resultado2 = filme["Title"]

print(resultado1, resultado2)