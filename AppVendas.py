print("Bem Vindo a Lanchonete do Higor Vilela")

print("Código     Descrição               Valor")

print("100        Cachorro-Quente         R$9,00")

print("101        Cachorro-Quente Duplo   R$11,00")

print("102        X_Egg                   R$12,00")

print("103        X-Salada                R$13,00")

print("104        X-Bacon                 R$14,00")

print("105        X-Tudo                  R$17,00")

print("200        Refrigerante Lata       R$5,00")

print("201        Chá Gelado              R$4,00")

pedindo = True

codigo = 0

resposta = ""

total = 0

vefCodigo = True

while pedindo == True:

   while vefCodigo == True:

       codigo = input(": ")

       if codigo == '100':

           print("100 - Cachorro-Quente - R$9,00")

           total = total + 9

           vefCodigo = False

       elif codigo == '101':

           print("101 - Cachorro-Quente Duplo - R$11,00")

           total = total + 11

           vefCodigo = False

       elif codigo == '102':

           print("101 - X-Egg - R$12,00")

           total = total + 12

           vefCodigo = False

       elif codigo == '103':

           print("101 - X-Salada - R$13,00")

           total = total + 13

           vefCodigo = False

       elif codigo == '104':

           print("101 - X-Bacon - R$14,00")

           total = total + 14

           vefCodigo = False

       elif codigo == '105':

           print("101 - X-Tudo - R$17,00")

           total = total + 17

           vefCodigo = False

       elif codigo == '200':

           print("101 - Refrigerante Lata - R$5,00")

           total = total + 5

           vefCodigo = False

       elif codigo == '201':

           print("101 - Chá Gelado - R$4,00")

           total = total + 4

           vefCodigo = False

       else:

           print("Opção Inválida!")

   resposta = input("Continuar pedindo? Sim ou Não? ")

   if resposta == "sim" or resposta == "Sim" or resposta == "s" or resposta == "S":

       vefCodigo = True

       print("Valor total: R$",total)

   else:

       pedindo = False

print("Valor total: R$",total)