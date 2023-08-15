DESAFIO
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

ENTRADA
O arquivo de entrada contém 1 valor inteiro qualquer.

SAÍDA 
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

-----------------------------------------
| EXEMPLO DE ENTRADA | EXEMPLO DE SAÍDA | 
-----------------------------------------
|          8         |         1        |
|                    |         3        |
|                    |         5        |
|                    |         7        |
-----------------------------------------

CÓDIGO

X = int(input())

for i in range(1, X + 1, 2):
    print(i)
