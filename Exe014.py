print("<<BOLETIM ESCOLAR>>")

AV1 = float(input("Digite a nota AV1: "))
AV2 = float(input("Digite a nota AV2: "))
print("-----------------------------------------------------")
print("A avaliação N1(",AV1,")+ avaliação N2(",AV2,")o resultado é:",(AV1+AV2))
print("Média final:",(AV1+AV2)/2)
print("-----------------------------------------------------")
media = float(input("Qual é a média final: "))
if media >=5.0:
    print("<O aluno obteve a nota acima de 5.0: Aprovado")
else:
    print("O aluno obteve a nota abaixo de 5.0: Reprovado")
print("-----------------------------------------------------")
print("Boas Férias")