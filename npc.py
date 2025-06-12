import pygame as pygame
import math
import os
import random

class NPC(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.change_dir_timer = 0
        self.change_dir_interval = random.randint(1000, 3000)  
        self.state = "idle"
        self.state_timer = 0
        self.state_duration = random.randint(1000, 3000)  # duración inicial en milisegundos

        ruta_sprites = os.path.join("sprites", "prueba.png")
        sheet = pygame.image.load(ruta_sprites).convert_alpha()

        # 8 direcciones posibles para que el personaje mire
        directions = [
            "up", "up_right", "right", "down_right",
            "down", "down_left", "left", "up_left"
        ]

        self.frames = {}  # Diccionario vacío para guardar los frames de cada dirección

        for idx, dir_name in enumerate(directions):
            frame_list = []  # Lista para los 8 frames de dirección

            for i in range(8):  # 8 columnas por cada fila
                frame_x = i * 64           # columna del frame
                frame_y = idx * 64         # fila del frame (una fila por dirección)
                frame = sheet.subsurface(pygame.Rect(frame_x, frame_y, 64, 64))  # recortar imagen
                frame_list.append(frame)  # agregar el frame a la lista

            self.frames[dir_name] = frame_list  # guardar lista en el diccionario

        self.direction = "down"
        self.image = self.frames[self.direction][0]
        self.rect = self.image.get_rect(center=(400, 300))

        self.frame_index = 0
        self.animation_timer = 0
        self.animation_delay = 150


    def change_state(self):
        if self.state == "idle":
            self.state = "moving"
            self.state_duration = random.randint(2000, 4000)  # mover de 2 a 4 seg
            self.direction = self.random_dir_choice()  # nueva dirección
        else:
            self.state = "idle"
            self.state_duration = random.randint(1000, 3000)  # pausa de 1 a 3 seg

    def random_dir_choice(self):
        return random.choice([
            "up", "up_right", "right", "down_right",
            "down", "down_left", "left", "up_left"
        ])

    def update(self):
        current_time = pygame.time.get_ticks()

        # Cambiar dirección cada cierto tiempo
        if current_time - self.state_timer > self.state_duration:
            self.change_state()
            self.state_timer = current_time

        moving = False
        dx = dy = 0

        # Movimiento basado en dirección
        if self.state == "moving":
            if self.direction == "up":
                dy -= 1
            elif self.direction == "up_right":
                dy -= 1
                dx += 1
            elif self.direction == "right":
                dx += 1
            elif self.direction == "down_right":
                dy += 1
                dx += 1
            elif self.direction == "down":
                dy += 1
            elif self.direction == "down_left":
                dy += 1
                dx -= 1
            elif self.direction == "left":
                dx -= 1
            elif self.direction == "up_left":
                dy -= 1
                dx -= 1

            if dx != 0 or dy != 0:
                moving = True
                length = math.hypot(dx, dy)
                dx /= length
                dy /= length
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed

        # Animación
        if moving:
            if current_time - self.animation_timer > self.animation_delay:
                self.frame_index = (self.frame_index + 1) % len(self.frames[self.direction])
                self.animation_timer = current_time
        else:
            self.frame_index = 0

        self.image = self.frames[self.direction][self.frame_index]