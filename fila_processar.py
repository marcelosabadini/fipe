import requests
import pandas as pd
import sys
from time import sleep
from fake_headers import Headers
from random import randint
from tqdm import tqdm

bar = tqdm()

header = Headers(
    headers=False
)

df = pd.read_csv('final.csv')

try:
    fila  = pd.read_csv('fila.csv')
    final = pd.read_csv('final.csv')
    
    # join entre fila -> final
    fila = pd.merge(fila, final, on='url', how='outer', indicator=True)
    
    # separa somente o que esta no lado esquerdo, na fila que ainda nao foi consultado
    fila = fila[fila['_merge'] == 'left_only']
    
    bar.total = len(fila)
    
    for i, row in fila.iterrows():
        
        bar.update(1)
        
        r_final = requests.post(row['url'], headers=header.generate()).json()
        
        r_final['url'] = row['url']
        
        df = df.append(r_final, ignore_index=True)
        
        # grava no disco, pra poder ficar sempre up to date.
        df.to_csv('final.csv', index=False)
        
        sleep(randint(0,3))
       
except Exception as e:
    print('algum BO', e)