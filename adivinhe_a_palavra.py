import random
from palavras_para_adivinhar import palavras
from estagios_forca import estagios, logo

vidas = 6

print(logo, sep=None)

escolha_da_palavra = random.choice(palavras)

campo = ""
for posicao in range(len(escolha_da_palavra)):
    campo += "_"
print(f"Palavra a ser adivinhada: {campo}")

fim_de_jogo = False
escolhas_certas = []
while not fim_de_jogo:
    print(f"******************** Você tem {vidas}/6 vidas restantes ********************")
    jogada = input("\nEscolha uma letra: ").lower()

    if jogada in escolhas_certas:
        print(f"Você já escolheu a letra: {jogada}")

    display = ""

    for letra in escolha_da_palavra:
        if letra == jogada:
            display += jogada
            escolhas_certas.append(letra)
        elif letra in escolhas_certas:
            display += letra
        else:
            display += "_"

    print(f"Palavra a ser adivinhada: " + display)

    if jogada not in escolha_da_palavra:
        vidas -= 1
        print(f"Você já escolheu a letra: {jogada}, ela nao aparece na palavra. Você perdeu uma vida.")
        if vidas == 0:
            fim_de_jogo = True
            print(f"******************** A palavra era: {escolha_da_palavra} - Você perdeu! ********************")

    if "_" not in display:
        fim_de_jogo = True
        print("******************** Parabéns, você ganhou!********************")

    print(estagios[vidas])