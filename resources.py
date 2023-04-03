import pyglet


def img_source(image):
    img = pyglet.resource.image('' + image)
    return img

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

pyglet.resource.path = ['game/resources']
pyglet.resource.reindex()
main_batch = pyglet.graphics.Batch()
wall_batch = pyglet.graphics.Batch()

main_character_image = img_source('cat1.png')
center_image(main_character_image)
    
walls_top = [img_source('w1.png'), img_source('w2.png'), img_source('w3.png'), img_source('w4.png'), img_source('w5.png'), img_source('w6.png')]
walls_bot = [img_source('wb1.png'), img_source('wb2.png'), img_source('wb3.png'), img_source('wb4.png'), img_source('wb5.png'), img_source('wb6.png')]
walls_left = [img_source('wl1.png'), img_source('wl2.png'), img_source('wl3.png'), img_source('wl4.png')]
walls_right = [img_source('wr1.png'), img_source('wr2.png'), img_source('wr3.png'), img_source('wr4.png')]

wall_list = []

for wall in wall_list:
    center_image(wall)

