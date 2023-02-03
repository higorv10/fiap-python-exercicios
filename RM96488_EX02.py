votos_segunda = int(input("Digite a quantidade de votos que segunda-feira obteve: "))
votos_terça = int(input("Digite a quantidade de votos que terça-feira obteve: "))
votos_quarta = int(input("Digite a quantidade de votos que quarta-feira obteve: "))
votos_quinta = int(input("Digite a quantidade de votos que quinta-feira obteve: "))
votos_sexta = int(input("Digite a quantidade de votos que sexta-feira obteve: "))

if votos_segunda > votos_terça and votos_segunda > votos_quarta and votos_segunda > votos_quinta and votos_segunda > votos_sexta:
    print("O dia escolhido foi segunda-feira ")
elif votos_terça > votos_segunda and votos_terça > votos_quarta and votos_terça > votos_quinta and votos_terça > votos_sexta:
    print("O dia escolhido foi terça-feira ")
elif votos_quarta > votos_segunda and votos_quarta > votos_terça and votos_quarta > votos_quinta and votos_quarta > votos_sexta:
    print("O dia escolhido foi quarta-feira ")
elif votos_quinta > votos_segunda and votos_quinta > votos_terça and votos_quinta > votos_quarta and votos_quinta > votos_sexta:
    print("O dia escolhido foi quinta-feira ")
elif votos_sexta > votos_segunda and votos_sexta > votos_terça and votos_sexta > votos_quarta and votos_sexta > votos_quinta:
    print("O dia escolhido foi sexta-feira ")
elif votos_segunda == votos_terça == votos_quarta == votos_quinta == votos_sexta:
    print("Todos os dias da semana obtiveram a mesma quantidade de votos ")
else:
    print("Dois ou mais dias receberam a maior, e mesma,  quantidade de votos")





