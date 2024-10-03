import pico2d
import random
import math

pico2d.open_canvas()

background = pico2d.load_image('C:/Users/Creator/Documents/2DGP/2019180040_Drill_06/TUK_GROUND.png')
animation_sheet = pico2d.load_image('C:/Users/Creator/Documents/2DGP/2019180040_Drill_06/animation_sheet.png')
hand_image = pico2d.load_image('C:/Users/Creator/Documents/2DGP/2019180040_Drill_06/hand_arrow.png')

character_x, character_y = pico2d.get_canvas_width() // 2, pico2d.get_canvas_height() // 2
hand_x, hand_y = random.randint(100, 700), random.randint(100, 500)
frame = 0
direction = 1
speed = 2.5
running = True

while running:
    pico2d.clear_canvas()

    background.draw(pico2d.get_canvas_width() // 2, pico2d.get_canvas_height() // 2)

    dx, dy = hand_x - character_x, hand_y - character_y
    distance = math.sqrt(dx**2 + dy**2)

    if distance > 0:
        move_x = (dx / distance) * speed
        move_y = (dy / distance) * speed
        character_x += move_x
        character_y += move_y

        direction = 1 if dx > 0 else -1

    frame = (frame + 0.5) % 8

    if direction == 1:
        animation_sheet.clip_draw(int(frame) * 100, 100, 100, 100, character_x, character_y)
    else:
        animation_sheet.clip_draw(int(frame) * 100, 0, 100, 100, character_x, character_y)

    hand_image.draw(hand_x, hand_y)

    if distance < speed:
        hand_x, hand_y = random.randint(100, 700), random.randint(100, 500)

    pico2d.update_canvas()
    pico2d.delay(0.02)

    # 이벤트 처리 (ESC 키를 누르면 종료)
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            running = False
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False

pico2d.close_canvas()
