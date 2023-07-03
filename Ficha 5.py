import csv
import matplotlib.pyplot as plt

# Importar Dados do ficheiro e ler como formato csv
def importar_dados(arquivo):
    dados = []
    with open(arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)  # Pular a primeira linha 
        for linha in leitor_csv:
            dados.append(linha)
    return dados

#função com o algoritmo de ordenação Quick Sort
def quick_sort(dados):
    if len(dados) <= 1:
        return dados
    
    pivot = dados[(len(dados)//2)][1]
    menores = [x for x in dados if (x[1]) < pivot]
    medios = [x for x in dados if (x[1]) == pivot]
    maiores = [x for x in dados if (x[1]) > pivot]
    
    return quick_sort(menores) + medios + quick_sort(maiores)

#Função com o algortimo de ordenação Merge Sort
def merge_sort(dados):
    if len(dados) <= 1:
        return dados
    
    mid = len(dados) // 2 #define como meio o valor correspondente a metade da lista dados
    L = dados[:mid] 
    R = dados[mid:]
    
    L = merge_sort(L)  # Atribuir o retorno à lista L
    R = merge_sort(R)  # Atribuir o retorno à lista R
    
    i = j = k = 0
    
    while i < len(L) and j < len(R):
        if L[i][1] < R[j][1]:
            dados[k] = L[i]
            i += 1
        else:
            dados[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        dados[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        dados[k] = R[j]
        j += 1
        k += 1
    
    return dados  



def calcular_total_vendas_por_produto(dados): 
    total_vendas = {} 
    for venda in dados: 
        produto = venda[1] 
        quantidade = int(venda[3])
        if produto in total_vendas:
            total_vendas[produto] += quantidade
        else: 
            total_vendas[produto] = quantidade 
    return total_vendas



# função apresenta dados no grafico. Apresenta o total de vendas por produto de forma ascendente
def apresentar_resultados(dados):
    total_vendas = calcular_total_vendas_por_produto(dados)
    dados_ordenados = merge_sort(list(total_vendas.items()))  # Converte o dicionário em uma lista de tuplas e chama o metodo merge sort
    
    produtos = [produto for produto, _ in dados_ordenados]
    vendas = [quantidade for _, quantidade in dados_ordenados]
    
    plt.bar(produtos, vendas)
    plt.xlabel('Produtos')
    plt.ylabel('Número de Vendas')
    plt.title('Produtos e suas Vendas')
    plt.show()



dados = importar_dados('AtividadePedagogica4_10793_02.csv')
dados_ordenados = quick_sort(dados)
apresentar_resultados(dados_ordenados)
