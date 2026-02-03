import pygame

# 1. 初始化 Pygame
pygame.init()

# 2. 建立視窗
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("鍵盤控制的蛇")

# 3. 設定控制與變數
clock = pygame.time.Clock()

# 蛇的設定
snake_pos = [320, 240]        # 初始位置改為螢幕中間
snake_speed = 5
snake_size = 20
direction = [snake_speed, 0]  # 初始方向：向右移動 [x速度, y速度]

running = True
while running:
    # A. 事件處理 (偵測按鍵)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 偵測按下按鍵
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = [0, -snake_speed]
            elif event.key == pygame.K_DOWN:
                direction = [0, snake_speed]
            elif event.key == pygame.K_LEFT:
                direction = [-snake_speed, 0]
            elif event.key == pygame.K_RIGHT:
                direction = [snake_speed, 0]

    # B. 更新遊戲邏輯 (根據方向移動)
    snake_pos[0] += direction[0]
    snake_pos[1] += direction[1]
    
    # 邊界處理 (穿牆)
    if snake_pos[0] > 640: snake_pos[0] = 0
    if snake_pos[0] < 0:   snake_pos[0] = 640
    if snake_pos[1] > 480: snake_pos[1] = 0
    if snake_pos[1] < 0:   snake_pos[1] = 480

    # C. 繪圖
    screen.fill("black")
    pygame.draw.rect(screen, "green", (snake_pos[0], snake_pos[1], snake_size, snake_size))
    
    # D. 更新螢幕
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
