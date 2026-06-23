import requests
import pandas as pd

# Credenciais extraídas (lembre-se de colar o token completo)
API_KEY = "aa9228bde116e0eb901daaf2a7846224"
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYTkyMjhiZGUxMTZlMGViOTAxZGFhZjJhNzg0NjIyNCIsIm5iZiI6MTc4MTY1NDE3My42NTY5OTk4LCJzdWIiOiI2YTMxZTI5ZGU2ODBmM2IxZDczZDk5MjAiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.raI7nCRoHgNi8Rh9yTyr8OM4jukrDwg-0Bd-5U9ibRQ" # Insira o token completo da imagem aqui

# Endpoint para filmes atualmente nos cinemas
url = "https://api.themoviedb.org/3/movie/now_playing"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

params = {
    "language": "pt-BR",
    "region": "BR",
    "page": 1
}

# Iniciando a extração 
print("Interceptando dados da API...")
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    
    # Estruturando os dados brutos
    df_filmes = pd.DataFrame(data['results'])
    
    # Filtrando as colunas mais relevantes
    df_limpo = df_filmes[['title', 'release_date', 'vote_average', 'popularity']]
    df_limpo = df_limpo.sort_values(by='popularity', ascending=False)
    
    print("\n✅ Download concluído. Filmes em alta no momento:\n")
    print(df_limpo.head())
    
else:
    print(f"❌ Falha na injeção de bytes. Erro: {response.status_code} - {response.text}")
