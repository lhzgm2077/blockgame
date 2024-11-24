import pygame
import sys
from pack.moudel01 import BlockPool

# 初始化pygame
pygame.init()
# 初始化pygame的混音器
pygame.mixer.init()
# 加载MP3文件
pygame.mixer.music.load(r'sound\下载.mp3')
# 播放MP3文件


image_files = ['blue.png', 'green.png', 'orange.png', 'purple.png', 'qing.png', 'red.png', 'yellow.png']

# 设置屏幕大小
screen_width, screen_height = 700, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("下落方块")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

# 特定区间
x_range0 = (-1, 99)
x_range1 = (99, 199)
x_range2 = (199, 299)
x_range3 = (299, 399)
x_range4 = (399, 499)
x_range5 = (499, 599)
x_range6 = (599, 699)
y_range = (475, 575)
# 加载音频
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=4096)
audio_A = pygame.mixer.Sound(r'sound\C41.wav')
audio_W = pygame.mixer.Sound(r'sound\D41.wav')
audio_D = pygame.mixer.Sound(r'sound\E41.wav')
audio_SPACE = pygame.mixer.Sound(r'sound\F41.wav')
audio_J = pygame.mixer.Sound(r'sound\G41.wav')
audio_K = pygame.mixer.Sound(r'sound\A41.wav')
audio_L = pygame.mixer.Sound(r'sound\B41.wav')

# 创建方块池
blockPool = BlockPool(image_files)
print(enumerate(image_files))
print(blockPool)

