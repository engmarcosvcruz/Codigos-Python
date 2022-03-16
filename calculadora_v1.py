# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print("Python Calculator")
print("Escolha uma Seleção")

def soma (x,y):
    return x + y

def subtraçao(x,y):
    return x - y

def multiplcaçao(x,y):
    return x * y

def divisao(x,y):
    return x / y

print ("1- Soma")
print ("2- Subtração")
print ("3- Multiplicação")
print ("4- Divisao")

operaçao = int (input('Faça a sua escolha(1/2/3/4/'))
x =  int (input('Digite o Primeiro Numero'))
y =  int (input('Digite o Segundo Numero'))


if operaçao == 1: 
    soma = x + y
    print(soma)

if operaçao == 2:
    subtraçao =  x - y
    print(subtraçao)

if operaçao == 3:
    multiplcaçao = x * y
    print(multiplcaçao)
    
if operaçao == 4:
    divisao = x / y
    print(divisao)

