import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_to_dataframe(xml_file):
    # Parse o arquivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Crie listas para armazenar os dados
    data = {
        'codigo': [],
        'nome': [],
        'comentario': [],
        'preco': [],
        'quantidade': [],
        'desconto (%)': [],
        'Valor Unitário Máximo Aceitável': [],
        'Valor Total Máximo Aceitável': []
    }

    # Percorra os elementos do XML e extraia os dados relevantes
    for item in root.findall('.//item'):
        codigo = item.find('codigo').text if item.find('codigo') is not None else ''
        nome = item.find('nome').text if item.find('nome') is not None else ''
        comentario = item.find('comentario').text if item.find('comentario') is not None else ''
        preco = item.find('preco').text if item.find('preco') is not None else ''
        quantidade = item.find('quantidade').text if item.find('quantidade') is not None else ''
        
        data['codigo'].append(codigo)
        data['nome'].append(nome)
        data['comentario'].append(comentario)
        data['preco'].append(preco)
        data['quantidade'].append(quantidade)
        data['desconto (%)'].append(None)  # Coluna vazia
        data['Valor Unitário Máximo Aceitável'].append(None)  # Coluna vazia
        data['Valor Total Máximo Aceitável'].append(None)  # Coluna vazia

    # Crie um DataFrame a partir dos dados
    df = pd.DataFrame(data)

    return df

# Exemplo de uso
xml_file = 'seu_arquivo.xml'
df = parse_xml_to_dataframe(xml_file)
df.to_json('saida.json', orient='records', lines=True)
