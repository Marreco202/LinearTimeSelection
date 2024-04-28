'''
Alunos: 
    Guilherme A. Ponce (inserir matricula)
    João Victor Godinho W. (2011401)

'''

#Encontrar o K-esimo maior elemento da lista

A = [1,2,3,4,5,6,7,8,9,10] #no rep
B = [1,2,4,4,5,5,7,8,9,10] #w/ rep

def BubbleFiveSort(A): #ordena uma lista de 5 elementos. Retorna mediana | (O(cst. * cst.))

    tam = len(A) #sempre sera 5, entao a complexicdade dos fors sera tempo cst.
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
        return A[int((tam-1)/2)]
    else: #lista par
        return A[int((tam-1)/2 - 0.5)] #pega o menor elemento entre os dois do meio 




def MOM(A,k): #Median Of Medians algorithm | O(n)

    resto = len(A) % 5 #se esse valor for diferente de zero, entao este valor deve ser o tamanho da ultima particao 
    mom_list = [] 

    while i < len(A):

        if(resto != 0 and i+5 >= len(A)): #ultima particao menor que 5 elementos 
            mom_list.append(BubbleFiveSort(A[i:i+resto]))    
            break #como sao os ultimos elementos, acabou a mediana das medianas

        mom_list.append(BubbleFiveSort(A[i:i+5])) #pega a mediana do primeiro grupo de 5

        i+=5

    if(len(mom_list) <= 5):
        return BubbleFiveSort(mom_list) #mediana das medianas
    else:
        return MOM(mom_list,k)


def LinearSelection(A,k):

    tam = len(A)
    if(tam == 1):
        return A
    
    median = MOM(A,k)

    L = []
    R = []

    for i in range(i,tam):
        if(A[i] < median): # se fosse menor ou igual, teriamos um algoritmo n²
            L.append(A[i])
        else:
            R.append(A[i])

    if(len(L)<= k-1):
        return median

    if(len(L) > k-1):
        LinearSelection(L,k)
    else:
        LinearSelection(R, k - len(L) - 1)



BubbleFiveSort([1,1,5,4,3])
