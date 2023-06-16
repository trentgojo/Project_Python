print("Teste de Nomes!!!!!!! ")

nome = "Thiago"
sobrenome_mae = "Carvalho"
sobrenome_pai = "Porto"
iniciais = nome[0] + sobrenome_mae[0] + sobrenome_pai[0]
empresa = "ikross"

print("---------------------------------------------------------------------")
print(">>>INICIO")
print("<<<Informações>>>")
print("Nome do usuário:",nome, sobrenome_pai, sobrenome_mae)
print("Quais são minhas iniciais:",iniciais)
print("Nome da empresa:",empresa)
print("---------------------------------------------------------------------")


print("<<<Resultado:>>>" )

print(nome+" "+sobrenome_mae+" "+sobrenome_pai)
print("Meu nome completo é " +nome+ " " +sobrenome_mae + " " +sobrenome_pai + " e minhas iniciais são"+ " " +iniciais+".")
print("Criando o Email: "+nome+"."+sobrenome_pai+"@"+empresa+".com" )
print("---------------------------------------------------------------------")
print("Procurando letras especificas: ")
print(nome[1],sobrenome_pai[4],sobrenome_mae[5])
print(nome[4],sobrenome_mae[3],sobrenome_pai[3])
print(sobrenome_pai[4],sobrenome_mae[2],nome[1])
print("---------------------------------------------------------------------")
print(">>>FIM")