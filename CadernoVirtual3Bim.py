#Laço for  - laço de repetição
x = 10
for i in range(x):
    print (i)
#if_else
#>
#<
#==
#!=
#>=
#<=
print("Else If")
x = 50
y = 10
if x > y:
    print("Verdadeiro") #Executa se verdadeiro/sim/positivo
elif x < y: #else if
    print("V2")
else:
    #else continuação da estrutura
    print("Falso")
#Prova Paulista
print("Simulação Prova Paulista")
temperatura = 20
if temperatura == 5:
    resposta = "Coloque um casaco"
elif temperatura == 10:
    resposta = "Coloque um casaco está moderadamente frio"
elif temperatura == 20:
    resposta = "Coloque um casaco está frio"
elif temperatura == 22:
    resposta = "Leva um casaco por precaução"
else:
    resposta = "Leve um casaco, está agradável"
print(resposta)

temperatura = int(input("Insira um número!"))
match temperatura:
    case 5:
        resposta = "Coloque um casaco"
    case 10:
        resposta = "Coloque um casaco está moderadamente frio"
    case _:
        resposta = "Leve um casaco, está agradável"
print(resposta)
