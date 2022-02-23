import pygame

# initializing pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((800, 600))
# Set title and icon
pygame.display.set_caption("Button")
icon = pygame.image.load('data/ufo.png')
pygame.display.set_icon(icon)

# Load button images  -->
start_img = pygame.image.load('data/start_btn1.png').convert_alpha()
exit_img = pygame.image.load('data/exit_btn1.png').convert_alpha()


# Creating button class
class Button():
    def __init__(self, x, y, image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked=False

    def draw(self,surface,show=True):
        if show :
            action=False
            # Getting Mouse Position
            pos=pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                    # print('clciked')
                    self.clicked=True
                    action=True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            # Draw buttons on screen
            surface.blit(self.image,(self.rect.x, self.rect.y))
            return action


if __name__ == '__main__':
    # Create button instances
    start_btn = Button(100, 200, start_img, 0.4)
    exit_btn = Button(450, 200, exit_img, 0.4)
    running = True
    while running:
        screen.fill((128, 0, 0))
        if start_btn.draw(screen):
            print('Start pressed')
        if exit_btn.draw(screen):
            running=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()