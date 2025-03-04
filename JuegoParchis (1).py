import pygame
import random
import math


# Clase Tablero ya implementada
class Tablero:
    def __init__(self, width=600, height=600):
        pygame.init()
        self.width, self.height = width, height
        pygame.display.set_caption("Proyecto final programación")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.colors = {
            "WHITE": (255, 255, 255), "BLACK": (0, 0, 0), "RED": (255, 0, 0),
            "BLUE": (0, 0, 255), "GREEN": (0, 255, 0), "YELLOW": (255, 255, 0), "GRAY": (150, 150, 150)
        }
        self.cell_size_sup = self.width / 20
        self.cell_size_mid = self.width / 10
        self.border = 3

    def dibujar_triangulos(self):
        pygame.draw.polygon(self.screen, self.colors["BLACK"], [[210, 390], [300, 300], [390, 390]], 3)
        pygame.draw.polygon(self.screen, self.colors["YELLOW"], [[240, 360], [300, 300], [360, 360]])
        pygame.draw.polygon(self.screen, self.colors["BLACK"], [[240, 360], [300, 300], [360, 360]], 3)
        pygame.draw.polygon(self.screen, self.colors["BLACK"], [[210, 210], [300, 300], [390, 210]], 3)
        pygame.draw.polygon(self.screen, self.colors["GREEN"], [[240, 360], [300, 300], [240, 240]])
        pygame.draw.polygon(self.screen, self.colors["BLACK"], [[240, 360], [300, 300], [240, 240]], 3)
        pygame.draw.polygon(self.screen, self.colors["RED"], [[240, 240], [300, 300], [360, 240]])
        pygame.draw.polygon(self.screen, self.colors["BLACK"], [[240, 240], [300, 300], [360, 240]], 3)
        pygame.draw.polygon(self.screen, self.colors["BLUE"], [[360, 240], [300, 300], [360, 360]])
        pygame.draw.polygon(self.screen, self.colors["BLACK"], [[360, 240], [300, 300], [360, 360]], 3)

    def dibujar_casas(self):
        pygame.draw.rect(self.screen, self.colors["RED"], (0, 0, 7 * self.cell_size_sup, 7 * self.cell_size_sup))
        pygame.draw.rect(self.screen, self.colors["BLUE"],
                         (13 * self.cell_size_sup, 0, 7 * self.cell_size_sup, 7 * self.cell_size_sup))
        pygame.draw.rect(self.screen, self.colors["GREEN"],
                         (0, 13 * self.cell_size_sup, 7 * self.cell_size_sup, 7 * self.cell_size_sup))
        pygame.draw.rect(self.screen, self.colors["YELLOW"], (
        13 * self.cell_size_sup, 13 * self.cell_size_sup, 7 * self.cell_size_sup, 7 * self.cell_size_sup))
        pygame.draw.rect(self.screen, self.colors["GRAY"], [400,400,200,100])
        pygame.draw.rect(self.screen, self.colors["BLACK"], [400, 400, 200, 100],3)

    def dibujar_torres(self):
        pygame.draw.rect(self.screen, self.colors["YELLOW"], [270, 360, 60, 240])
        pygame.draw.rect(self.screen, self.colors["RED"], [270, 0, 60, 240])
        pygame.draw.rect(self.screen, self.colors["GREEN"], [0, 270, 240, 60])
        pygame.draw.rect(self.screen, self.colors["BLUE"], [360, 270, 240, 60])

    def dibujar_lineas_horizontales(self):
        for i in range(1, 7):
            pygame.draw.line(self.screen, self.colors["BLACK"], (7 * self.cell_size_sup, i * self.cell_size_sup),
                             (13 * self.cell_size_sup, i * self.cell_size_sup),
                             self.border)
        for i in range(6, 10):
            pygame.draw.line(self.screen, self.colors["BLACK"],
                             (0, (i - 5) * self.cell_size_mid + 5 * self.cell_size_sup),
                             (self.width, (i - 5) * self.cell_size_mid + 5 * self.cell_size_sup), self.border)
        for i in range(14, 21):
            pygame.draw.line(self.screen, self.colors["BLACK"], (7 * self.cell_size_sup, i * self.cell_size_sup),
                             (13 * self.cell_size_sup, i * self.cell_size_sup),
                             self.border)

    def dibujar_lineas_verticales(self):
        for i in range(1, 7):
            pygame.draw.line(self.screen, self.colors["BLACK"], (i * self.cell_size_sup, 7 * self.cell_size_sup),
                             (i * self.cell_size_sup, 13 * self.cell_size_sup),
                             self.border)

        pygame.draw.line(self.screen, self.colors["BLACK"], (210, 0), (210, 600), self.border)

        pygame.draw.line(self.screen, self.colors["BLACK"], (270, 0), (270, 238), self.border)
        pygame.draw.line(self.screen, self.colors["BLACK"], (270, 360), (270, 600), self.border)
        pygame.draw.line(self.screen, self.colors["BLACK"], (330, 0), (330, 238), self.border)
        pygame.draw.line(self.screen, self.colors["BLACK"], (330, 360), (330, 600), self.border)

        pygame.draw.line(self.screen, self.colors["BLACK"], (390, 0), (390, 600), self.border)

        for i in range(14, 21):
            pygame.draw.line(self.screen, self.colors["BLACK"], (i * self.cell_size_sup, 7 * self.cell_size_sup),
                             (i * self.cell_size_sup, 13 * self.cell_size_sup),
                             self.border)

    def dibujar_seguros(self):
        pygame.draw.rect(self.screen, self.colors['YELLOW'], [330, 450, 60, 30])
        pygame.draw.rect(self.screen, self.colors['GRAY'], [210, 450, 60, 30])
        pygame.draw.rect(self.screen, self.colors['GRAY'], [330, 120, 60, 30])
        pygame.draw.rect(self.screen, self.colors['RED'], [210, 120, 60, 30])

        pygame.draw.rect(self.screen, self.colors['GRAY'], [450, 330, 30, 60])
        pygame.draw.rect(self.screen, self.colors['BLUE'], [450, 210, 30, 60])
        pygame.draw.rect(self.screen, self.colors['GRAY'], [120, 210, 30, 60])
        pygame.draw.rect(self.screen, self.colors['GREEN'], [120, 330, 30, 60])

    def dibujar_tablero(self):
        self.screen.fill(self.colors['WHITE'])
        self.dibujar_casas()
        self.dibujar_torres()
        self.dibujar_seguros()
        self.dibujar_lineas_horizontales()
        self.dibujar_lineas_verticales()
        self.dibujar_triangulos()

    def run(self):
        running = True
        while running:
            self.dibujar_tablero()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
        pygame.quit()


