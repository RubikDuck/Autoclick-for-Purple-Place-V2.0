import time
from pynput import mouse

mouseL_down = False
mouseL_up = False
mouseLD_x = 0
mouseLD_y = 0
mouseLU_x = 0
mouseLU_y = 0
mouse_button = ''
Ur_moves = {}
clicker_counter = 0

def mouse_move(x, y):
    print('Arrow XY: {0}'.format((x, y)))

def mouse_click(x, y, button, pressed):
    global mouseLD_x, mouseLD_y, mouseLU_x, mouseLU_y, mouseL_down, mouseL_up, mouse_button, clicker_counter

    mouse_button = str(button)
    print('Button:', button)
    if pressed:
        mouseL_down = True
        mouseLD_x, mouseLD_y = x, y
    else:
        mouseL_up = True
        mouseLU_x, mouseLU_y = x, y
        clicker_counter += 1

print('Press Ctrl-C to stop the clicker counter')

listener = mouse.Listener(on_click=mouse_click, on_move=mouse_move)
listener.start()

try:
    while True:
        if mouseL_down:
            clicker_counter += 1
            print('\nLoop: mouseL_down:', mouseLD_x, mouseLD_y, "clicker_counter:", clicker_counter)
            Ur_moves[clicker_counter] = mouse_button, 'mouseLD_xy', mouseLD_x, mouseLD_y
            mouseL_down = False

        if mouseL_up:
            print('\nLoop: mouseL_up:', mouseLU_x, mouseLU_y, "clicker_counter:", clicker_counter)
            Ur_moves[clicker_counter] = mouse_button, 'mouseLU_xy', mouseLU_x, mouseLU_y
            mouseL_up = False

except KeyboardInterrupt:
    listener.stop()
    listener.join()
    print("Ur moves:")
    print(Ur_moves)
    input('\nAfter copying the movements, close this program and start the second one.')
