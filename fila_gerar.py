import requests
import pandas as pd
import sys
from time import sleep
from fake_headers import Headers

header = Headers(
    headers=False
)

referencia   = [267]
veiculo_tipo = [1, 2, 3]

fila  = pd.DataFrame()
i = 0

for tabela_referencia in referencia:

    for tipo in veiculo_tipo:
        
        try:
        
            url = f"https://veiculos.fipe.org.br/api/veiculos//ConsultarMarcas?codigoTabelaReferencia={tabela_referencia}&codigoTipoVeiculo={tipo}"    
            r_marcas = requests.post(url, headers=header.generate()).json()
            
            for marca in r_marcas:
                url_modelos = f"https://veiculos.fipe.org.br/api/veiculos//ConsultarModelos?codigoTipoVeiculo={tipo}&codigoTabelaReferencia={tabela_referencia}&codigoMarca={marca['Value']}"
                r_modelos = requests.post(url_modelos, headers=header.generate()).json()
                
                for modelo in r_modelos['Modelos']:
                    
                    url_ano_modelo = f"https://veiculos.fipe.org.br/api/veiculos//ConsultarAnoModelo?codigoTipoVeiculo={tipo}&codigoTabelaReferencia={tabela_referencia}&codigoMarca={marca['Value']}&codigoModelo={modelo['Value']}"
                    r_ano_modelo = requests.post(url_ano_modelo, headers=header.generate()).json()
                    
                    for completa in r_ano_modelo:
                        
                        i += 1
                        
                        print('URL ', i)
                        
                        ano = completa['Value'].split('-')[0]
                        combustivel  = completa['Value'].split('-')[1]
                        url_completa = f"https://veiculos.fipe.org.br/api/veiculos//ConsultarValorComTodosParametros?&codigoTabelaReferencia={tabela_referencia}&codigoMarca={marca['Value']}&codigoModelo={modelo['Value']}&codigoTipoVeiculo={tipo}&anoModelo={ano}&codigoTipoCombustivel={combustivel}&tipoConsulta=tradicional"
                        
                        fila = fila.append({'url': url_completa}, ignore_index=True)
                        
                fila.to_csv('fila.csv', index=False)
                
                sleep(1)
                
            sleep(1)
                    
        except Exception as e:
            print('algum BO', e)