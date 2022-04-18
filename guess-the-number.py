import random
import os

while True:
    #Sistema de contagem de players
    while True:
        try:
            players = input('Olá, antes de começarmos, me diga quantos jogadores irão jogar (OBS: Máximo de 5 jogadores) :: ')
            players = int(players)
            
            if players <= 5 and players >=2:
                print('OK! ' + str(players) + ' jogadores irão participar!')
                break

            elif players == 1:
                print('OK! ' + str(players) + ' jogador irá participar!')
                break

            elif players <= 0:
                print('Então, possuímos um necessidade mínima de 1 jogador!')

            else:
                print('Então, possuímos uma capacidade máxima de 5 jogadores!')

        except:
            print('Então, apenas números podem ser digitados nesse jogo!')

    repeat = 0
    saves = []

    #Sistema de armazenamento de nomes
    while repeat < players:
        repeat += 1
        name = input('\nOlá, Jogador número ' + str(repeat) + ', informe seu nome :: ')
        print('Seja bem-vindo(a) ' + name + '!')
        saves.append([name, repeat])

    #Gestão de números máximos e mínimos
    while True: #Mínimo
        try:
            minimum = input('\nAgora nos diga qual será o menor número da partida :: ')
            minimum = int(minimum)
            if minimum >= 0:
                print('OK! O menor número possível é o ' + str(minimum) + '!')
                break

            else:
                print('Então, não aceitamos números negativos!')

        except:
            print('Então, apenas números podem ser digitados nesse jogo!')

    while True: #Máximo
        try:
            maximum = input('\nAgora nos diga qual será o maior número da partida :: ')
            maximum = int(maximum)

            if maximum <= minimum:
                print('Então, o maior número não pode ser menor ou igual ao menor número!')

            elif maximum < minimum + 15:
                print('Então, o maior número tem que ser pelo menos 15 unidades maior que o menor número!')

            else:
                print('OK! O maior número possível é o ' + str(maximum) + '!')
                break

        except ValueError:
            print('Então, apenas números podem ser digitados nesse jogo!')

    repeat = 0

    #Criação do jogo
    while repeat < players:
        repeat += 1
        attempts = 0
        number = random.randint(minimum, maximum)
        
        while True:
            try:
                player_number = input('\n' + saves[repeat - 1][0] + ' digite um valor entre (' + str(minimum) + ' - ' + str(maximum) + ') :: ')
                player_number = int(player_number)
                attempts += 1

                if number == player_number:
                    input('Parabéns ' + saves[repeat - 1][0] + '! Você acertou o número em ' + str(attempts) + ' tentativas! Aperte ENTER para o próximo jogador!')
                    saves[repeat - 1].append(attempts)
                    os.system('cls')
                    break
                
                elif player_number < minimum:
                    print('Então, você digitou um valor menor que o intervalo possível!\n')

                elif player_number > maximum:
                    print('Então, você digitou um valor maior que o intervalo possível!\n')

                elif player_number < number:
                    print('Que pena! Você digitou um número menor que o nosso!\n')

                elif player_number > number:
                    print('Que pena! Você digitou um número maior que o nosso!\n')

            except ValueError:
                print('Então, apenas números podem ser digitados nesse jogo!')

    repeat = 0
    minimum_attempts = saves[0][2]
    minimum_attempts_name = saves[0][0]
    draw = []
    draw.append(saves[0][0])

    #Calculando vencedor
    while repeat < players:  
        
        if minimum_attempts > saves[repeat][2]:
            minimum_attempts = saves[repeat][2]
            minimum_attempts_name = saves[repeat][0]
            draw = []

        elif repeat == 0:
            repeat += 1
            continue

        elif minimum_attempts == saves[repeat][2]:
            minimum_attempts = saves[repeat][2]
            minimum_attempts_name = saves[repeat][0]
            draw.append(minimum_attempts_name)
        
        else:
            pass
        
        repeat += 1  

    #Mostrando vencedor
    if players == 1:
        print('Isso foi só um teste! Agora chame seus amigos para jogar!')
        play_again = input('\nDeseja jogar novamente? (S/N) :: ')
    
    elif draw != []:
        print('\nOs empatados foram ' + ((str(draw).replace("'","")).replace("[","")).replace("]","") + '! Parabéns!')
        play_again = input('\nDeseja jogar novamente? (S/N) :: ')

    else:
        print('\nO(a) vencedor(a) foi o(a) ' + minimum_attempts_name + '! Parabéns!')
        play_again = input('\nDeseja jogar novamente? (S/N) :: ')

    #Perguntando se irá jogar o jogo novamente
    while True:
        if play_again.upper() == 'S':
            os.system('cls')
            break

        elif play_again.upper() == 'N':
            print('Obrigado por jogar!')
            break

        else:
            print('Digite S ou N!')
            continue

    if play_again.upper() == 'S':
        continue

    else:
        break
