import pygame
import sys

pygame.init()

# Задаємо розміри вікна
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Початкові координати фігури
x = width // 2
y = height // 2

# Початкова швидкість руху фігури
speed_x = 0.2
speed_y = 0.5

# Завантаження зображення
image = pygame.image.load("catgif.png")

# Завантаження музичного файлу
#pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.play(-1)

# Основний цикл програми
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # Очищаємо екран

    # Зміщуємо фігуру
    x += speed_x
    y += speed_y

    # Змінюємо напрямок руху, якщо фігура доторкнулась до меж вікна
    if x <= 0 or x >= width:
        speed_x *= -1
    if y <= 0 or y >= height:
        speed_y *= -1

    # Відображаємо зображення на екрані
    screen.blit(image, (x, y))

    pygame.display.flip()  # Оновлюємо екран


py_quite()

