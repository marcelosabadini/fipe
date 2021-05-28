import requests
import pandas as pd
import sys
from time import sleep
from fake_headers import Headers
from random import randint
from tqdm import tqdm

# Esse cara cria o cabeçalho fake para cada requisição
header = Headers(
    headers=False
)

try:
    # todas URLS
    fila  = pd.read_csv('fila.csv')
    # o que já foi consultado
    final = pd.read_csv('final.csv')
    
    # Configura a barra de rolagem. Seta o tamanho total (fila) e inicia o contador com o que já foi consultado.
    bar = tqdm(total=len(fila), initial=len(final))
    
    # join entre fila -> final
    fila = pd.merge(fila, final, on='url', how='outer', indicator=True)
    
    print('\nFila:', len(fila), 'Processado: ', len(final), end=', ')
    
    # separa somente o que esta no lado esquerdo, ou seja, na fila e que ainda nao foi consultado
    fila = fila[fila['_merge'] == 'left_only']
    
    print('Falta: ', len(fila))
    
    for i, row in fila.iterrows():
        
        # Atualiza a progress bar
        bar.update(1)
        
        r_final = requests.post(row['url'], headers=header.generate()).json()
        
        # coloca a URL no dataframe final, pois o JOIN é feito com ela
        r_final['url'] = row['url']
        
        final = final.append(r_final, ignore_index=True)
        
        # grava no disco, pra poder ficar sempre up to date.
        final.to_csv('final.csv', index=False)
        
        sleep(randint(1,2))
        
        # A cada 30 requests vamos deixar o servidor descansar
        if i % 30 == 0:
            sleep(30)
       
except Exception as e:
    print('algum BO', e)