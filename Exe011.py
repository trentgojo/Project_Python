print("<<Teste de Nomes>>")
print("-="*20)

#DADOS
nome = "SATORU"
sobrenome_pai = "GOJO"
sobrenome_mae = "YUGI"
inicias = nome[0] + sobrenome_mae[0] + sobrenome_mae[0]
empresa = "JUJUTSU"

#RESOLUÇÃO
print("<<DADOS>>")
print("Nome do usuário:"+nome+""+sobrenome_pai+sobrenome_mae)
print("Quais sao as inicias: "+inicias)
print("Nome da empresa:",empresa)
print("-="*25)

#RODANDO APLICACAO
print(">>>INICIO")
print("O nome completo é:",nome,"",sobrenome_pai,"",sobrenome_mae,",e as inicais sao:",inicias)
print("Criando o email:"+nome+"."+sobrenome_pai+"@"+empresa+".com")
print("-="*25)

input("Clique para sair")