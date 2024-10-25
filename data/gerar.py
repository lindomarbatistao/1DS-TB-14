import pandas as pd
import os

data = {
    'tituloProduto':['furadeira','parafusadeira'],
    'preco':[500, 250],
    'descricao':['Furar paredes', 'Parafusar coisas'],
    'imagemProduto':['/images', '/images'],
    'categoriaProduto': ['Ferramentas','Ferramentas' ],
    'classProduto':['Manual', 'Manual'],
    'exibirHome':[True, False]
}

df = pd.DataFrame(data)

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace('\\', '/')

df.to_csv(caminho_final+'/data/ferramentas.csv', index=False)