# Clase Dado
class Dado:
    def __init__(self, tablero):
        self.tablero = tablero
        self.valor = 1
        self.tamaño = 50
        self.posicion = (500,425)  # Posición por defecto
        self.font = pygame.font.SysFont(None, 30)

    def lanzar(self):
        """Lanza el dado y devuelve un valor entre 1 y 6"""
        self.valor = random.randint(1, 6)
        return self.valor

    def dibujar(self):
        """Dibuja el dado en la pantalla"""
        # Dibuja el cuadrado del dado
        pygame.draw.rect(self.tablero.screen, self.tablero.colors["WHITE"],
                         (self.posicion[0], self.posicion[1], self.tamaño, self.tamaño))
        pygame.draw.rect(self.tablero.screen, self.tablero.colors["BLACK"],
                         (self.posicion[0], self.posicion[1], self.tamaño, self.tamaño), 2)

        # Dibuja los puntos según el valor del dado
        if self.valor == 1:
            self._dibujar_punto(0, 0)
        elif self.valor == 2:
            self._dibujar_punto(-1, -1)
            self._dibujar_punto(1, 1)
        elif self.valor == 3:
            self._dibujar_punto(-1, -1)
            self._dibujar_punto(0, 0)
            self._dibujar_punto(1, 1)
        elif self.valor == 4:
            self._dibujar_punto(-1, -1)
            self._dibujar_punto(-1, 1)
            self._dibujar_punto(1, -1)
            self._dibujar_punto(1, 1)
        elif self.valor == 5:
            self._dibujar_punto(-1, -1)
            self._dibujar_punto(-1, 1)
            self._dibujar_punto(0, 0)
            self._dibujar_punto(1, -1)
            self._dibujar_punto(1, 1)
        elif self.valor == 6:
            self._dibujar_punto(-1, -1)
            self._dibujar_punto(-1, 0)
            self._dibujar_punto(-1, 1)
            self._dibujar_punto(1, -1)
            self._dibujar_punto(1, 0)
            self._dibujar_punto(1, 1)

    def _dibujar_punto(self, x_offset, y_offset):
        """Dibuja un punto en el dado según el offset desde el centro"""
        centro_x = self.posicion[0] + self.tamaño / 2
        centro_y = self.posicion[1] + self.tamaño / 2
        radio = self.tamaño / 10
        x = centro_x + x_offset * (self.tamaño / 3)
        y = centro_y + y_offset * (self.tamaño / 3)
        pygame.draw.circle(self.tablero.screen, self.tablero.colors["BLACK"], (int(x), int(y)), int(radio))

