# Scraper de Vagas com Python

## Descrição

Projeto desenvolvido para coletar vagas de emprego utilizando a API pública da Adzuna.

O programa consulta múltiplas páginas de resultados, extrai informações relevantes das vagas e exporta os dados para um arquivo JSON.

Os dados coletados incluem:

* Link da vaga
* Título da vaga
* Empresa
* Localização

## Tecnologias Utilizadas

* Python 3
* Requests
* JSON

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/scraper-vagas.git
cd scraper-vagas
```

Instale as dependências:

```bash
pip install requests
```

## Configuração

No arquivo principal, configure suas credenciais da API Adzuna:

```python
app_id = "SEU_APP_ID"
app_key = "SEU_APP_KEY"
```

Caso ainda não possua credenciais, crie uma conta na Adzuna e obtenha sua chave de acesso.

## Execução

Execute o programa:

```bash
python main.py
```

## Saída

Após a execução será gerado o arquivo:

```text
lista_vagas.json
```

Exemplo de saída:

```json
[
  {
    "link": "https://...",
    "titulo": "Desenvolvedor Python",
    "empresa": "Empresa Exemplo",
    "localizacao": "São Paulo"
  }
]
```

## Funcionalidades

* Consulta vagas reais através da API Adzuna.
* Coleta vagas de múltiplas páginas.
* Exporta os resultados para JSON.
* Não utiliza Selenium.
* Pode ser executado em background ou agendado via cron/Task Scheduler.

## Estrutura do Projeto

```text
.
├── main.py
├── lista_vagas.json
└── README.md
```

## Observações

Os links retornados são fornecidos pela API da Adzuna e apontam para as respectivas vagas divulgadas pelos recrutadores e plataformas de recrutamento.

## Autor

Projeto desenvolvido como solução para o desafio "Scraper de Vagas".
