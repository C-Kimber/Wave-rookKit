import pygame
from SpaceshipAdventure import SpaceshipAdventure

def main():
    pygame.font.init()
    c = SpaceshipAdventure(1200, 800, 60)
    c.main_loop()
    return
    
if __name__ == "__main__":
    main()

