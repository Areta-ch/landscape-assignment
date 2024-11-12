import pygame

pygame.init()

WIDTH = 780
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#variables
cloud_x = 500
cloud_x2 = 300
cloud_x3 = 100
sun_y = 70
moon_y = 750  
sunset_pt = 330
star_radius = 3
star_color = (255, 255, 255)
bird1 = 60
bird2 = 780
day_color = (200, 228, 255)  
night_color = (21, 21, 36) 
sky_color = day_color  
star1 = (330, 50)
star2 = (700, 40)
star3 = (550, 90)
star4 = (200, 150)
star5 = (100, 50)
star6 = (650, 180)
star7 = (480, 180)
sky_red = 200
sky_green = 228
sky_blue = 255
fcount = 0
stars_show = False  

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fcount += 1

    if fcount >= 120:
        stars_show = True

    cloud_x += 3
    cloud_x2 -= 3
    cloud_x3 += 4
    sun_y += 2
    bird1 += 3.8
    bird2 += -4
    
    if moon_y > 80:
        moon_y -= 3
    else:
        moon_y = 80 

    if moon_y < 330: 
        stars_show = True
    else:
        stars_show = False

    if sky_red > 0:
        sky_red -= 1
    if sky_green > 0:
        sky_green -= 1
    if sky_blue > 0 :       
        sky_blue -= 1

    screen.fill((sky_red, sky_green, sky_blue))
    if stars_show:
        count = 1

        while count <= 7:
            if count == 1:
                pygame.draw.circle(screen, star_color, star1, star_radius)
            elif count == 2:
                pygame.draw.circle(screen, star_color, star2, star_radius)
            elif count == 3:
                pygame.draw.circle(screen, star_color, star3, star_radius)
            elif count == 4:
                pygame.draw.circle(screen, star_color, star4, star_radius)
            elif count == 5:
                pygame.draw.circle(screen, star_color, star5, star_radius)
            elif count ==6:
                pygame.draw.circle(screen, star_color, star6, star_radius)
            elif count == 7:
                pygame.draw.circle(screen, star_color, star7, star_radius)
  

            count += 1  

    pygame.draw.circle(screen, (253, 253, 150), (80, sun_y), 60)  # Sun
    pygame.draw.circle(screen, (255, 255, 255), (80, moon_y), 60)  # Moon

    #mountains
    pygame.draw.polygon(screen, (230, 190, 255), [(520 + 70, 440 + 80), (695 + 70, 60 + 40), (863 + 105, 400 + 140)])
    pygame.draw.polygon(screen, (140, 183, 255), [(100, 500), (320, 115), (600, 500)])
    pygame.draw.polygon(screen, (230, 183, 255), [(50, 500), (320, 115), (460, 500)])
    pygame.draw.polygon(screen, (200, 240, 255), [(390, 440 + 80), (495 + 70, 160 + 40), (703 + 105, 540)])
    pygame.draw.polygon(screen, (134, 204, 218), [(680, 440 + 80), (495 + 70, 160 + 40), (703 + 105, 540)])
    pygame.draw.polygon(screen, (140, 160, 255), [(-220, 480), (40, 200), (380, 580)])
    pygame.draw.polygon(screen, (160, 244, 230), [(-60 + 70, 440 + 80), (125 + 70, 160 + 80), (300 + 70, 440 + 80)])
    pygame.draw.polygon(screen, (134, 134, 218), [(-60 + 150, 440 + 80), (125 + 70, 160 + 80), (300 + 150, 440 + 80)])
    pygame.draw.polygon(screen, (134, 134, 218), [(208 + 70, 440 + 80), (375 + 70, 200 + 80), (533 + 105, 400 + 140)])
    pygame.draw.polygon(screen, (134, 204, 218), [(208, 440 + 80), (375 + 70, 200 + 80), (533, 400 + 140)])


    #clouds
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x - 17, 175), 45)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 25, 150), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 50, 180), 40)

    pygame.draw.circle(screen, (255, 255, 255), (cloud_x2 - 25, 76), 38)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x2, 50), 32)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x2 + 20, 84), 38)

    pygame.draw.circle(screen, (255, 255, 255), (cloud_x3 - 20, 200), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x3 + 10, 185), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x3 + 28, 200), 35)

    #birds
    pygame.draw.arc(screen, (0, 0, 0), (bird1, 40, 35, 30), 0, 2.7, 2) 
    pygame.draw.arc(screen, (0, 0, 0), (bird1 + 35, 40, 35, 30), 0, 3.2, 2) 


    pygame.draw.arc(screen, (0, 0, 0), (bird2 - 95 - 35, 70, 35, 30), 0, 3.14, 2)  
    pygame.draw.arc(screen, (0, 0, 0), (bird2 - 60 - 35, 70, 35, 30), 0, 3.14, 2) 



    pygame.display.flip() 
    clock.tick(30)  

pygame.quit()