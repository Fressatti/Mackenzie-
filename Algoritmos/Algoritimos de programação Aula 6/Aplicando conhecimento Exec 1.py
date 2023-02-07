num = int(input())
while num < 0 or num > 10:
    print("VALOR INVÁLIDO")
    num = int(input())
for i in range (1, 11, 1):
    resultado = num * i
    print(f"{num}x{i}={resultado}") 