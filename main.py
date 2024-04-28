'''
Alunos: 
    Guilherme A. Ponce (2011179)
    João Victor Godinho W. (2011401)

'''

#Encontrar o K-esimo maior elemento da lista

from random import randint

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

    print("fim de bubble sort!",A)

    if(tam%2 != 0): #lista impar
        return A[tam//2]
    else: #lista par
        return A[tam//2 -1] #pega o menor elemento entre os dois do meio 


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

    print("mom_list: ",mom_list)

    if(len(mom_list) <= 5):
        print("retornando mediana das medianas...")
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


def testing():

    A = [7,8,9,10,1,2,3,4,5,6,] #no rep
    B = [1,4,5,5,7,9,8,10,2,4,10,10,] #w/ rep
    C = [1,2,3,4] #len < 5
    D = [3,3,3,3,3,3,3,3,3]# all rep
    test_list = [A,B,C,D]

    for i in range(0,len(test_list)):
        lista = test_list[i]
        k = randint(1,len(lista))
        print(i,"Lista sendo testada: ",lista)
        print("K elemento sendo procurado: ",k)
        print("valor de retorno: ",LinearSelection(lista,k))
    return

testing()