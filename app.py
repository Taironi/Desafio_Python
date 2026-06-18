'''
Desafio: Scraper de Vagas
Prazo: Domingo, 21 de junho, às 23:00

Descrição:

Desenvolva um programa em Python capaz de coletar vagas de emprego de sites de recrutamento.
Os melhores projetos poderão ser incorporados aos nossos sistemas e os autores receberão a marcação de Programador Python no perfil.

Ferramentas sugeridas: Selenium ou API aberta/gratuita.
Mas pode utilizar o que for melhor e que funcionar. É apenas uma sugestão.
Se rodar em background sem a necessidade do Selenium, melhor ainda.

Regras:

O programa deve coletar vagas reais de um ou mais sites.
Os links retornados devem apontar diretamente para a vaga.

     Não são permitidos links para buscadores.
     Não são permitidos agregadores de vagas ou páginas intermediárias.

O projeto deve estar em um repositório público no GitHub.
O repositório deve conter:
     README.md explicando instalação e exemplo de execução.

O programa deve exportar os dados contendo, no mínimo, o link da vaga.
Um bom diferencial, mas não obrigatório, é gerar um JSON contendo:

       Link da vaga;
       Título da vaga;
       Empresa;
       Localização;

Desafios repetidos/iguais não serão aceitos
'''


import json
import requests
import os


app_key = '908e52cd859d795a9f77ba9d3f495724' 
app_id = '0b92eb27'

vagas = []
for pagina in range(1,5):
    url_api = requests.get(f'https://api.adzuna.com/v1/api/jobs/br/search/{pagina}?app_id={app_id}&app_key={app_key}').json()

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
