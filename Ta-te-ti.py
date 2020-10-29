"""
Juego TA-TE-TI:
- Elige un símbolo "X" u "O"
- Las "X" inician el juego
- El juego termina con un ganador o en empate
"""

import random

def simboloJugador():
    tablero = ['_' for i in range(1,10)]
    print('Bienvenido a TA_TE_TI')
    tableroTateti(tablero)
    simbolo = input('\n Elige un simbolo "X" u "O": ').upper()
    validarSimbolo = False
    while validarSimbolo == False:
        if (simbolo == 'X' or simbolo == 'O'):
            validarSimbolo = True
            inicioPartida(simbolo,tablero)
        else:
            simbolo = input('Simbolo invalido, por favor ingrese "X" u "O": ').upper()
            validarSimbolo = False
    return simbolo

def tableroTateti(tablero):
    print('|' + tablero[0] + '|' + tablero[1] + '|' + tablero[2] + '|')
    print('|' + tablero[3] + '|' + tablero[4] + '|' + tablero[5] + '|')
    print('|' + tablero[6] + '|' + tablero[7] + '|' + tablero[8] + '|')

def inicioPartida(simbolo,tablero):
    print('Inicio del juego \n Éstas son las posiciones del tablero: \n')
    indicadorPosicion = ['0','1','2','3','4','5','6','7','8']
    tableroTateti(indicadorPosicion)
    if simbolo == 'X':
        computadora = 'O'
        juegOpcion = 1
        juego(juegOpcion,simbolo,computadora,tablero)
    else:
        computadora = 'X'
        juegOpcion = 2
        juego(juegOpcion,simbolo,computadora,tablero)
    return juegOpcion, computadora

def juego(juegOpcion,simbolo,computadora,tablero):
    finJuego = False
    while finJuego == False:
        if '_' not in tablero:
            try: 
                juegoNuevo = int(input('Fin del juego! \n ¿Desea jugar de nuevo? (1: Si 0: No): '))
                if juegoNuevo == 1:
                    finJuego = False
                    simboloJugador()
                elif juegoNuevo == 0:
                    print('Vuelve pronto')
                    finJuego = True
            except ValueError:
                print('Simbolo invalido, fin del juego')
                finJuego = True
                return
        else:
            resultado = validar_tablero(tablero)
            if resultado == 0:
                if juegOpcion == 1:
                    partidaJugador(simbolo,tablero)
                    partidaComputadora(computadora,tablero)
                else:
                    partidaComputadora(computadora,tablero)
                    partidaJugador(simbolo,tablero)
            else:
                if resultado == 1:
                    print("Ganador O!")
                elif resultado == 2:
                    print("Ganador X!")
                elif resultado == 3:
                    print("Empate!")
                finJuego = True


def validar_tablero(tablero):
    resultado = 0
    # Fila completa
    regla_1 = (tablero[0] in ('X', 'O')) and (tablero[0] == tablero[1] == tablero[2])
    regla_2 = (tablero[3] in ('X', 'O')) and (tablero[3] == tablero[4] == tablero[5])
    regla_3 = (tablero[6] in ('X', 'O')) and (tablero[6] == tablero[7] == tablero[8])
    # Columna completa
    regla_4 = (tablero[0] in ('X', 'O')) and (tablero[0] == tablero[3] == tablero[6])
    regla_5 = (tablero[1] in ('X', 'O')) and (tablero[1] == tablero[4] == tablero[7])
    regla_6 = (tablero[2] in ('X', 'O')) and (tablero[2] == tablero[5] == tablero[8])
    # diagonales
    regla_7 = (tablero[0] in ('X', 'O')) and (tablero[0]== tablero[4] == tablero[8])
    regla_8 = (tablero[2] in ('X', 'O')) and (tablero[2] == tablero[4] == tablero[6])

    if regla_1:
        resultado = 2 if tablero[0] == 'X' else 1
    elif regla_2:
        resultado = 2 if tablero[3] == 'X' else 1
    elif regla_3:
        resultado = 2 if tablero[6] == 'X' else 1
    elif regla_4:
        resultado = 2 if tablero[0] == 'X' else 1
    elif regla_5:
        resultado = 2 if tablero[1] == 'X' else 1
    elif regla_6:
        resultado = 2 if tablero[2] == 'X' else 1
    elif regla_7:
        resultado = 2 if tablero[0] == 'X' else 1
    elif regla_8:
        resultado = 2 if tablero[2] == 'X' else 1
    else:
        empate = True
        for row in tablero:
            for col in row:
                if col not in ('X', 'O'):
                    empate = False
                    break
        if empate:
            resultado = 3
    return resultado

def partidaJugador(simbolo, tablero):
    if '_' not in tablero:
        return
    else:
        validarPosicion = True
        while validarPosicion == True:
            posicion = input('Es su turno \n Ingrese una posición: ')
            if tablero[int(posicion)] == '_':
                tablero[int(posicion)] = simbolo
                tableroTateti(tablero)
                validarPosicion = False
            else:
                print('Posición ocupada, intente otra \n')
                validarPosicion = True

def partidaComputadora(computadora,tablero):
    if '_' not in tablero:
        return
    else:
        print('Turno de la computadora')
        posicion = (random.choice(([x for x in range(0,9) if tablero[x] == '_'])))
        tablero[posicion] = computadora
        tableroTateti(tablero)


simboloJugador()