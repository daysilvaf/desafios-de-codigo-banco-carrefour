DESAFIO
Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada 
posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 
1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

ENTRADA
A entrada contém um valor inteiro (V<=50).

SAÍDA
Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro 
número do vetor N (N[0]) irá receber o valor de V.

-----------------------------------------
| EXEMPLO DE ENTRADA | EXEMPLO DE SAÍDA |
-----------------------------------------
|          1         |     N[0] = 1     |
|                    |     N[1] = 2     |
|                    |     N[2] = 4     |
|                    |        ...       |
-----------------------------------------

CÓDIGO

x = int(input())
n = []

for i in range(10):
    n.append(x)
    x *= 2
    print("N[{}] = {}".format(i, n[i]))
