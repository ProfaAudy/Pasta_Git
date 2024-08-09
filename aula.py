#Exemplo de exercício
#Enunciado: Faça um programa que receba o código do estado de origem da carga de um cami nhão, o peso da carga em toneladas e o código dela. 
#Calcule e apresente: o peso da carga em quilos, o preço da carga, o valor do imposto e o valor total da carga (preço da carga mais imposto).

# Tabela de Códigos e Cargos
# +--------+-------+
# | Código | Cargo |
# +--------+-------+
# |   1    |  20   |
# |   2    |  15   |
# |   3    |  10   |
# |   4    |   5   |
# +--------+-------+

# Tabela de Preços por Quilo
# +----------------+----------------+
# | Código da carga | Preço por quilo|
# +----------------+----------------+
# |     10 a 20    |      180       |
# |     21 a 30    |      120       |
# |     31 a 40    |      230       |
# +----------------+----------------+

# Recebendo os dados de entrada
codigo_estado = int(input("Digite o código do estado de origem da carga: "))
peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga: "))

# Convertendo o peso de toneladas para quilos
peso_quilos = peso_toneladas * 1000

# Determinando o preço por quilo com base no código da carga
if 10 <= codigo_carga <= 20:
    preco_quilo = 180
elif 21 <= codigo_carga <= 30:
    preco_quilo = 120
elif 31 <= codigo_carga <= 40:
    preco_quilo = 230
else:
    print("Código de carga inválido.")
    preco_quilo = 0

# Calculando o preço da carga
preco_carga = peso_quilos * preco_quilo

# Determinando o valor do imposto com base no código do estado
if codigo_estado == 1:
    imposto = 0.20
elif codigo_estado == 2:
    imposto = 0.15
elif codigo_estado == 3:
    imposto = 0.10
elif codigo_estado == 4:
    imposto = 0.05
else:
    print("Código de estado inválido.")
    imposto = 0

# Calculando o valor do imposto
valor_imposto = preco_carga * imposto

# Calculando o valor total da carga
valor_total = preco_carga + valor_imposto

# Exibindo os resultados
print(f"Peso da carga em quilos: {peso_quilos:.2f} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Valor total da carga: R$ {valor_total:.2f}")