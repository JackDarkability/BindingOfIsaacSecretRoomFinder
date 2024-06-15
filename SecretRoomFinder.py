from tkinter import Tk, Frame, Button
from PIL import Image, ImageTk
from bindingOfIsaacImages import getImages
from buttonFunctions import changeRoom, resetAllRooms, resetRoom, runTest

"""
This is a program which will allow you to find secret and super secret rooms in the Binding of Isaac game
It will allow you to click on rooms to denote what type of room it is, and then it will find all possible secret and super secret rooms
For rooms that span more than a 1x1 area, just select all the respective squares as regular rooms and it will work.

The program does not work with rooms on the border of the selectable area as it can not know what is beyond the border, 
so select a size of map which is larger than the actual map size to allow for the map to be contained and diagrammed completely.



Super Secret Rooms are most likely to be found either at the end of a series of rooms that lead to a dead-end, 
and are particularly likely to appear near the Boss Room, as they are the second room type to be placed on a map during Map Generation, 
and are therefore placed far away from the room Isaac starts in. Because Shops are the third type of room generated, 
super secret rooms are also likely to spawn near the shop, and are likely to spawn in between the shop and the Boss Room.

- https://bindingofisaacrebirth.fandom.com/wiki/Secret_Room

Copyright for all games images goes to the Binding of Isaac and Edmund McMillen, I do not own any of the images used in this program
The program is made as is and is not guaranteed to be accurate 
(for example when there is no suitable position to be connected to more than one room, 
the game will put it connected to only one room, this is not represented in the program), 
but should be a good guide to finding secret rooms in the game

© 2024 Jack Newton
"""

root = Tk()
root.title(string="Binding Of Isaac Secret Room Finder")
# Layout for map
btns_frame = Frame(root)
btns_frame.pack()

# Load images, zoom size as they are only 8x8 as taken from the binding of isaac wiki
zoomAmountX = 50
zoomAmountY = 50
roomIcons = getImages(zoomAmountX, zoomAmountY)

# Size of map (so how many rooms to click there are)
sizeOfMap = 20

for row in range(sizeOfMap):
    for col in range(sizeOfMap):
        b = Button(
            btns_frame,
            text="n",
            image=roomIcons[0][0],
        )
        b.bind(
            "<Button-1>", lambda event, b=b: changeRoom(b, roomIcons)
        )  # Left click changes room type
        b.bind(
            "<Button-2>",
            lambda event, b=b: resetAllRooms(b, sizeOfMap, btns_frame, roomIcons),
        )  # Middle click resets all rooms (new level)
        b.bind(
            "<Button-3>", lambda event, b=b: resetRoom(b, roomIcons)
        )  # Right click resets specific button
        b.grid(row=row + 1, column=col)

b = Button(
    btns_frame,
    text="Test for Secret Rooms",
    command=lambda: runTest(btns_frame, roomIcons),
)

b.grid(row=sizeOfMap, column=sizeOfMap)

root.mainloop()
