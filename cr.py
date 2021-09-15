import pygame as pg

pg.init()

window = pg.display.set_mode((800, 600))

while True:
    event = pg.event.poll()
    if event.type == pg.QUIT:
        break
    pg.mouse.set_visible(False)
    window.fill((0,0,0))
    window.blit(pg.image.load("images/cursor.png"), pg.mouse.get_pos())
    pg.display.update()

pg.quit()