print("Média do aluno")
print("---------------------------------------------------")

peso1 = float(input("Digite o peso da primeira avaliação: "))
peso2 = float(input("Digite o peso da segunda avaliação: "))
AV1 = float(input("Digite a nota da primeira AV1: "))
AV2 = float(input("Digite a nota da segunda AV2: "))

media = ((peso1*AV1) + (peso2*AV2) / (peso1+peso2))
print("---------------------------------------------------")
print("A media do aluno é:" ,media)
print("---------------------------------------------------")

resultado = float(input("Média Final: "))
if resultado >= 5.0:
    print("A aluno obteve a nota acima de 5.0: APROVADO")
else:
    print("O aluno obteve a note abaixo de 5.0: REPROVADO")

print("Boas Férias")
print("---------------------------------------------------")
input("Aperte enter para sair")