# 游戏主循环
game_loop_counter = 0
running = True
clock = pygame.time.Clock()
while running:
    # 监控循环次数
    game_loop_counter = game_loop_counter+1
    print(game_loop_counter)
    if game_loop_counter == 12:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 62:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 122:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 182:
        blockPool.get_block(8).is_active = True
    if game_loop_counter == 242:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 302:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 362:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 422:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 482:
        blockPool.get_block(12).is_active = True
    if game_loop_counter == 542:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 602:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 662:
        blockPool.get_block(18).is_active = True
    if game_loop_counter == 722:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 782:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 842:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 902:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 962:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 1012:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 1062:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 1122:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 1182:
        blockPool.get_block(8).is_active = True
    if game_loop_counter == 1242:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 1302:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 1362:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 1422:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 1482:
        blockPool.get_block(12).is_active = True
    if game_loop_counter == 1542:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 1602:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 1662:
        blockPool.get_block(18).is_active = True
    if game_loop_counter == 1722:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 1782:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 1812:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 1832:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 1852:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 1892:
        blockPool.get_block(8).is_active = True
    if game_loop_counter == 1912:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 1932:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 1972:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 1992:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 2012:
        blockPool.get_block(12).is_active = True
    if game_loop_counter == 2092:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 2132:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 2152:
        blockPool.get_block(18).is_active = True
    if game_loop_counter == 2172:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 2212:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 2232:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 2252:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 2292:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 2312:
        blockPool.get_block(8).is_active = True
    if game_loop_counter == 2332:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 2452:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 2472:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 2492:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 2532:
        blockPool.get_block(8).is_active = True
    if game_loop_counter == 2552:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 2572:
        blockPool.get_block(15).is_active = True
    if game_loop_counter == 2612:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 2632:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 2652:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 2732:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 2772:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 2792:
        blockPool.get_block(18).is_active = True
    if game_loop_counter == 2812:
        blockPool.get_block(12).is_active = True
    if game_loop_counter == 2852:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 2872:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 2892:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 2932:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 2972:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 3092:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 3132:
        blockPool.get_block(14).is_active = True
    if game_loop_counter == 3172:
        blockPool.get_block(6).is_active = True
    if game_loop_counter == 3192:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 3212:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 3252:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 3272:
        blockPool.get_block(12).is_active = True
    if game_loop_counter == 3292:
        blockPool.get_block(13).is_active = True
    if game_loop_counter == 3372:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 3412:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 3432:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 3452:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 3492:
        blockPool.get_block(18).is_active = True
    if game_loop_counter == 3512:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 3532:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 3552:
        blockPool.get_block(13).is_active = True
    if game_loop_counter == 3572:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 3592:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 3612:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 3632:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 3732:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 3772:
        blockPool.get_block(6).is_active = True
    if game_loop_counter == 3812:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 3832:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 3852:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 3892:
        blockPool.get_block(12).is_active = True
    if game_loop_counter == 3912:
        blockPool.get_block(13).is_active = True
    if game_loop_counter == 3932:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 4012:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 4052:
        blockPool.get_block(18).is_active = True
    if game_loop_counter == 4072:
        blockPool.get_block(19).is_active = True
    if game_loop_counter == 4092:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 4132:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 4152:
        blockPool.get_block(25).is_active = True
    if game_loop_counter == 4172:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 4192:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 4212:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 4232:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 4252:
        blockPool.get_block(14).is_active = True
    if game_loop_counter == 4372:
        blockPool.get_block(8).is_active = True
    if game_loop_counter == 4392:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 4412:
        blockPool.get_block(21).is_active = True
    if game_loop_counter == 4532:
        blockPool.get_block(15).is_active = True
    if game_loop_counter == 4552:
        blockPool.get_block(9).is_active = True
    if game_loop_counter == 4572:
        blockPool.get_block(22).is_active = True
    if game_loop_counter == 4612:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 4632:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 4652:
        blockPool.get_block(16).is_active = True
    if game_loop_counter == 4692:
        blockPool.get_block(4).is_active = True
    if game_loop_counter == 4712:
        blockPool.get_block(5).is_active = True
    if game_loop_counter == 4732:
        blockPool.get_block(11).is_active = True
    if game_loop_counter == 4812:
        blockPool.get_block(7).is_active = True
    if game_loop_counter == 4852:
        blockPool.get_block(18).is_active = True
    if game_loop_counter == 4872:
        blockPool.get_block(12).is_active = True
    if game_loop_counter == 4892:
        blockPool.get_block(25).is_active = True
    if game_loop_counter == 4932:
        blockPool.get_block(2).is_active = True
    if game_loop_counter == 4952:
        blockPool.get_block(1).is_active = True
    if game_loop_counter == 4972:
        blockPool.get_block(0).is_active = True
    if game_loop_counter == 5012:
        blockPool.get_block(7).is_active = True

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                audio_A.play()  # 播放音频
                for block in blockPool.all_blocks:
                    if block.is_active and block.is_visible and x_range0[0] <= block.rect.x <= x_range0[1] and y_range[
                        0] <= block.rect.y <= y_range[1]:
                        block.is_falling = False
                        block.is_visible = False
                        block.is_active = False
            if event.key == pygame.K_w:
                audio_W.play()  # 播放音频
                for block in blockPool.all_blocks:
                    if block.is_active and block.is_visible and x_range1[0] <= block.rect.x < x_range1[1] and y_range[
                        0] <= block.rect.y <= y_range[1]:
                        block.is_falling = False
                        block.is_visible = False
                        block.is_active = False
            if event.key == pygame.K_d:
                audio_D.play()  # 播放音频
                for block in blockPool.all_blocks:
                    if block.is_active and block.is_visible and x_range2[0] <= block.rect.x < x_range2[1] and y_range[
                        0] <= block.rect.y <= y_range[1]:
                        block.is_falling = False
                        block.is_visible = False
                        block.is_active = False
            if event.key == pygame.K_SPACE:
                audio_SPACE.play()  # 播放音频
                for block in blockPool.all_blocks:
                    if block.is_active and block.is_visible and x_range3[0] <= block.rect.x < x_range3[1] and y_range[
                        0] <= block.rect.y <= y_range[1]:
                        block.is_falling = False
                        block.is_visible = False
                        block.is_active = False
            if event.key == pygame.K_j:
                audio_J.play()  # 播放音频
                for block in blockPool.all_blocks:
                    if block.is_active and block.is_visible and x_range4[0] <= block.rect.x < x_range4[1] and y_range[
                        0] <= block.rect.y <= y_range[1]:
                        block.is_falling = False
                        block.is_visible = False
                        block.is_active = False
            if event.key == pygame.K_k:
                audio_K.play()  # 播放音频
                for block in blockPool.all_blocks:
                    if block.is_active and block.is_visible and x_range5[0] <= block.rect.x < x_range5[1] and y_range[
                        0] <= block.rect.y <= y_range[1]:
                        block.is_falling = False
                        block.is_visible = False
                        block.is_active = False
            if event.key == pygame.K_l:
                audio_L.play()  # 播放音频
                for block in blockPool.all_blocks:
                    if block.is_active and block.is_visible and x_range6[0] <= block.rect.x < x_range6[1] and y_range[
                        0] <= block.rect.y <= y_range[1]:
                        block.is_falling = False
                        block.is_visible = False
                        block.is_active = False

    # 填充背景色
    screen.fill(WHITE)
    # 在y=535处画一条黑线
    pygame.draw.line(screen, BLACK, (0, 535), (700, 535), 1)
    # 在屏幕上显示游戏时间（这里只是示例，您可以根据需要自定义显示方式）
    font = pygame.font.SysFont('Arial', 20)
    text = font.render(f'Game Time: {int(game_loop_counter/64)} s', True, BLACK)
    screen.blit(text, (10, 10))
    # 回收方块并从活跃列表中移除，清空回收列表
    for block in blockPool.all_blocks:
        if block.is_visible and 0 <= block.rect.x <= 700 and 600 <= block.rect.y:
            block.is_active = False

    for block in blockPool.all_blocks:
        if not block.is_active:
            blockPool.recycle_block(block)

    # 更新方块位置
    for block in blockPool.all_blocks:
        block.update()
        block.draw(screen)
    pygame.display.flip()
    # 控制游戏速度
    clock.tick(64)

# 退出pygame
pygame.quit()
sys.exit()