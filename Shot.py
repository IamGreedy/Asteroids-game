from circleshape import CircleShape
import pygame
from constants import *


class shot(CircleShape):
    def __init__(self,x,y,velocity):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = velocity
    
    def draw (self, surface):
        pygame.draw.circle(surface,"white",(int(self.position.x),int(self.position.y)),SHOT_RADIUS,2)
    
    def update (self, dt):
        self.position+=self.velocity*dt