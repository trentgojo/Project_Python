print("<<BOLETIM ESCOLAR>>")

num1 = float(input("Digite a nota N1: "))
num2 = float(input("Digite a nota N2: "))
print("-----------------------------------------------------")
print("A avaliação N1(",num1,")+ avaliação N2(",num2,")o resultado é:",(num1+num2))
print("Média final:",(num1+num2)/2)
print("-----------------------------------------------------")
media = float(input("Qual é a média final: "))
if media >=5.0:
    print("<O aluno obteve a nota acima do 5.0: Aprovado")
else:
    print("O aluno obteve a nota abaixo do 5.0: Reprovado")
print("-----------------------------------------------------")
print("Bons estudos")