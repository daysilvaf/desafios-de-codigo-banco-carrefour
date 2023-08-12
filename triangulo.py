DESAFIO
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo 
(soma de todos os lados) e apresente a mensagem:
Perimetro = XX.X
Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:
Area = XX.X
Fórmula da área de um trapézio: AREA = ((A + B) x C) / 2

ENTRADA
A entrada contém três valores reais.

SAÍDA
O resultado deve ser apresentado com uma casa decimal.

-----------------------------------------
| EXEMPLO DE ENTRADA | EXEMPLO DE SAÍDA |
-----------------------------------------
|     6.0 4.0 2.0    |    Area = 10.0   |
-----------------------------------------
|     6.0 4.0 2.1    | Perimetro = 12.1 |
-----------------------------------------

CÓDIGO

lados = [float(x) for x in input().split()]

a = lados[0]
b = lados[1]
c = lados[2]

if a + b > c and a + c > b and b + c > a:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
