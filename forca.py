import random
#LISTAS
fruits = ['laranja', 'banana', 'mamao', 'melancia']
cores = ['vermelho', 'verde', 'azul', 'amarelo','laranja','lilas']
marcas = ['cocacola', 'guarana', 'saogeraldo']
animais = ['gato', 'cachorro', 'papagaio', 'hamster']
words = {'Frutas': fruits, 'Cores': cores, 'Marcas de refrigerante': marcas, 'Animais domésticos': animais}

chaves = list(words.keys())
classe = random.choice(chaves)
palavra = random.choice(words[classe])

#TESTE
# print(chaves)
# print(classe)
# print(palavra)

#PONTOS DE PARADA
vidas = 5
tentativas = 0

#INTRODUÇÃO
print('='*90)
print('JOGO DA FORCA')
print('Desconsidere: espaços, acentos e letras maiúsculas')
print('='*90)

#CÓDIGO NA INTEGRA
while True:
    for c in range (len(palavra)):
        numero = len(palavra)
    letra = input(f' A categoria é: {classe} e a palavra possui {numero} letras. Digite uma letra: ').lower()
    digitadas = []
    digitadas.append(letra)
    secreto_temporario = ''
    
    if tentativas >= 0:
        chute = input(f'Você tem 3 tentativas de chute, deseja chutar uma palavra? (S/N):').lower()
        if chute == 'S' or chute == 's':
            chute_palavra = input('Chute uma palavra:').lower()
            tentativas += 1
            if chute_palavra == palavra:
                print(f'Parabéns, você acertou a palavra: {palavra}')
                break
            else:
                print(f'Você errou, a palavra era: {palavra}', end=' ')
                vidas = 0 
                print(f'Vidas: {vidas}')
                break
            
    for letra_secreta in palavra:

        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '_'

        
    print(f'As letras que você digitou estão nas seguintes posições: {secreto_temporario}') 

    if letra not in secreto_temporario:
        print(f'A letra {letra} não está na palavra {palavra}, você perdeu uma vida.', end=' ')
        vidas -= 1
        print(f'Vidas: {vidas}')

    if vidas == 0:
         print(f'Você perdeu pois suas vidas acabaram, a palavra era: {palavra}')
         break