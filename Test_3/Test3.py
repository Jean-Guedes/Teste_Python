import json
import xml.etree.ElementTree as ET
import os

# Função para leitura do arquivo, retornando um lista de objetos contendo os faturamentos por dia e valor.
def carregar_faturamento(arquivo):
    extensao = os.path.splitext(arquivo)[-1].lower()
    
    if extensao == '.json':
        with open(arquivo, 'r') as file:
            data = json.load(file)
            faturamento = [(dia['dia'], dia['valor']) for dia in data if dia['valor'] > 0] # Criação de uma Lista através de um list comprehension, recuperarndo apenas caso o valor seja maior que 0
    
    elif extensao == '.xml':
        tree = ET.parse(arquivo)
        root = tree.getroot()
        faturamento = [(int(dia.find('dia').text), float(dia.find('valor').text)) 
                       for dia in root.findall('dia') if float(dia.find('valor').text) > 0] # Criação de uma Lista através de um list comprehension, recuperarndo apenas caso o valor seja maior que 0
    
    else:
        raise ValueError("Formato de arquivo não suportado. Use .json ou .xml.")
    
    return faturamento

# Função para calcular o faturamento, recebendo o caminho do arquivo, e retornando duas tuplas (representando o menor e maior faturamento) e uma lista de valores inteiros
def calcular_faturamento(faturamento):
    # Encontrar o menor e maior valor de faturamento e os dias correspondentes
    menor_faturamento = min(faturamento, key=lambda x: x[1]) # função anônima para recuperar o valor da tupla, no index 1
    maior_faturamento = max(faturamento, key=lambda x: x[1]) # função anônima para recuperar o valor da tupla, no index 1
    
    # Calcular a média de faturamento mensal (ignorando dias sem faturamento)
    media_mensal = sum(valor for _, valor in faturamento) / len(faturamento) # Variável '_' como placeholder
    
    # Encontrar os dias com faturamento acima da média
    dias_acima_da_media = [dia for dia, valor in faturamento if valor > media_mensal]
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Função para escolher o formato do arquivo. Retorna o caminho do escolhido como string.
def escolher_arquivo():
    print("Escolha o arquivo para carregar o faturamento:")
    print("1. faturamento.json")
    print("2. faturamento.xml")
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        return 'faturamento.json'
    elif escolha == '2':
        return 'faturamento.xml'
    else:
        print("Escolha inválida! Tente novamente.")
        return escolher_arquivo()

# Main:
arquivo = escolher_arquivo() # Escolher o caminho.
faturamento = carregar_faturamento(arquivo) # Ler caminho do arquivo.
menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(faturamento) # Recuperar os valores
total_dias_acima_da_media = len(dias_acima_da_media) # Calcula o número de dias em que o faturamento ficou acima da média.

print(f"Menor valor de faturamento: {menor_faturamento[1]} - no dia {menor_faturamento[0]}")
print(f"Maior valor de faturamento: {maior_faturamento[1]} - no dia {maior_faturamento[0]}")
if total_dias_acima_da_media > 1:
    print(f"Numero de dias com faturamento acima da média: {total_dias_acima_da_media} - nos dias: {dias_acima_da_media}")
elif total_dias_acima_da_media == 1:
    print(f"Numero de dias com faturamento acima da média: {total_dias_acima_da_media} - no dia {dias_acima_da_media[0]}")
else:
    print("Não houveram dias em que o faturamento ficou acima da média.")
