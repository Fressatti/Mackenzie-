num_alunos = int(input())

if num_alunos == 0:
    print("NÃO HOUVE PROCESSAMENTO")
else:
    soma = 0
    for i in range(num_alunos):
        media = float(input(""))
        soma += media
        if media >= 6.0:
            print("PARABÉNS VOCÊ ESTÁ APROVADO")
    media_geral = soma / num_alunos
    print(media_geral)