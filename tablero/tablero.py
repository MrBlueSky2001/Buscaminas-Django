# Importa el módulo random
import random

# Clase que representa una casilla en el tablero
class Casilla:
    def __init__(self):
        # Indica si la casilla contiene una mina
        self.contiene_mina = False
        # Número de minas adyacentes a la casilla
        self.minas_adyacentes = 0
        # Lista de posiciones adyacentes a la casilla
        self.adyacentes = []

# Clase que representa el tablero de juego
class Tablero:
    def __init__(self, filas, columnas, num_minas):
        # Número de filas en el tablero
        self.filas = filas
        # Número de columnas en el tablero
        self.columnas = columnas
        # Número total de minas en el tablero
        self.num_minas = num_minas
        # Matriz que representa el tablero, con instancias de la clase Casilla
        self.tablero = [[Casilla() for _ in range(columnas)] for _ in range(filas)]
        
        # Inicializa el tablero generando minas y calculando minas adyacentes
        self.generar_minas()
        self.calcular_minas_adyacentes()

    # Método para generar minas en posiciones aleatorias del tablero
    def generar_minas(self):
        minas_generadas = 0
        while minas_generadas < self.num_minas:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if not self.tablero[fila][columna].contiene_mina:
                self.tablero[fila][columna].contiene_mina = True
                minas_generadas += 1

    # Método para calcular el número de minas adyacentes a cada casilla
    def calcular_minas_adyacentes(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                casilla = self.tablero[fila][columna]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= fila + i < self.filas and 0 <= columna + j < self.columnas:
                            casilla.adyacentes.append((fila + i, columna + j))
                            if self.tablero[fila + i][columna + j].contiene_mina:
                                casilla.minas_adyacentes += 1

    # Método para representar el tablero como una lista de listas en formato HTML
    def mostrar_tablero(self):
        tablero_html = []
        for fila in range(self.filas):
            fila_html = []
            for columna in range(self.columnas):
                casilla = self.tablero[fila][columna]
                if casilla.contiene_mina:
                    fila_html.append('M')
                elif casilla.minas_adyacentes > 0:
                    fila_html.append(str(casilla.minas_adyacentes))
                else:
                    fila_html.append('')
            tablero_html.append(fila_html)

        return tablero_html
