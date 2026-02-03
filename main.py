import pygame
import sys

def main():
    # 初始化 Pygame
    pygame.init()
    
    # 設定視窗大小與標題
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Starter - Premium Design")
    
    clock = pygame.time.Clock()
    
    # 基本顏色設定
    BG_COLOR = (15, 15, 20)  # 深色背景 (接近黑色，稍微帶藍)
    ACCENT_COLOR = (0, 255, 150) # 翡翠綠
    
    running = True
    angle = 0
    
    while running:
        # 事件處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # 繪製邏輯
        screen.fill(BG_COLOR)
        
        # 畫一個會旋轉的正方形展示效果
        rect_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, ACCENT_COLOR, (0, 0, 100, 100), border_radius=15)
        
        rotated_surface = pygame.transform.rotate(rect_surface, angle)
        rect = rotated_surface.get_rect(center=(400, 300))
        
        screen.blit(rotated_surface, rect.topleft)
        
        angle = (angle + 2) % 360
        
        # 更新顯示
        pygame.display.flip()
        
        # 控制幀率 (60 FPS)
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
