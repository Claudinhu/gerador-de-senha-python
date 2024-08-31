import random
import string

def gerador_senha (len_pass = 8):
    ascii_opcoes = string.ascii_letters
    numero_opcoes = string.digits
    ponto_opcoes = string.punctuation
    opcoes = ascii_opcoes + numero_opcoes + ponto_opcoes

    senha_usuario = ""
    
    for i in range(0, len_pass):
        digit = random.choice(opcoes)
        senha_usuario = senha_usuario + digit

    return senha_usuario

escolha_usuario = input("Quantos digitos na senha ?")

if escolha_usuario.isdigit():
    escolha_usuario = int(escolha_usuario)
else:
    print("Entrada Invalida!")
    quit()

resposta = gerador_senha(len_pass = escolha_usuario)
print(f"Senha Gerada meu chefe :): \n{resposta}")