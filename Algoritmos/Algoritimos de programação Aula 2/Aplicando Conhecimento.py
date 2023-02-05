import math
Custo = float(input())
Preco = float(input())
Min = (Custo / Preco)
Lucro = Custo * 0.23
Qtd_lucro = (Custo + Lucro) / Preco

rounded_Lucro = math.ceil(Min)
rounded_Qtd_lucro = math.ceil(Qtd_lucro)
print( rounded_Lucro)
print( rounded_Qtd_lucro)