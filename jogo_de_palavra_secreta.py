import os # o importamento de os, ela vai limpar o seu ternimal quando for finalizado o jogo

palavra_secreta = 'Coruja'
letras_acertadas = '' # vai recebar o valor da letra acertadas q esta dentro do if 
numero_de_tentativa = 0

while True: # o jogo vai ser rodado tudo aqui
    
    letra_digitada = input('Digite apenas uma letra: ') # vai ser pedido para q o jogador digite apenas 1 letra

    numero_de_tentativa += 1

    if len(letra_digitada) > 1: # se caso o jogador digitar mais q 1 letra, vai dar 1 erro e voltar para o inicio
        print('Digite apenas 1 letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('A palvra formada é', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('Clear')
        print('VOCÊ GANHOU !!! PARABÉNS')
        print('A palavra era ', palavra_secreta)
        print('tentativas: ', numero_de_tentativa)
        letras_acertadas = '' # vai recebar o valor da letra acertadas q esta dentro do if 
        numero_de_tentativa = 0

    
