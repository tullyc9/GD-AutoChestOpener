import time
from pynput.mouse import Controller, Button
mouse = Controller()
print("GD Auto Chest Opener\n"
      "    By TullyYT\n"
      "--------------------")
x = input("How Many Pages Of Chests Would You Like To Open?")
x=int(x)
i=0

while i <= x:
    def open_chest_at_pos(x,y):
        mouse.position = (x,y)
        mouse.click(Button.left)
        time.sleep(1)
        mouse.position = (765,715)
        time.sleep(3)
        mouse.click(Button.left)

    open_chest_at_pos(415, 290)
    open_chest_at_pos(665, 290)
    open_chest_at_pos(915, 290)
    open_chest_at_pos(1165, 290)
    open_chest_at_pos(415, 540)
    open_chest_at_pos(665, 540)
    open_chest_at_pos(915, 540)
    open_chest_at_pos(1165, 540)
    open_chest_at_pos(415, 720)
    open_chest_at_pos(665, 720)
    open_chest_at_pos(915, 720)
    open_chest_at_pos(1165, 720)
    input("Press Enter To Go To The Next Page")
    open_chest_at_pos(1915, 290) # DO NOT DELETE THIS LINE! IT MAKES YOU GOT TO THE NEXT PAGE!
    i += 1



