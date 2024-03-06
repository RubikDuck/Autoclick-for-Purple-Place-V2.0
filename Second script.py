import pyautogui
import tkinter as tk
import time
import threading

stop_execution = False

def repeat_events(Ur_moves, num_repeats):
    global stop_execution

    for _ in range(num_repeats):
        if stop_execution:
            break

        for key, item in Ur_moves.items():
            The_click, The_action, x, y = item

            if The_click == 'Button.left':
                if The_action == 'mouseLD_xy':
                    print("left_down", x, y)
                    pyautogui.mouseDown(x=x, y=y)
                elif The_action == 'mouseLU_xy':
                    print("LEFT_UP", x, y)
                    pyautogui.mouseUp(x=x, y=y)

            elif The_click == 'Button.right':
                if The_action == 'mouseLD_xy':
                    print("right_down", x, y)
                    pyautogui.mouseDown(button='right', x=x, y=y)
                elif The_action == 'mouseLU_xy':
                    print("RIGHT_UP", x, y)
                    pyautogui.mouseUp(button='right', x=x, y=y)

            time.sleep(1)

def start_execution():
    global stop_execution
    stop_execution = False

    Ur_moves_str = events_text.get("1.0", tk.END)
    num_repeats = int(repeat_var.get())
    Ur_moves = eval(Ur_moves_str)

    execution_thread = threading.Thread(target=repeat_events, args=(Ur_moves, num_repeats))
    execution_thread.start()

def stop_execution():
    global stop_execution
    stop_execution = True

root = tk.Tk()
root.title("Ur moves")

frame = tk.Frame(root)
frame.pack(pady=10)

label_events = tk.Label(frame, text="Paste Ur moves!")
label_events.grid(row=0, column=0, columnspan=2)

events_text = tk.Text(frame, height=10, width=50)
events_text.grid(row=1, column=0, columnspan=2)

label_repeat = tk.Label(frame, text="Number of loops:")
label_repeat.grid(row=2, column=0, sticky='e')

repeat_var = tk.StringVar()
entry_repeat = tk.Entry(frame, textvariable=repeat_var)
entry_repeat.grid(row=2, column=1, sticky='w')

start_button = tk.Button(frame, text="Start", command=start_execution)
start_button.grid(row=3, column=0)

stop_button = tk.Button(frame, text="Stop", command=stop_execution)
stop_button.grid(row=3, column=1)

root.mainloop()