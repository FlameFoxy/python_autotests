import requests
HOST='https://api.pokemonbattle.me:9104'

response=requests.post(url=f'{HOST}/pokemons', 
              json={
                  "name": "Тестермон",
                  "photo": "https://dolnikov.ru/pokemons/albums/001.png"
              },
              headers={"trainer_token": "e6309cbd44815c4173731f08cd174555", 
              'Content-Type': 'application/json'}, timeout=5)

print('Создать покемона')
print(response.json()) 

response=requests.put(url=f'{HOST}/pokemons',
                      json={
                          "pokemon_id": '19841',
                          "name": "Тестермон Петрович",
                          "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                      headers={"trainer_token": "e6309cbd44815c4173731f08cd174555", 
                      'Content-Type': 'application/json'}, timeout=5)
print(' ')
print('Переименовать покемона')
print(response.json()) 

response=requests.post(url=f'{HOST}/trainers/add_pokeball',
                       json={
                           "pokemon_id": '19841'
                       },
                       headers={"trainer_token": "e6309cbd44815c4173731f08cd174555", 
                      'Content-Type': 'application/json'}, timeout=5)
print(' ')
print('Поймать покемона')
print(response.json()) 