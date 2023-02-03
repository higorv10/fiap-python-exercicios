n = int(input("Digite o minuto atual: "))
c = n
f = 1
print("{}! = ".format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}, A SUA SENHA É LIBERDADE{}'.format(f, f))
5