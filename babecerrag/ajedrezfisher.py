# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.
Trabajo Anterior: https://colab.research.google.com/drive/1bjnU75IsBKKzH3TY3YxN-ykyJJYhx9Tn
Original file is located at
    https://colab.research.google.com/drive/1iiELzLLXbovefVQtBWot077qtcR8e7J1

TRABAJO REALIZADO POR: BRAYAN BECERRA Y JHOUSUA ALBADAN
"""

import random

class Tablero:
    def __init__(self):
        self.tablero = self.inicializar_tablero()
        self.turno_blancas = True
        self.movimientos = []
    
    def inicializar_tablero(self):
        tablero = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                   ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                   ['.', '.', '.', '.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.', '.', '.', '.'],
                   ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                   ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        return tablero
    
    def generar_posicion_ajedrez_960(self):
        piezas = ["r", "n", "b", "q", "k", "b", "n", "r"]
        random.shuffle(piezas)
        
        posicion_inicial = [piezas[i] for i in range(8)]
        posicion_inicial.extend(["p"] * 8)
        posicion_inicial.extend(["."] * 32)
        posicion_inicial.extend(["P"] * 8)
        posicion_inicial.extend([piezas[i].upper() for i in range(8)])
        
        random.shuffle(posicion_inicial)
        
        return [posicion_inicial[i:i+8] for i in range(0, 64, 8)]
    
    def mostrar_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))
    
    def movimiento_valido(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        # Comprobar si las coordenadas están dentro del tablero
        if not (0 <= fila_inicial < 8 and 0 <= columna_inicial < 8 and 0 <= fila_destino < 8 and 0 <= columna_destino < 8):
            return False
        
        # Comprobar si la casilla de origen contiene una pieza del jugador actual
        if (self.turno_blancas and self.tablero[fila_inicial][columna_inicial].islower()) or (not self.turno_blancas and self.tablero[fila_inicial][columna_inicial].isupper()):
            return False
        
        # Comprobar si el movimiento es válido para la pieza en la casilla de origen
        pieza = self.tablero[fila_inicial][columna_inicial].lower()
        if pieza == 'p':
            return self.movimiento_valido_peon(fila_inicial, columna_inicial, fila_destino, columna_destino)
        elif pieza == 'r':
            return self.movimiento_valido_torre(fila_inicial, columna_inicial, fila_destino, columna_destino)
        elif pieza == 'n':
            return self.movimiento_valido_caballo(fila_inicial, columna_inicial, fila_destino, columna_destino)
        elif pieza == 'b':
            return self.movimiento_valido_alfil(fila_inicial, columna_inicial, fila_destino, columna_destino)
        elif pieza == 'q':
            return self.movimiento_valido_reina(fila_inicial, columna_inicial, fila_destino, columna_destino)
        elif pieza == 'k':
            return self.movimiento_valido_rey(fila_inicial, columna_inicial, fila_destino, columna_destino)
        
        return False
    
    def movimiento_valido_peon(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        # Implementar lógica de movimiento válido para el peón
        pass
    
    def movimiento_valido_torre(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        # Implementar lógica de movimiento válido para la torre
        pass
    
    def movimiento_valido_caballo(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        # Implementar lógica de movimiento válido para el caballo
        pass
    
    def movimiento_valido_alfil(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        # Implementar lógica de movimiento válido para el alfil
        pass
    
    def movimiento_valido_reina(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        # Implementar lógica de movimiento válido para la reina
        pass
    
    def movimiento_valido_rey(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        # Implementar lógica de movimiento válido para el rey
        pass
    
    def realizar_movimiento(self, fila_inicial, columna_inicial, fila_destino, columna_destino):
        if self.movimiento_valido(fila_inicial, columna_inicial, fila_destino, columna_destino):
            # Actualizar el tablero con el movimiento realizado
            self.tablero[fila_destino][columna_destino] = self.tablero[fila_inicial][columna_inicial]
            self.tablero[fila_inicial][columna_inicial] = '.'
            
            # Registrar el movimiento
            movimiento = {
                'fila_inicial': fila_inicial,
                'columna_inicial': columna_inicial,
                'fila_destino': fila_destino,
                'columna_destino': columna_destino
            }
            self.movimientos.append(movimiento)
            
            # Cambiar el turno de juego
            self.turno_blancas = not self.turno_blancas
        else:
            print("Movimiento inválido")
    
    def jugar(self):
        self.tablero = self.generar_posicion_ajedrez_960()
        
        while True:
            self.mostrar_tablero()
            
            if self.turno_blancas:
                jugador_actual = "Blancas"
            else:
                jugador_actual = "Negras"
            
            print("Turno de las", jugador_actual)
            
            # Solicitar al jugador que ingrese el movimiento
            fila_inicial = int(input("Ingrese la fila de la casilla de origen (0-7): "))
            columna_inicial = int(input("Ingrese la columna de la casilla de origen (0-7): "))
            fila_destino = int(input("Ingrese la fila de la casilla de destino (0-7): "))
            columna_destino = int(input("Ingrese la columna de la casilla de destino (0-7): "))
            
            # Realizar el movimiento
            self.realizar_movimiento(fila_inicial, columna_inicial, fila_destino, columna_destino)
            
            # Verificar si hay jaque mate o empate
            # (Implementar lógica adicional para determinar el final del juego)
            

# Ejemplo de uso
tablero = Tablero()
tablero.jugar()