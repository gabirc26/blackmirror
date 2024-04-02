pergunta_1 = "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?"
pergunta_2 = "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?"
pergunta_3 = "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?"
pergunta_4 = "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?"
pergunta_5 = "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?"
pergunta_6 = "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?"
pergunta_7 = "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE."
usuario = input("Qual sua pergunta?: " ).upper()

if usuario == pergunta_1:
    print('Annie Murphy')

elif usuario == pergunta_2:
     print('Super Computador')

elif usuario == pergunta_3:
     print('Streamberry')

elif usuario == pergunta_4:
     print('Procurando uma série para assistir')
     
elif usuario == pergunta_5:
     print('SURTO')

elif usuario == pergunta_6:
     print('Manipulação dos Dados, Deep Fake, realidade virtual, série')

elif usuario == pergunta_7:
     print('Sim, termina de uma maneira que não imaginava, era tudo uma série com algo que aconteceu em outra realidade.')
        
else:
     print('Não encontrei a sua pergunta')