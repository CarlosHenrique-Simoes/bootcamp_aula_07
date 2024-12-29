import random

palavras = ["carro", "moto", "bicicleta", "fogão", "geladeira", "microondas"]

escolha_da_palavra = random.choice(palavras)

campo = ""
for posicao in range(len(escolha_da_palavra)):
    campo += "_"
print(campo)

fim_de_jogo = False
escolhas_certas = []
while not fim_de_jogo:
    jogada = input("\nEscolha uma letra: ").lower()

    display = ""

    for letra in escolha_da_palavra:
        if letra == jogada:
            display += jogada
            escolhas_certas.append(letra)
        elif letra in escolhas_certas:
            display += letra
        else:
            display += "_"

    print(display)

    if "_" not in display:
        fim_de_jogo = True
        print("Parabéns, você ganhou!")