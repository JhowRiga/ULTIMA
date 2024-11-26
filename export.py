import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_to_dataframe(xml_files):
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

    # Percorra os arquivos XML
    for xml_file in xml_files:
        # Parse o arquivo XML
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Extraia os dados relevantes de cada item no XML
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
            data['desconto (%)'].append(None)
            data['Valor Unitário Máximo Aceitável'].append(None)
            data['Valor Total Máximo Aceitável'].append(None)

    # Crie um DataFrame a partir dos dados
    df = pd.DataFrame(data)
    return df

# Lista de arquivos XML
xml_files = ['seu_arquivo1.xml', 'seu_arquivo2.xml', 'seu_arquivo3.xml', 'seu_arquivo4.xml']

# Processar os arquivos XML e gerar o DataFrame
df = parse_xml_to_dataframe(xml_files)

# Exporta o DataFrame para um arquivo JSON
df.to_json('saida.json', orient='records', lines=True)
