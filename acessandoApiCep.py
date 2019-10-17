import requests
r = requests.get(url='https://viacep.com.br/ws/63100020/json/')
cep = r.json()
print(cep)
