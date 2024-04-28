'''
Alunos: 
    Guilherme A. Ponce (2011179)
    João Victor Godinho W. (2011401)

'''

#Encontrar o K-esimo maior elemento da lista

from random import randint
from time import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def BubbleFiveSort(A): #ordena uma lista de 5 elementos. Retorna mediana | (O(cst. * cst.))

    tam = len(A) #sempre sera 5, entao a complexidade dos fors sera tempo cst.
                 #so nao hard coded o numero 5 nos ranges pq temos ainda que fazer o bubble sort da particao 

    for i in range(0,tam):
        for j in range(0,tam):
            if(j+1 >= tam):
                break #lista esta ordenada
            elif(A[j] > A[j+1]):
                buf = A[j+1]
                A[j+1] = A[j]
                A[j] = buf

    #print("fim de bubble sort!",A)

    if(tam%2 != 0): #lista impar
        return A[tam//2]
    else: #lista par
        return A[tam//2 -1] #pega o menor elemento entre os dois do meio 


def BubbleSort(A): #ordena uma lista de 5 elementos. Retorna mediana | (O(cst. * cst.))

    tam = len(A) #sempre sera 5, entao a complexidade dos fors sera tempo cst.
                 #so nao hard coded o numero 5 nos ranges pq temos ainda que fazer o bubble sort da particao 

    for i in range(0,tam):
        for j in range(0,tam):
            if(j+1 >= tam):
                break #lista esta ordenada
            elif(A[j] > A[j+1]):
                buf = A[j+1]
                A[j+1] = A[j]
                A[j] = buf

    #print("fim de bubble sort!",A)

    return A

def MOM(A,k): #Median Of Medians algorithm | O(n)

    resto = len(A) % 5 #se esse valor for diferente de zero, entao este valor deve ser o tamanho da ultima particao 
    mom_list = [] 
    i = 0
    while i < len(A):

        if(resto != 0 and i+5 >= len(A)): #ultima particao menor que 5 elementos 
            mom_list.append(BubbleFiveSort(A[i:i+resto]))    
            break #como sao os ultimos elementos, acabou a mediana das medianas

        mom_list.append(BubbleFiveSort(A[i:i+5])) #pega a mediana do primeiro grupo de 5

        i+=5

    #print("mom_list: ",mom_list)

    if(len(mom_list) <= 5):
        #print("retornando mediana das medianas...")
        return BubbleFiveSort(mom_list) #mediana das medianas
    else:
        return MOM(mom_list,k)


def LinearSelection(A,k):

    tam = len(A)
    if(tam == 1):
        return A[0]
    
    median = MOM(A,k)

    L = []
    R = []
    M = []

    for i in range(0,tam):

        if(A[i] == median):
            M.append(A[i])
        elif(A[i] < median): # se fosse menor ou igual, teriamos um algoritmo n²
            L.append(A[i])
        else:
            R.append(A[i])

    if(len(L) + len(M) >= k and len(L) < k):
        return median

    if(len(L) >= k):
        return LinearSelection(L,k)
    else:
        return LinearSelection(R, k - len(L) - len(M))

def SortSelection(A, k):
    Aord = BubbleSort(A)
    n = len(Aord)
    if k <= 0 or k > n:
        raise ValueError("k está fora dos limites da lista")
    return Aord[k-1]


def tarefa2():

    tam = randint(1000,10000)

    if(tam%2 == 1): #arredondando para baixo caso metade do k seja impar
        k = tam//2 -1
    else:
        k = tam//2

    lista_entrada = []
    
    lista_saida_linear = []
    lista_saida_sort = []

    for i in range(0,10):
        buf = []
        for j in range(0,tam):
            buf.append(randint(1,100000))
        lista_entrada.append(buf)

    for i in range(0,10):
        start = time()
        buf_linear = LinearSelection(lista_entrada[i],k)
        lista_saida_linear.append([buf_linear,time() - start])

        start = time()
        buf_sort = SortSelection(lista_entrada[i],k)
        lista_saida_sort.append([buf_sort,time() - start])

    # print(lista_saida_linear)
    # print(lista_saida_sort)

    for i in range(0,10): #verifica se os valores estao batendo
        if(lista_saida_linear[i][0] != lista_saida_sort[i][0]):
            raise Exception("valor ",i,"diferente entre Linear e Sort")


    #PLOTTING

    x_axis = []
    y_axis_linear = []
    y_axis_sort = []

    for i in range(0,10): #pega os eixos e os tempos
        x_axis.append(lista_saida_linear[i][0])
        y_axis_linear.append(lista_saida_linear[i][1])
        y_axis_sort.append(lista_saida_sort[i][1])

    dicio_linear = {'entrada': x_axis, 'tempo_saida': y_axis_linear}
    dicio_sort = {'entrada': x_axis, 'tempo_saida': y_axis_sort}

    df_linear = pd.DataFrame(dicio_linear)
    df_sort = pd.DataFrame(dicio_sort)


    ax = plt.subplots()
    ax = sns.barplot(x=df_sort["entrada"], y=df_sort["tempo_saida"], color='b', alpha=0.5)
    ax = sns.barplot(x=df_linear["entrada"], y=df_linear["tempo_saida"], color='r', alpha=0.5)

    ax.set(xlabel='Entrada', ylabel='Tempo de execução (s)')

    # ax = sns.barplot(x="entrada", y="tempo_saida", data=df_linear)
    # yx = sns.barplot(x="entrada", y="tempo_saida", data=df_sort)

    plt.show()


    return


def testing():

    A = [7,8,9,10,1,2,3,4,5,6] #no rep
    B = [1,4,5,5,7,9,8,10,2,4,10,10,] #w/ rep
    C = [1,2,3,4] #len < 5
    D = [3,3,3,3,3,3,3,3,3]# all rep
    test_list = [A,B,C,D]

    for i in range(0,len(test_list)):
        lista = test_list[i]
        k = (len(lista)//2)
        print("Lista", i, "sendo testada: ",lista)
        print("K elemento sendo procurado: ",k)
        print("valor de retorno LinearSelection: ",LinearSelection(lista,k))
        print("Valor de retorno SortSelection: ", SortSelection(lista,k))


# testing()
tarefa2()
