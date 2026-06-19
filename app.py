import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

vagas = []
for pagina in range(1,5):
    url_api = requests.get(f'https://api.adzuna.com/v1/api/jobs/br/search/{pagina}?app_id={os.getenv("ADZUNA_APP_ID")}&app_key={os.getenv("ADZUNA_APP_KEY")}').json()

    for vaga in url_api["results"]:
          vagas.append({
               "link": vaga["redirect_url"],
               "titulo": vaga["title"],
               "empresa": vaga["company"]["display_name"],
               "localizacao": vaga["location"]["display_name"]
          })

if not os.path.exists("lista_vagas.json"):
     with open("lista_vagas.json", "w", encoding="utf-8") as arquivo:
          json.dump(vagas, arquivo, indent=2, ensure_ascii=False)
          print("Vagas exportadas para lista_vagas.json")
else:
     print("O arquivo vagas.json já existe. Por favor, remova-o para exportar novamente.")
