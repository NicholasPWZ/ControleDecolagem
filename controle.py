from plane import Plane
from airport import Airport
print(r'''    
                       --====|====--
                             |  

                         .-"""""-. 
                       .'_________'. 
                      /_/_|__|__|_\_\
                     ;'-._       _.-';
,--------------------|    `-. .-'    |--------------------,
 ``""--..__    ___   ;       '       ;   ___    __..--""``
           `"-// \\.._\             /_..// \\-"`
              \\_//    '._       _.'    \\_//
               `"`        ``---``        `"`''''' '\n'
                     'Airport Simulator\n'
                        'By Nicholas')
 
nome_aero = input('Crie o Aeroporto:\nInforme o nome do Aeroporto:')
aeroporto = Airport(nome_aero)
while True:
    comando = input('S - para sair\nA - para adicionar um avião na fila\nD - para deletar um avião da fila\nL - exibir a fila\
\nP - exibe o próximo avião a decolar\nN - Decolar próximo avião da fila\nK - para exibir o número de aviões na fila\
\nI - para procurar um avião pelo número\nInforme o comando:')
    comando = comando.lower()
    if comando == 's':
        print('Você saiu do programa')
        break
    elif comando == 'a':
       numero_a = input('Informe o numero do avião: ')
       modelo_a = input('Informe o modelo do avião: ')
       companhia_a = input('Informe a companhia aérea do avião: ')
       aviao = Plane(numero_a,modelo_a, companhia_a)
       aeroporto.add_fila(aviao)
    elif comando == 'd':
        for i, fila_numerada in enumerate(aeroporto.fila):
            print(f'{i}, {fila_numerada.numero}')
        index = input('Informe o número do aviao a ser deletado da fila')
        aeroporto.del_fila(index)
        print('Aviao retirado da fila!')
    elif comando == 'l':
        for i, fila_numerada in enumerate(aeroporto.fila):
            print(f'{i}, {fila_numerada.numero}')
    elif comando == 'p':
        print(f'Número: {aeroporto.fila[0].numero}\nModelo: {aeroporto.fila[0].modelo}\nCompanhia: {aeroporto.fila[0].companhia}')
    elif comando == 'n':
        print(f'Avião nº {aeroporto.fila[0].numero} decolando...')
        aeroporto.del_fila[0]
    elif comando == 'i':
        id = input('Informe o número do avião procurado: ')
        for i in aeroporto.fila:
            if id == i.numero:
                print(f'Número: {i.numero}\nModelo: {i.modelo}\nCompanhia: {i.companhia}\nPosição na fila: {aeroporto.fila.index(i) + 1}')



        



