import math

Custo = float(input())
Preco = float(input())

Min = (Custo / Preco)
Lucro = Custo * 0.23
Qtd_lucro = (Custo + Lucro) / Preco

Arredonda_Lucro = math.ceil(Min)
Arredonda_Qtd_lucro = math.ceil(Qtd_lucro)

print( Arredonda_Lucro)
print( Arredonda_Qtd_lucro)