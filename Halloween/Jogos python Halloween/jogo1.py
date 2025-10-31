import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100...")
    print("Você tem 10 tentativas para acertar!")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    while tentativas < max_tentativas:
        try:
            palpite = int(input(f"Tentativa {tentativas + 1}/{max_tentativas} - Digite seu palpite: "))
        except ValueError:
            print(" Por favor, digite um número válido.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break
    else:
        # Esse "else" pertence ao while — executa se o jogador não acertar a tempo
        print(f"Suas {max_tentativas} tentativas acabaram! O número era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()