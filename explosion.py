import pygame
from circleshape import CircleShape
from constants import *

class Explosion (CircleShape):
    containers =()

    def __init__(self,x,y):
        super().__init__(x,y,radius=1)
        self.age=0.0
        self.lifetime = EXPLOSION_LIFETIME
        self.max_radius = EXPLOSION_MAX_RADIUS
        self.alpha = EXPLOSION_ALPHA

    def update (self,dt):
        self.age+=dt
        t=self.age/self.lifetime
        if t>=1.0:
            self.kill()
            return
        self.radius=int(self.max_radius*t)
        self.alpha=int(255*(1-t))

    def draw(self,screen):
        size=self.radius*2+6
        surf=pygame.Surface((size,size),pygame.SRCALPHA)
        center=(size//2,size//2)

    # disque jaune
        pygame.draw.circle(surf, (255, 200, 50, self.alpha), center, self.radius)
    # anneau orange
        pygame.draw.circle(surf, (255, 120, 0, self.alpha), center, max(2, self.radius // 2), width=3)
    # affiche au centre de l'explosion
        screen.blit(surf, (self.position.x - size // 2, self.position.y - size // 2))
