import pygame

pygame.init()

#initialise the joystick module
pygame.joystick.init()

#define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Joysticks")

#define font
font_size = 30
font = pygame.font.SysFont("Futura", font_size)

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#create clock for setting game frame rate
clock = pygame.time.Clock()
FPS = 60

#create empty list to store joysticks
joysticks = []

#create player rectangle
x = 350
y = 200
player = pygame.Rect(x, y, 100, 100)

#define player colour
col = "royalblue"

#game loop
run = True
while run:

  clock.tick(FPS)

  #update background
  screen.fill(pygame.Color("midnightblue"))

  #draw player
  player.topleft = (x, y)
  pygame.draw.rect(screen, pygame.Color(col), player)

  #show number of connected joysticks
  draw_text("Controllers: " + str(pygame.joystick.get_count()), font, pygame.Color("azure"), 10, 10)
  for joystick in joysticks:
    draw_text("Battery Level: " + str(joystick.get_power_level()), font, pygame.Color("azure"), 10, 35)
    draw_text("Controller Type: " + str(joystick.get_name()), font, pygame.Color("azure"), 10, 60)
    draw_text("Number of axes: " + str(joystick.get_numaxes()), font, pygame.Color("azure"), 10, 85)

  for joystick in joysticks:
    #change player colour with buttons
    if joystick.get_button(0):
      col = "royalblue"
    if joystick.get_button(1):
      col = "crimson"
    if joystick.get_button(2):
      col = "fuchsia"
    if joystick.get_button(3):
      col = "forestgreen"
    i=0
    k=[]
    while 1:
        try: k.append(joystick.get_hat(i))
        except: break
        i+=1
    print(k)
    
    #player movement with joystick
    if joystick.get_button(14):
      x += 5
    if joystick.get_button(13):
      x -= 5
    if joystick.get_button(11):
      y -= 5
    if joystick.get_button(12):
      y += 5

    #player movement with analogue sticks
    horiz_move = joystick.get_axis(0)
    vert_move = joystick.get_axis(1)

    if abs(vert_move) > 0.1:
      y += vert_move * 5
    if abs(horiz_move) > 0.1:
      x += horiz_move * 5
    

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.JOYDEVICEADDED:
      joy = pygame.joystick.Joystick(event.device_index)
      joysticks.append(joy)
    #quit program
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()



# import pygame as pg
# from pygame.math import Vector2


# def main():
#     pg.init()
#     screen = pg.display.set_mode((640, 480))
#     clock = pg.time.Clock()
#     player_img = pg.Surface((42, 70), pg.SRCALPHA)
#     pg.draw.polygon(player_img, pg.Color('dodgerblue1'),
#                     [(0, 70), (21, 2), (42, 70)])
#     player_rect = player_img.get_rect(center=screen.get_rect().center)

#     joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
#     for joystick in joysticks:
#         joystick.init()

#     while True:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 return

#         if len(joysticks) > 0:  # At least one joystick.
#             # Use the stick axes to create a vector.
#             vec = Vector2(joysticks[0].get_axis(0), joysticks[0].get_axis(1))
#             radius, angle = vec.as_polar()  # angle is between -180 and 180.
#             # Map the angle that as_polar returns to 0-360 with 0 pointing up.
#             adjusted_angle = (angle+90) % 360
#             pg.display.set_caption(
#                 'radius {:.2f} angle {:.2f} adjusted angle {:.2f}'.format(
#                     radius, angle, adjusted_angle))

#         # Rotate the image and get a new rect.
#         player_rotated = pg.transform.rotozoom(player_img, -adjusted_angle, 1)
#         player_rect = player_rotated.get_rect(center=player_rect.center)

#         screen.fill((30, 30, 30))
#         screen.blit(player_rotated, player_rect)
#         pg.display.flip()
#         clock.tick(60)


# if __name__ == '__main__':
#     main()
#     pg.quit()