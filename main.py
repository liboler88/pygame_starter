import pygame

# 1. 初始化
pygame.init()

# 2. 建立視窗
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("最簡單的 Pygame")

# 3. 遊戲迴圈
running = True
while running:
    # 處理事件 (例如點擊關閉按鈕)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. 畫東西 (填滿藍色)
    screen.fill("blue")
    
    # 更新畫面
    pygame.display.flip()

# 5. 結束
pygame.quit()
