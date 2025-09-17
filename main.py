import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidsField import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt=0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    Updatable = pygame.sprite.Group()
    Drawable = pygame.sprite.Group()
    Asteroids = pygame.sprite.Group()
    Player.containers= Updatable,Drawable
    Asteroid.containers= Updatable,Drawable, Asteroids
    AsteroidField.containers= Updatable
    Field=AsteroidField()
    player = Player(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT)/2)
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        Updatable.update(dt)
        for a in Asteroids:
            if player.check_collisions(a):
                print ("Game Over")
                pygame.quit()
                raise SystemExit
        for obj in Drawable:
            obj.draw(screen)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed/1000



if __name__ == "__main__":
    main()