recorrido_base = [
            (342, 583), (343, 553), (341, 523), (341, 492), (341, 465), (342, 433), (343, 402), (341, 373),
            (375, 338), (402, 343), (432, 342), (464, 340), (492, 340), (522, 341), (553, 342), (582, 343),
            (583, 280), (583, 254), (553, 257), (524, 255), (491, 255), (463, 257), (434, 254), (404, 255),
            (375, 255), (342, 226), (339, 193), (339, 165), (256, 132), (340, 102), (341, 72), (341, 40),
            (341, 11), (280, 12), (255, 9), (256, 40), (257, 73), (256, 100), (256, 132), (256, 161),
            (257, 190), (256, 225), (223, 256), (193, 255), (166, 255), (135, 254), (104, 256), (74, 255),
            (44, 254), (12, 256), (11, 315), (11, 341), (43, 343), (71, 343), (100, 342), (132, 342),
            (163, 343), (192, 343), (225, 343), (251, 373), (253, 402), (253, 433), (250, 463), (254, 496),
            (255, 520), (255, 554), (255, 583), (314, 584)
        ]

# Clase Ficha
class Ficha:
    salidas = {
        "RED": 38,
        "BLUE": 21,
        "GREEN": 55,
        "YELLOW": 4
    }
    def __init__(self, color, indice, tablero):
        self.color = color  # RED, BLUE, GREEN o YELLOW
        self.indice = indice  # 0, 1, 2, 3 (número de ficha)
        self.tablero = tablero
        self.posicion = None  # Coordenadas (x, y) en el tablero
        self.casilla = -1  # -1 si está en casa, 0-67 si está en el recorrido
        self.en_casa = True
        self.en_meta = False
        self.radio = 15

        # Establecer posición inicial en casa
        self._establecer_posicion_inicial()

    def _establecer_posicion_inicial(self):
        """Establece la posición inicial de la ficha en su casa"""
        offset_x = 25 + (self.indice % 2) * 50
        offset_y = 25 + (self.indice // 2) * 50

        if self.color == "RED":
            self.posicion = (offset_x, offset_y)
        elif self.color == "BLUE":
            self.posicion = (self.tablero.width - offset_x, offset_y)
        elif self.color == "GREEN":
            self.posicion = (offset_x, self.tablero.height - offset_y)
        elif self.color == "YELLOW":
            self.posicion = (self.tablero.width - offset_x, self.tablero.height - offset_y)

    def obtener_posicion_casilla(self, casilla):
        """Obtiene la coordenada (x, y) de una casilla en el tablero, ajustada para cada color"""

        if 0 <= casilla < len(recorrido_base):
            print(f"🎯 Casilla {casilla} -> Posición {recorrido_base[casilla]}")  # Debug
            return recorrido_base[casilla]
        else:
            print(f"⚠️ Casilla {casilla} fuera de rango, usando posición default")  # Debug
            return (300, 300)  # Posición de error

    def dibujar(self):
        """Dibuja la ficha en el tablero"""
        if self.posicion:
            pygame.draw.circle(self.tablero.screen, self.tablero.colors[self.color],
                               (int(self.posicion[0]), int(self.posicion[1])), self.radio)
            pygame.draw.circle(self.tablero.screen, self.tablero.colors["BLACK"],
                               (int(self.posicion[0]), int(self.posicion[1])), self.radio, 2)

            # Dibuja el número de la ficha
            font = pygame.font.SysFont(None, 20)
            texto = font.render(str(self.indice + 1), True, self.tablero.colors["BLACK"])
            self.tablero.screen.blit(texto, (int(self.posicion[0] - 5), int(self.posicion[1] - 8)))

    def mover(self, pasos, forzar_salida=False):
        """Mueve la ficha un número de pasos por su recorrido único"""

        print(
            f"🔍 Intentando mover ficha {self.color}: pasos={pasos}, en_casa={self.en_casa}, forzar_salida={forzar_salida}")

        # 1️⃣ Si la ficha está en casa y saca un 5, debe salir
        if self.en_casa and pasos == 5:
            if forzar_salida:
                self.en_casa = False
                self.casilla = Ficha.salidas[self.color]  # Casilla de salida fija
                self.posicion = recorrido_base[self.casilla]  # Asigna directamente la coordenada
                print(f"✅ Ficha {self.color} ha salido correctamente en {self.posicion}")
                return True
            return False

        # 2️⃣ Si la ficha ya está en juego, debe moverse normalmente
        if not self.en_casa and not self.en_meta:
            nueva_casilla = self.casilla + pasos

            # Verificar si llega a la meta
            if nueva_casilla >= 68:
                self.en_meta = True
                self.casilla = 68
                return True

            # Asegurar que la casilla y posición se actualicen correctamente
            self.casilla = nueva_casilla
            self.posicion = self.obtener_posicion_casilla(self.casilla)
            print(f"📍 Ficha {self.color} movida a casilla {self.casilla}, nueva posición {self.posicion}")
            return True

        return False


# Clase Jugador
class Jugador:
    def __init__(self, color, nombre, tablero):
        self.color = color
        self.nombre = nombre
        self.tablero = tablero
        self.fichas = [Ficha(color, i, tablero) for i in range(4)]
        self.dado = None  # Se asignará más tarde
        self.turno = False

    def lanzar_dado(self):
        """Lanza el dado y devuelve el resultado"""
        if self.turno and self.dado:
            return self.dado.lanzar()
        return 0

    def mover_ficha(self, indice_ficha, pasos):
        """Mueve una ficha específica del jugador"""
        if self.turno and 0 <= indice_ficha < len(self.fichas):
            return self.fichas[indice_ficha].mover(pasos)
        return False

    def dibujar_fichas(self):
        """Dibuja todas las fichas del jugador"""
        for ficha in self.fichas:
            ficha.dibujar()

    def todas_en_meta(self):
        """Verifica si todas las fichas han llegado a la meta"""
        return all(ficha.en_meta for ficha in self.fichas)


# Clase Juego
class Juego:
    def __init__(self, num_jugadores=4):
        self.tablero = Tablero()
        self.dados = [Dado(self.tablero), Dado(self.tablero)]  # Crear dos dados
        self.dados[0].posicion = (470, 425)
        self.dados[1].posicion = (530, 425)

        colores = ["RED", "BLUE", "GREEN", "YELLOW"]
        self.jugadores = []

        for i in range(min(num_jugadores, 4)):
            jugador = Jugador(colores[i], f"Jugador {i + 1}", self.tablero)
            self.jugadores.append(jugador)

        self.turno_actual = 0
        self.jugadores[self.turno_actual].turno = True
        self.esperando_seleccion = False
        self.valores_dados = (0, 0)
        self.dados_lanzados = False  # 🔹 Se inicializa como False
        self.font = pygame.font.SysFont(None, 18)

    def cambiar_turno(self):
        """Cambia el turno al siguiente jugador"""
        self.jugadores[self.turno_actual].turno = False
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        self.jugadores[self.turno_actual].turno = True
        self.esperando_seleccion = False

    def procesar_eventos(self, event):
        """Procesa los eventos del juego"""
        jugador_actual = self.jugadores[self.turno_actual]

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(f"🖱️ Clic detectado en posición {pos}")

            # 1️⃣ Verificar si se hizo clic en los dados para lanzarlos (solo si aún no han sido lanzados)
            if not self.dados_lanzados:
                dado1_x, dado1_y = self.dados[0].posicion
                dado2_x, dado2_y = self.dados[1].posicion
                dado_tamaño = self.dados[0].tamaño

                if (dado1_x <= pos[0] <= dado1_x + dado_tamaño and dado1_y <= pos[1] <= dado1_y + dado_tamaño) or \
                        (dado2_x <= pos[0] <= dado2_x + dado_tamaño and dado2_y <= pos[1] <= dado2_y + dado_tamaño):

                    print("🎲 Clic en los dados detectado, lanzando ambos...")
                    self.valores_dados = (self.dados[0].lanzar(), self.dados[1].lanzar())
                    self.dados_lanzados = True
                    print(f"🎲 Resultado de los dados: {self.valores_dados}")

                    # 2️⃣ Verificar si todas las fichas están en casa y NO salió un 5
                    todas_en_casa = all(ficha.en_casa for ficha in jugador_actual.fichas)

                    if todas_en_casa and 5 not in self.valores_dados:
                        print("🚫 Todas las fichas están en casa y no salió un 5. Cambio de turno.")
                        self.dados_lanzados = False  # 🔹 Resetear para el siguiente turno
                        self.cambiar_turno()
                        return

                    # Si al menos una ficha puede moverse, esperar selección
                    self.esperando_seleccion = True
                    return

            # 3️⃣ Esperar selección de ficha después de lanzar los dados
            if self.esperando_seleccion:
                print("🎯 Esperando selección de ficha...")
                for i, ficha in enumerate(jugador_actual.fichas):
                    if ficha.posicion:
                        dx = pos[0] - ficha.posicion[0]
                        dy = pos[1] - ficha.posicion[1]
                        distancia = math.sqrt(dx ** 2 + dy ** 2)

                        if distancia <= ficha.radio:
                            print(f"🔍 Ficha {ficha.color} seleccionada")

                            # Verificar si la ficha está en casa y se usará un 5 para sacarla
                            if ficha.en_casa:
                                if 5 in self.valores_dados:
                                    print(f"🚪 Sacando ficha {ficha.color} de la cárcel con un 5")
                                    if ficha.mover(5, forzar_salida=True):
                                        if self.valores_dados[0] == 5:
                                            self.valores_dados = (0, self.valores_dados[1])
                                        else:
                                            self.valores_dados = (self.valores_dados[0], 0)
                                    break

                                    # Si la ficha ya está en juego, permitir elegir qué dado usar
                            if self.valores_dados[0] > 0:
                                print(f"⚀ Intentando mover ficha {ficha.color} con dado 1 ({self.valores_dados[0]})")
                                if ficha.mover(self.valores_dados[0]):
                                    self.valores_dados = (0, self.valores_dados[1])

                            elif self.valores_dados[1] > 0:
                                print(f"⚁ Intentando mover ficha {ficha.color} con dado 2 ({self.valores_dados[1]})")
                                if ficha.mover(self.valores_dados[1]):
                                    self.valores_dados = (self.valores_dados[0], 0)

                                    # Si ambos dados fueron usados o no hay más movimientos posibles, cambiar turno
                            if self.valores_dados == (0, 0):
                                print("🔄 Ambos dados usados, cambiando turno.")
                                self.esperando_seleccion = False
                                self.dados_lanzados = False  # 🔹 Resetear para el siguiente turno
                                self.cambiar_turno()
                            break

    def dibujar_info_turno(self):
        """Dibuja información del turno actual"""
        jugador_actual = self.jugadores[self.turno_actual]

        # Dibujar nombre y color del jugador actual
        texto_jugador = self.font.render(f"Turno: {jugador_actual.nombre}", True,
                                         self.tablero.colors[jugador_actual.color])
        self.tablero.screen.blit(texto_jugador, (405, 405))

        # Instrucciones
        if self.esperando_seleccion:
            texto_instr = self.font.render(f"Selecciona una ficha para mover", True, self.tablero.colors["BLACK"])
            texto_dado1 = self.font.render(f"Dado 1: {self.valores_dados[0]}", True, self.tablero.colors["BLACK"])
            texto_dado2 = self.font.render(f"Dado 2: {self.valores_dados[1]}", True, self.tablero.colors["BLACK"])
            self.tablero.screen.blit(texto_instr, (405, 480))
            self.tablero.screen.blit(texto_dado1, (405, 500))
            self.tablero.screen.blit(texto_dado2, (405, 515))
        else:
            texto_instr = self.font.render("Haz clic en los dados para lanzar", True, self.tablero.colors["BLACK"])
            self.tablero.screen.blit(texto_instr, (405, 480))

    def comprobar_ganador(self):
        """Comprueba si hay un ganador"""
        for i, jugador in enumerate(self.jugadores):
            if jugador.todas_en_meta():
                return i
        return -1

    def run(self):
        """Bucle principal del juego"""
        running = True
        clock = pygame.time.Clock()

        while running:
            # Procesar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.procesar_eventos(event)

            # Comprobar si hay ganador
            ganador = self.comprobar_ganador()
            if ganador >= 0:
                texto_ganador = self.font.render(f"¡{self.jugadores[ganador].nombre} ha ganado!", True,
                                                 self.tablero.colors["BLACK"])
                self.tablero.screen.blit(texto_ganador, (200, 300))

            # Dibujar todo
            self.tablero.dibujar_tablero()

            # Dibujar fichas
            for jugador in self.jugadores:
                jugador.dibujar_fichas()

            # Dibujar dados
            for dado in self.dados:
                dado.dibujar()

            # Dibujar información del turno
            self.dibujar_info_turno()

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


# Función principal
def main():
    num_jugadores = 4  # Se puede cambiar según la necesidad
    juego = Juego(num_jugadores)
    juego.run()


if __name__ == "__main__":
    main()