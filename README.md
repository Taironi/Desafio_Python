# Scraper de Vagas com Python

## Sobre o Projeto

Este projeto foi desenvolvido para coletar vagas de emprego utilizando a API pública da Adzuna.

O script realiza a consulta de múltiplas páginas de resultados, extrai informações relevantes das vagas e exporta os dados para um arquivo JSON.

## Funcionalidades

* Coleta vagas reais através da API da Adzuna.
* Consulta múltiplas páginas de resultados.
* Exporta os dados para um arquivo JSON.
* Não utiliza Selenium.
* Utiliza variáveis de ambiente para proteger credenciais da API.

## Dados Coletados

Para cada vaga são armazenados:

* Link da vaga
* Título da vaga
* Empresa
* Localização

## Tecnologias Utilizadas

* Python 3
* Requests
* Python Dotenv
* JSON

## Estrutura do Projeto

```text
.
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/scraper-vagas.git
cd scraper-vagas
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou:

```bash
pip install requests python-dotenv
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
ADZUNA_APP_ID=seu_app_id
ADZUNA_APP_KEY=sua_app_key
```

Para obter as credenciais:

1. Crie uma conta na plataforma Adzuna.
2. Gere seu APP ID e APP KEY.
3. Adicione os valores ao arquivo `.env`.

### Exemplo de arquivo `.env.example`

```env
ADZUNA_APP_ID=
ADZUNA_APP_KEY=
```

## Execução

Execute o script:

```bash
python main.py
```

## Saída

Ao executar o programa será gerado o arquivo:

```text
lista_vagas.json
```

Exemplo de saída:

```json
[
  {
    "link": "https://exemplo.com/vaga",
    "titulo": "Desenvolvedor Python",
    "empresa": "Empresa Exemplo",
    "localizacao": "São Paulo"
  }
]
```

## Como Funciona

O programa:

1. Carrega as credenciais da API através do arquivo `.env`.
2. Consulta as páginas 1 a 4 da API da Adzuna.
3. Extrai os dados das vagas encontradas.
4. Armazena os resultados em uma lista.
5. Exporta os dados para o arquivo `lista_vagas.json`.

## Dependências

Arquivo `requirements.txt`:

```text
requests
python-dotenv
```

## Observações

* O arquivo `.env` não deve ser enviado ao GitHub.
* Recomenda-se adicionar `.env` ao `.gitignore`.
* O arquivo JSON é criado apenas se não existir previamente.

## Autor

Projeto desenvolvido como solução para o desafio de coleta de vagas utilizando Python e API pública.
