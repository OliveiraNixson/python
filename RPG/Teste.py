import random

def mostrar_titulo():
    print("Bem vindo ao Fibula RPG!")

def iniciar_jogo():
    nome = input('Qual o seu nome? ')
    hp = 100
    level = 1
    strength = 3
    exp = 0
    inventory = []
    status = True  # Vivo ou Morto

    return nome, hp, level, strength, exp, inventory, status

def sortear_monstro(jogador_lv):
    slime = ["Slime", 10, 2, 10]
    goblin = ["Goblin", 20, 4, 20]
    troll = ["Troll", 40, 8, 40]
    orc = ["Orc", 80, 16, 80]
    mumia = ["Múmia", 160, 32, 160]
    quimera = ["Quimera", 320, 64, 320]
    dragao = ["Dragão", 1000, 100, 1000]

    if jogador_lv < 5:
        monstro_sorteado = random.choice([slime, goblin, troll])
    elif jogador_lv < 10:
        monstro_sorteado = random.choice([orc, mumia, quimera])
    else:
        monstro_sorteado = dragao

    return monstro_sorteado

def game_over():
    print("O jogo acabou.")
    print("Obrigado por jogar!")
    exit(0)

def atacar(atacante_nome, atacante_forca, defensor_nome, defensor_hp, defensor_forca):
    atacante_sorte = random.randint(0, 6)
    defensor_sorte = random.randint(0, 6)
    if atacante_sorte == 6:
        print(f"O {atacante_nome} acertou um ataque crítico!")
    elif atacante_sorte == 0:
        print(f"O {atacante_nome} acertou um ataque!")
    else:
        print(f"O {atacante_nome} errou o golpe.")

    dano = max(0, (atacante_forca * atacante_sorte) / 10 - (defensor_forca * defensor_sorte) / 10)
    if dano > 0:
        print(f"O {defensor_nome} sofreu um dano de {dano:.2f}")
        defensor_hp -= dano
    else:
        print(f"O {defensor_nome} não sofreu dano.")
    
    if defensor_hp <= 0:
        print(f"{defensor_nome} foi derrotado!")
        return 0
    else:
        return defensor_hp

def calcular_level(jogador_level, jogador_exp, jogador_hp, jogador_forca, exp_monstro):
    jogador_exp += exp_monstro
    exp_necessaria = 3 ** jogador_level
    if jogador_exp >= exp_necessaria:
        jogador_level += 1
        jogador_hp = 100
        jogador_forca *= 2

    return jogador_level, jogador_exp, jogador_hp, jogador_forca

def obter_pocao():
    chance = random.random()
    if chance <= 0.2:
        print("Você encontrou uma poção de cura!")
        return "Poção"
    else:
        return None

def usar_item(jogador_inventario, jogador_hp):
    if not jogador_inventario:
        print("Você não possui itens.")
    else:
        print("Inventário:")
        for index, item in enumerate(jogador_inventario):
            print(f"{index + 1}. {item}")
        opcao_item = int(input("Escolha o item ou 0 para cancelar: "))
        if opcao_item == 0:
            print("\n")
        else:
            item_escolhido = jogador_inventario[opcao_item - 1]
            if item_escolhido == "Poção":
                print("Você usou uma poção!")
                jogador_hp += 20
                if jogador_hp > 100:
                    jogador_hp = 100
                print(f"Seu HP é {jogador_hp}.")
                jogador_inventario.pop(opcao_item - 1)
            else:
                print("Item inválido!\n")
    return jogador_hp, jogador_inventario

def fugir(jogador_nome):
    sucesso = random.choice([True, False])
    if sucesso:
        print(f"{jogador_nome} escapou!")
        return True
    else:
        print(f"{jogador_nome} não escapou!")
        return False

def main():
    mostrar_titulo()
    nome_jogador, jogador_hp, jogador_level, jogador_forca, jogador_exp, jogador_inventario, status = iniciar_jogo()

    jogador_enfrentando_monstro = False

    while True:
        if not jogador_enfrentando_monstro:
            monstro_nome, monstro_hp, monstro_forca, exp_monstro = sortear_monstro(jogador_level)
            print(f"\nUm {monstro_nome} aleatório apareceu!")
            print(f"HP: {jogador_hp}\n")
            jogador_enfrentando_monstro = True
        else:
            print(f"\nVocê está enfrentando o {monstro_nome}!")
            print(f"HP: {jogador_hp}, HP do monstro: {monstro_hp}\n")
            opcao = int(input("1) Atacar\n2) Usar item\n3) Fugir\n"))
            if opcao == 1:
                monstro_hp = atacar(monstro_nome, monstro_forca, nome_jogador, jogador_hp, jogador_forca)
                if jogador_hp == 0:
                    game_over()
                else:
                    print(f"Você ganhou {exp_monstro} XP!")
                    jogador_level, jogador_exp, jogador_hp, jogador_forca = calcular_level(jogador_level, jogador_exp, jogador_hp, jogador_forca, exp_monstro)
                    pocao = obter_pocao()
                    if pocao is not None:
                        jogador_inventario.append(pocao)
                    jogador_enfrentando_monstro = False
            elif opcao == 2:
                jogador_hp, jogador_inventario = usar_item(jogador_inventario, jogador_hp)
            elif opcao == 3:
                if fugir(nome_jogador):
                    jogador_enfrentando_monstro = False
                else:
                    jogador_hp = atacar(nome_jogador, monstro_nome, monstro_hp, jogador_hp, jogador_forca)
                    if jogador_hp == 0:
                        game_over()
            else:
                print("Opção inválida!")
                
            if jogador_hp == 0:
                game_over()

if __name__ == "__main__":
    main()
