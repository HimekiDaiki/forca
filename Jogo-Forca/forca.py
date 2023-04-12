#Observação: Assista One Piece
#Jogo da Forca em Python 3
#Desenvolvedor: HimekiDaiki
#Versão: 1.0

#Menu de Boas vindas
print('********************************')
print('***Bem Vindo ao Jogo da Forca***')
print('********************************')
print('Dica: Existe tanto no mar quanto no céu')

palavra_secreta = "Estrela" .upper()
letras_acertadas =["_" for letra in palavra_secreta]
print(letras_acertadas)

#Variavel para ver se ta funcionando 
enforcou = False
acertou = False
erros = 0

#Controle de fim do jogo
while( not enforcou and not acertou):
    chute = input(" Qual a letra? ")
    chute = chute.strip().upper()

    if( chute in palavra_secreta ):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1
    else:
        erros += 1

    print(letras_acertadas)
    print('Chutes Errados ', erros)
    
    if erros == 7 : 
        enforcou = True
    
    if '_' not in letras_acertadas: 
        acertou = True
    if acertou == True: 
        print('Você Ganhou!!')
    if enforcou == True: 
        print('Você Perdeu!')
        print('Fim de Jogo')
    
input()    
