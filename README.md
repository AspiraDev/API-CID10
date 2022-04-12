# API-CID10
API REST feita com python e fastapi, que retorna valores referentes à Classificação Internacional de Doenças (CID-10).

## Linguagem e bibliotecas usadas
```sh
python==3.10
fastapi==0.75.1
uvicorn==0.17.6
```

## Instalação e uso

```sh
# Clone o repositório 
git clone https://github.com/AspiraDev/API-CID10.git

# Mude o diretorio
cd API-CID10

# Instale as dependências
pip install fastapi
pip install "uvicorn[standard]"

# Rode o projeto localmente
uvicorn main:app --reload
> Acesse em http://127.0.0.1:8000
```

## Instruções
```sh
# Leia a documentação:
> http://127.0.0.1:8000/docs

# Para requests com o codigo CID:
> http://127.0.0.1:8000/cid/codigo={COGIGO}

# Para requests com o nome do CID
> http://127.0.0.1:8000/cid/codigo={NOME}

```

