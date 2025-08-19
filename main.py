import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots,drawable,updatable)
    asteroidfield = AsteroidField()

    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for item in asteroids:
            if item.collision(player):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                if item.collision(shot):
                    shot.kill()
                
                    item.split()
                    
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        
        # player.draw(screen=screen)
        # player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
