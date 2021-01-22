import pygame
# Наследует от класса Спрайт
class EnemyClass(pygame.sprite.Sprite):
    def __init__(self, enemy_x, enemy_speed,image_names, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_names
        # положение и размер спрайта
        self.rect = self.image.get_rect(center=(enemy_x,0))
        self.enemy_speed = enemy_speed
        self.add(group)
            
    
    def update(self, *args):
        if self.rect.y < args[0]:
            self.rect.y+= self.enemy_speed
        else:
            self.kill()


