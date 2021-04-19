# fipe 

A ideia desse projetinho é poder consultar os dados de todos os veículos da tabela FIPE.

## Como ele funciona

O arquivo `fila_gerar.py` faz as consultas e gera uma lista de URLs que devem ser consultadas. Essa fila é salva no arquivo `fila.csv` e o arquivo `fila_processar.py` fica encarregado de executar os requests. 

Optei em fazer dessa forma para conseguir rodar em partes e caso de algum problema não seja necessário rodar toda fila novamente. 

- Gerar a fila de URLS com `fila_gerar.py`
- Executar a fila com `fila_processar.py`. A cada request os dados dos veículos serão salvos em `final.csv`.