import pygame

pygame.init()
w=600
h=600
bg = (0,0,0)
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Pong with wall')
run=True
rect1=pygame.Rect(0,0,25,25)
forward_speed=2
downward_speed=3
barspeed=5
count=0 #Later, if you hit 10 you won.
line=pygame.draw.line(screen,(255,255,255),(100,500),(200,500),2)
bar1=pygame.draw.rect(screen,(255,255,255),line,2)
#Gameloop
play=True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #Makes it stay inside the screen
    #Code is missing, couldnt get it working.
    
    screen.fill(bg)
    #Makes the cube move
    key=pygame.key.get_pressed()
    
    if play:
        rect1=pygame.Rect.move(rect1,forward_speed,downward_speed)
    # uncomment the bellow if statement for game over 
    if rect1.bottom>=h:
        play=False
    if rect1.right>=w or rect1.left<=0:
        forward_speed=-forward_speed
    if rect1.top<=0 or rect1.bottom>=h:
        downward_speed=-downward_speed
    if rect1.colliderect(bar1):
        downward_speed*=-1
    #Pongbar
    if key[pygame.K_RIGHT]==1 and bar1.right<w:
        bar1=pygame.Rect.move(bar1,barspeed,0)
    if key[pygame.K_LEFT]==1 and bar1.left>0:
        bar1=pygame.Rect.move(bar1,-barspeed,0)

    #Losing mechanism
    # if rect1.bottom>=h:
    #     forward_speed=0
    #     downward_speed=0
    #     print("You lost.")

    pygame.draw.rect(screen,(255,255,255),rect1)
    pygame.draw.rect(screen,(255,255,255),bar1)
    pygame.display.update()
pygame.quit()