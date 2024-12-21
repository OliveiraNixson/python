import random 

def mostrar_titulo():
        print("Bem vindo ao Fibula RPG!")

def iniciar_jogo():
        nome = input ('Qual o seu nome?')
        hp = 100
        level = 1
        strength = 3 
        exp = 0 
        inventory = []
        status = True #Vivo ou Morto
        
        return nome,hp,level,strength,exp,inventory,status



def sortear_monstro(jogador_lv):
        #Lista dos monstros:[nome,hp,força,exp]
        slime = ["Slime",10,2,10]
        goblin = ["goblin", 20, 4, 20]
        troll = ["troll", 40, 8, 40]
        orc = ["orc", 80, 16, 80]
        mumia = ["múmia", 160, 32, 160]
        quimera = ["quimera", 320, 64, 320]
        dragao = ["dragão", 1000, 100, 1000]

        #Calcula o level do monstro baseado no level do jogador
        if jogador_lv < 5:
            monstro_sorteado = random.choice([slime,goblin,troll])
        elif jogador_lv < 10:
            monstro_sorteado = random.choice([orc,mumia,quimera])
        else:
            monstro_sorteado = dragao 

        #Sorteia um monstro com base no level do jogador
        
        return monstro_sorteado

def game_over():
        print("O jogo acabou.")
        print("Obrigado por jogar!")
        #Função para interromper o jogo
        exit(0)

        


def atacar(atacante_nome,atacante_forca,defensor_nome,defensor_hp, defensor_forca):
        atacante_sorte = random.randint(0,6)
        defensor_sorte = random.randint(0,6)
        if atacante_sorte == 6:
            print(f"O {atacante_nome} acertou um ataque critico!")
        elif atacante_sorte == 0:
            print(f"O {atacante_nome} acertou um ataque!")
        else:
        #print(f")-> Uma string melhorada
            print(f"O {atacante_nome} errou o golpe")

        dano = max(0,(atacante_forca*atacante_sorte)/10 - (defensor_forca*defensor_sorte)/10)
        if dano > 0:
            print(f"O {defensor_nome} sofreu um dano de {dano}")
            defensor_hp -= dano
        else:
            print(f"O {defensor_nome} não sofreu dano.")
        if defensor_hp <= 0:
            print(f"{defensor_nome} foi derrotado!")
            return 0
        else:
            return defensor_hp
        

def calcular_level(jogador_level,jogador_exp,jogador_hp,jogador_forca,exp_monstro):
        jogador_exp += exp_monstro
        exp_necessaria = 3**jogador_level
        if jogador_exp >= exp_necessaria:
            jogador_level += 1
            jogador_hp = 100
            jogador_forca = jogador_forca*2
    
        return jogador_level,jogador_exp,jogador_hp,jogador_forca


def obter_pocao():
    #Função para pegar uma pocao de cura
    chance = random.random()
    if chance <= 0.2:
            print("Voce encontrou uma pocao de cura!")
            return "Poção"
    else:
            return None

def usar_item(jogador_inventario,jogador_hp):
        if not jogador_inventario:
            #Entro aqui caso esteja vazia a lista
            print("Você não possui itens.")
        else:
            print("Inventario:")
            for index,item in enumerate(jogador_inventario):
                print(f"{index+1}. {item}")
            opcao_item = int(input("Escolha o item ou 0 para cancelar"))
        if opcao_item ==0:
            print("\n")
        else:
            item_escolhido = jogador_inventario[opcao_item -1]
            if item_escolhido =="Poçao":
                print("Você usou uma poção!")
                jogador_hp += 20
                if jogador_hp > 100:
                    jogador_hp = 100
                    print(f"Seuu hp é{jogador_hp}.")
                    jogador_inventario.pop(opcao_item-1)
            else:
                print("Item invalido!\n")

                
def fugir(jogador_nome):
    sucesso = random.choice([True,False])
    if sucesso:
        print(f"{jogador_nome} escapou!")
        return True
    else:
        print(f"{jogador_nome} não escapou!")
        return False
    
                
              

            
        




#Aqui o jogo será executado
def main():
    mostrar_titulo()
    nome_jogador,jogador_hp,jogador_level,jogador_forca,jogador_exp,jogador_inventario, status = iniciar_jogo()
    print("\n")

    jogador_enfrentando_monstro = False

    while True:
        if not jogador_enfrentando_monstro:
        
                monstro_nome,monstro_hp,monstro_forca,exp_monstro = sortear_monstro(jogador_level)
                print(f"/n Um {monstro_nome} aleatorio apareceu!")
                print(f"HP: {jogador_hp}\n")
        else:
            print(f"n/ Voce está enfrentando o {monstro_nome}!")
            print(f"HP: {jogador_hp}, HP do monstro: {monstro_hp}\n")
            opcao = int(input("1) Atacar\n2) Usar item\n3) Fugir\n"))
            opcao = int(input())
            if opcao == 1:
                monstro_hp = atacar(monstro_nome,monstro_forca,nome_jogador,jogador_hp,jogador_forca)
                print('\n')
                if jogador_hp==0:
                    game_over()
                else:
                    print(f"Você ganhou {exp_monstro} XP!")
                    jogador_level, jogador_exp,jogador_hp, jogador_forca = calcular_level(jogador_level,jogador_exp,jogador_hp,jogador_forca,exp_monstro)
                    pocao = obter_pocao()
                if pocao is not None:
                    jogador_inventario.append(opcao)
                jogador_enfrentando_monstro = False
            elif opcao ==2:
                jogador_hp,jogador_inventario = usar_item(jogador_inventario,jogador_hp)

            elif opcao == 3:
                if fugir(nome_jogador):
                  jogador_enfrentando_monstro = False

                else:
                    jogador_hp = atacar(nome_jogador,monstro_nome,monstro_hp, jogador_hp)
                    print("\n")
                    if jogador_hp == 0:
                        game_over()
            elif opcao == 4:
                print(f"\n{nome_jogador}")
                print(f"HP: {jogador_hp}")
                print(f"Level:{jogador_level}")
                print(f"Exp:{jogador_exp}")
                exp_proximo_nivel = 3 **jogador_level
                print(f"Falta {exp_proximo_nivel - jogador_exp}")
                print(f"{jogador_forca}")
                print(f"Inventario:{jogador_inventario}")

if __name__ == "__main__":
    main()


