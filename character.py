import pygame as pygame
import math
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, speed, health=100):
        super().__init__()
        self.speed = speed
        self.health = health

        ruta_sprites = os.path.join("sprites", "personaje1", "basic_move.png")
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

    def update(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        moving = False

        # Movimiento con WASD
        dx = 0
        dy = 0
        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1

         # Normalización para que diagonales no sean más rápidas
        if dx != 0 or dy != 0:
            moving = True
            length = math.hypot(dx, dy)  # raíz de (dx² + dy²)
            dx /= length
            dy /= length
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
        
        # Dirección hacia el mouse (ángulo en grados)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = self.rect.centery - mouse_y  # invertimos y por coordenadas de pantalla
        angle = math.degrees(math.atan2(dy, dx)) % 360

        # Clasificación de ángulo en una de 8 direcciones
        if 337.5 <= angle or angle < 22.5:
            self.direction = "right"
        elif 22.5 <= angle < 67.5:
            self.direction = "up_right"
        elif 67.5 <= angle < 112.5:
            self.direction = "up"
        elif 112.5 <= angle < 157.5:
            self.direction = "up_left"
        elif 157.5 <= angle < 202.5:
            self.direction = "left"
        elif 202.5 <= angle < 247.5:
            self.direction = "down_left"
        elif 247.5 <= angle < 292.5:
            self.direction = "down"
        elif 292.5 <= angle < 337.5:
            self.direction = "down_right"

        # Animación
        if moving:
            if current_time - self.animation_timer > self.animation_delay:
                self.frame_index = 1 + self.frame_index % (len(self.frames[self.direction])-1) # empieza desde el 1 para evitar el sprite "idle" y avanza hasta el útltimo sprite (-1 porque se empieza con uno de más) para volver a repetirse con el módulo "%".
                self.animation_timer = current_time
        else:
            self.frame_index = 0

        self.image = self.frames[self.direction][self.frame_index]
        self.rect = self.image.get_rect(center=self.rect.center)


