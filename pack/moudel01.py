import pygame
import os
screen_width,screen_height=700,600
# 方块类

class Block:
    def __init__(self, x, y, image, name):
        self.x = x
        self.y = y
        self.current_image = pygame.image.load(os.path.join('picture', image))
        self.name = name  # 存储方块的唯一名称
        self.rect = self.current_image.get_rect(topleft=(self.x, self.y))
        self.is_falling = False
        self.is_visible = False
        self.is_active = True

    def update(self):
        if self.is_falling:
            self.rect.y += 5

    def draw(self, surface):
        if self.is_visible:
            surface.blit(self.current_image, self.rect)

class BlockPool:
    def __init__(self, image_files):
        self.pool = {}  # 使用字典来存储方块，以名称为键
        self.image_files = image_files
        self.all_blocks = []

        # 创建并添加Block对象到池中，使用图像文件名作为名称（或者你可以使用其他唯一标识符）
        for i, image in enumerate(image_files):
            name = i
            block = Block(i * 100, 0, image_files[i],i)
            block.is_falling = False
            block.is_visible = False
            block.is_active = True
            self.pool[name] = block
        for i, image in enumerate(image_files):
            j = i+7
            name = j
            block = Block(i * 100, 0, image_files[i],j)
            block.is_falling = False
            block.is_visible = False
            block.is_active = True
            self.pool[name] = block
        for i, image in enumerate(image_files):
            k = i+14
            name = k
            block = Block(i * 100, 0, image_files[i],k)
            block.is_falling = False
            block.is_visible = False
            block.is_active = True
            self.pool[name] = block
        for i, image in enumerate(image_files):
            x = i+21
            name = x
            block = Block(i * 100, 0, image_files[i],x)
            block.is_falling = False
            block.is_visible = False
            block.is_active = True
            self.pool[name] = block

    def get_block(self, name):
        block = self.pool.get(name)
        block.is_falling = True
        block.is_visible = True
        self.all_blocks.append(block)
        return block

    def recycle_block(self, block):
        a = block.name
        b = a % 7
        del self.pool[a]
        block = Block(b * 100, 0, self.image_files[b], a)
        self.all_blocks.append(Block(b, 0, self.image_files[b], a))
        block.is_falling = False
        block.is_visible = False
        block.is_active = True
        self.pool[a] = block
        return block