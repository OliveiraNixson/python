import itertools
import random
from time import sleep
import os

#criação das classes dos jogadores e maquinas

class Player:
    def __init__(self, balance=0):
        self.balance = balance


class CassaNiquel:

    def __init__(self,level =1,balance =0):
        self.SIMBOLOS ={
            'money_mouth_face':'1F911',
            'cold_face':'1F975',
            'alien':'1F47D',
            'heart_on_fire':'2764',
            'collision':'1F4A5'
        }
        self.level = level
        self.permutation = self.gen_permutation()
        self.balance = balance
        self.initial_balance = self.balance

    #Gerador de permutações dos emojis
    def gen_permutation(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(),repeat=3))
        for _ in range(self.level):
            for symbol in self.SIMBOLOS.keys():
                permutations.append((symbol,symbol,symbol))
        return permutations
    
    #Método para mostrar a jogada do jogador e gerar a lista de permutations
    def _get_final_result(self):
        if not hasattr(self,'permutations'):
            self.permutations = self.gen_permutation()
        result = list(random.choice(self.permutation))
        if len(set(result)) == 3 and random.randint(0,5)>=2:
            result[1] = result[0]
        return result
        
    #Output do programa para cada jogada
    def display(self,amount_bet,result,time=1):
        seconds = 2 
        for _ in range(0,int(seconds/time)):
            print(self.emojize(random.choice(self.permutation)))
            sleep(time)
            os.system('clear')
        print(self.emojize(result))


        if self.check_result_user(result):
            print(f'Você venceu e recebeu {amount_bet*3}')
        
        else:
            print('Foi quase, tente novamente')
            

        
    
    #Método para gerar os emojis
    def emojize(self,emojis):
        return ''.join(chr(int(self.SIMBOLOS[emoji],16)) for emoji in emojis)
        
    #Metodo para checagem do user
    def check_result_user(self,result):
        x = [result[0] == x for x in result]    
        return True if all(x) else False 

    
    #Faz atualização do caixa
    def update_balance(self,amount_bet,result, player:Player):
        if self.check_result_user(result):
            self.balance -= (amount_bet*3)
            player.balance += (amount_bet*3)
        else:
            self.balance += amount_bet
            player.balance -= (amount_bet)

    #Faz o jogo roda
    def play(self,amount_bet,player: Player):
        result = self._get_final_result()
       # self.display(amount_bet,result,time)
        self.update_balance(amount_bet,result,player)

                
        



player1 = Player()
maquina1 = CassaNiquel(level=4,balance=40)
maquina1.play(10,player1)
    
