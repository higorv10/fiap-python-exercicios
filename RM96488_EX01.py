assinatura = input("Digite o tipo da sua assinatura: ")
fat_anual = int(input("Digite seu faturamento anual: "))
assinatura = assinatura.upper()

if assinatura == "BASIC":
    bonus = fat_anual * 0.3
    print("Você irá receber", bonus)
elif assinatura == "SILVER":
    bonus = fat_anual * 0.2
    print("Você irá receber", bonus)
elif assinatura == "GOLD":
    bonus = fat_anual * 0.1
    print("Você irá receber", bonus)
elif assinatura == "PLATINUM":
    bonus = fat_anual * 0.05
    print("Você irá receber", bonus)
else:
    print("Não entendi o tipo de assinatura.")