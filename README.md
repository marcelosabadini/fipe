# fipe 

A ideia desse projetinho é consultar os dados de todos os veículos da tabela FIPE. Os dados são retornados em um DataFrame do Pandas para que seja fácil carregar em outro lugar.

## Ambiente

- Instale o Python, recomendo o mais atual
- Depois instale as libs 
  > pip install -r requirements.txt

## Como ele funciona

O arquivo `fila_gerar.py` faz as consultas e gera uma lista de URLs que devem ser consultadas. Essa fila é salva no arquivo `fila.csv` e o arquivo `fila_processar.py` fica encarregado de executar os requests. 

Optei em fazer dessa forma para conseguir rodar em partes e caso de algum problema não seja necessário rodar toda fila novamente. 

## Como rodar

- Gerar a fila de URLS com `fila_gerar.py`
- Executar a fila com `fila_processar.py`. A cada request os dados dos veículos serão salvos em `final.csv`
- Caso ocorra algum problema e o script pare, não fique preocupado. O `fila_processar.py` faz um JOIN com o que já processou e continua o trabalho de onde parou :)

![DEMO](img/demo.PNG)

## Mais

Use, modifique, faça o que bem entender com esse código. Se fizer melhorias manda pra mim :)