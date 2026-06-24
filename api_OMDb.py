
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests

API_KEY = "b570c69b"

def get_api_key() -> str:
    return os.environ.get("OMDB_API_KEY") or API_KEY

BASE_URL = "https://www.omdbapi.com/"

def get_movie(title: str, year: int | None = None, full_plot: bool = True) -> dict:
    params = {
        "apikey": get_api_key(),
        "t": title,
        "plot": "full" if full_plot else "short"
    }
    if year:
        params["y"] = year

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def get_movie_by_id(imdb_id: str, full_plot: bool = True) -> dict:
    params = {
        "apikey": get_api_key(),
        "i": imdb_id,
        "plot": "full" if full_plot else "short"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def search_movies(query: str, page: int = 1) -> dict:
    params = {
        "apikey": get_api_key(),
        "s": query,
        "page": page
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("=" * 60)
    print("Exemplo 1: Busca por titulo")
    print("=" * 60)
    movie = get_movie("Inception")
    print(f"Titulo: {movie.get('Title')}")
    print(f"Ano: {movie.get('Year')}")
    print(f"Genero: {movie.get('Genre')}")
    print(f"Diretor: {movie.get('Director')}")
    print(f"Sinopse: {movie.get('Plot')}")
    print(f"Poster: {movie.get('Poster')}")

    print("\n" + "=" * 60)
    print("Exemplo 2: Busca por ID IMDb")
    print("=" * 60)
    movie = get_movie_by_id("tt1375666")
    print(f"Titulo: {movie.get('Title')}")
    print(f"IMDb ID: {movie.get('imdbID')}")

    print("\n" + "=" * 60)
    print("Exemplo 3: Busca generica")
    print("=" * 60)
    results = search_movies("Batman")
    for item in results.get("Search", []):
        print(f"- {item.get('Title')} ({item.get('Year')}) - {item.get('imdbID')}")


#tem que rodar no terminal: python "nome_da_pasta.py"