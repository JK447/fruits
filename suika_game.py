import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ゲームウィンドウの設定
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("フルーツ落としゲーム")

# 色の設定
WHITE = (255, 255, 255)
FRUIT_COLORS = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]

# フルーツクラス
class Fruit(pygame.sprite.Sprite):
    def __init__(self, color, size, position):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self.size = size
        self.falling = True  # 落下中かどうかを示すフラグ

# フルーツグループ
fruit_group = pygame.sprite.Group()

# フルーツを生成してグループに追加する関数
def create_fruit(x, y):
    size = random.randint(20, 50)
    color = random.choice(FRUIT_COLORS)
    fruit = Fruit(color, size, (x, y - size))
    fruit_group.add(fruit)

# フルーツの落下とマージを行う関数
def update_fruits():
    for fruit in fruit_group:
        if fruit.falling:  # 落下中のフルーツのみ動かす
            fruit.rect.y += 5
            if fruit.rect.bottom >= SCREEN_HEIGHT:
                fruit.rect.bottom = SCREEN_HEIGHT
                fruit.falling = False  # 着地したので落下フラグをFalseに
        # 他のフルーツとの衝突を確認してマージする処理はここに追加

# ゲームループ
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # マウスをクリックした位置にフルーツを生成
            x, y = pygame.mouse.get_pos()
            create_fruit(x, y)

    update_fruits()  # フルーツの状態を更新
    fruit_group.draw(screen)  # フルーツを画面に描画
    pygame.display.flip()  # 画面を更新
    pygame.time.Clock().tick(30)  # 30FPSに設定
