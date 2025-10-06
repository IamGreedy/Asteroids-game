import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidsField import AsteroidField
from Shot import shot
from circleshape import CircleShape
from scoring import Score
from explosion import Explosion

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
    Shots = pygame.sprite.Group()

    Player.containers= Updatable,Drawable
    Asteroid.containers= Updatable,Drawable, Asteroids
    AsteroidField.containers= Updatable
    shot.containers= Updatable, Drawable, Shots
    Explosion.containers = Updatable, Drawable


    Field=AsteroidField()
    score = Score()

    player = Player(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT)/2)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        Updatable.update(dt)

        for a in Asteroids:
            if player.check_collisions(a):
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", True, (255, 0, 0))
                text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                screen.blit(text, text_rect)

                small = pygame.font.Font(None, 36)
                final_text = small.render(f"Score: {score.value}", True, (255, 255, 255))
                final_rect = final_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 60))
                screen.blit(final_text, final_rect)

                score.save_highscore()
                pygame.display.flip()
                pygame.time.wait(2000)
                print ("Game Over")
                pygame.quit()
                raise SystemExit

            for s in Shots:
                if a.check_collisions(s):
                    Explosion(a.position.x, a.position.y)
                    a.split()
                    s.kill()
                    score.add_points(100)

        for obj in Drawable:
            obj.draw(screen)

        score.draw(screen)
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed/1000



if __name__ == "__main__":
    main()
