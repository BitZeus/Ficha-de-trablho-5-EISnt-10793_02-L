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
    if len(dados) <= 1: #se os dados tiverem apenas 1 linha ou 1 item, ja esta ordenado
        return dados
    
    mid = len(dados) // 2 #define a posição central da lista dados
    L = dados[:mid] #define como L os items do inicio da lista até ao mid (posicção central)
    R = dados[mid:] #define como R os item depois do mid até ao fim da lista (posição central)
    
    L = merge_sort(L)  # volta a chamar a função para, entranto numa operação recursiva neste intervalo da lista L
    R = merge_sort(R)  # volta a chamar a função para, entranto numa operação recursiva neste intervalo da lista L
    
    i = j = k = 0
    
    #clico que compara os valores à esquerda com os da direita e posiciona consuante menor ou maior
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


#função para cacular o numero de total de vendas de cada produto, nos ultimos 10 dias de maio de 2023
def calcular_total_vendas_por_produto(dados): 
    total_vendas = {}       #criação de dicionario para melhor acesso ao valores por nome de produto
    for venda in dados:     #ciclo que cria duas listas que são ser colocados no dicionario totalvendas
        produto = venda[1] 
        quantidade = int(venda[3])
        if produto in total_vendas:
            total_vendas[produto] += quantidade #se o produto ja se encontar no dicionario, incrementa com a quantidade de venda
        else: 
            total_vendas[produto] = quantidade  #se o produto ainda nao se encontrar no dicionario, coloca como quantidade inicial de vendas a propria quantidade
    return total_vendas



# função apresenta dados no grafico. Apresenta o total de vendas por produto de forma ascendente
def apresentar_resultados(dados):
    total_vendas = calcular_total_vendas_por_produto(dados) #chama a função para calcular o total de vendas por produto e guarda em total_vendas 
    dados_ordenados = merge_sort(list(total_vendas.items()))  # Converte o dicionário em uma lista de tuplas e chama o metodo merge sort
    
    produtos = [produto for produto, _ in dados_ordenados]    #list comprehension que coloca no nome do produto na lista produtos
    vendas = [quantidade for _, quantidade in dados_ordenados] #list comprehension que coloca o numero de vendas do produto na lista quantidade
    
    plt.bar(produtos, vendas)                   #define o grafico a ser visualizado, grafico de barras verticais e a origem dos dados
    plt.xlabel('Produtos')                      #eixo horizontal com o nome dos produtos
    plt.ylabel('Número de Vendas')              #eixo vertical com o nr total de vendas
    plt.title('Total de vendas Produto')        #Titulo dda janela do grafico
    plt.show()                                  #apresenta a janela do grafico no ecran



dados = importar_dados('AtividadePedagogica4_10793_02.csv') #caminho para o ficheiro com os dados
dados_ordenados = quick_sort(dados) #chama a função quickstort para listas medias.
apresentar_resultados(dados_ordenados) #chama a função para criar e exibir a janela do gráfico.
