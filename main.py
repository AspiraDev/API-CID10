from typing import Optional
import json
from unidecode import unidecode
from fastapi import FastAPI

categorias = open('static/categorias.json', encoding="utf8")
subcategorias = open ('static/subcategorias.json', encoding="utf8")
capitulos = open('static/capitulos.json', encoding='utf8')

categorias = json.loads(categorias.read())
subcategorias = json.loads(subcategorias.read())
capitulos = json.loads(capitulos.read())
teste = []
app = FastAPI(
    title="API - CID-10",
    openapi_url="/api/v1/openapi.json",
    description='API que retornar valores referentes à Classificação Internacional de Doenças.',
    version="0.0.1",
    contact={
        "name": "Rogério Oliveira",
        "url": "https://github.com/AspiraDev",
        "email": "protocoloone@gmail.com",
    },
)

@app.get("/")
def read_root():
    return 'API CID-10'

@app.get("/cid/nome={cid}", tags=["nome"])
def puxar_pelo_nome(cid: Optional[str]):
    dadosSubCategorias = []
    cid = cid.capitalize()
    for i in subcategorias:
        if cid in unidecode(i['DESCRICAO']):
            sub = i['SUBCAT']

    try:
        for i in subcategorias:
            if i['SUBCAT'].startswith(sub[:3]):
                print(i['DESCRICAO'], i['SUBCAT'])
                SubCategoria = {'CodigoSubCategoria': i['SUBCAT'], 'DescricaoSubCategoria': i['DESCRICAO']}
                dadosSubCategorias.append(SubCategoria)
    except:
        dadosSubCategorias = 'SUBCATEGORIA NÃO ENCONTRADA!'

    try:
        for x in categorias:
            if x['CAT'].startswith(sub[:3]):
                dadosCategoria = {'CodigoCategoria': x['CAT'], 'DescricaoCategoria': x['DESCRICAO']}
    except:
        dadosCategoria = 'CATEGORIA NÃO ENCONTRADA!'

    try:
        for y in capitulos:
            if y['CATINIC'].startswith(sub[:1]):
                capitulo = y['DESCRICAO']
            else: 
                capitulo = 'CAPITULO NÃO ENCONTRADO!'
    except:
        capitulo = 'CAPITULO NÃO ENCONTRADO!'


    return {'Capitulo': capitulo, 'Categoria': dadosCategoria,'SubCategorias': dadosSubCategorias}

@app.get("/cid/codigo={cid}", tags=["codigo"])
def puxar_pelo_codigo(cid: Optional[str]):
    print(cid)
    cid = cid.capitalize()
    dadosSubCategorias = []
    capitulo = []
    for y in capitulos:
        if y['CATINIC'].startswith(cid[:1]):
            capitulo = y['DESCRICAO']
    
    for i in categorias:
        if i['CAT'].startswith(cid[:3]):
            dadosCategoria = {'CodigoCategoria': i['CAT'], 'DescricaoCategoria': i['DESCRICAO']}


    for x in subcategorias:
        if x['SUBCAT'].startswith(cid):
            SubCategoria = {'CodigoSubCategoria': x['SUBCAT'], 'DescricaoSubCategoria': x['DESCRICAO']}
            dadosSubCategorias.append(SubCategoria)

    return {'Capitulo': capitulo, 'Categoria': dadosCategoria,'SubCategorias': dadosSubCategorias}


