from tkinter import Tk, Frame, Button
from PIL import Image, ImageTk

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


# Size of map (so how many rooms to click there are)
sizeOfMap = 20


def load_image(file_path):
    pil_image = Image.open(file_path).resize((zoomAmountX, zoomAmountY))
    return ImageTk.PhotoImage(pil_image)


Default_Icon = load_image("greySquareIcon.png")
# Default room icon with nothing special
Treasure_Room_Icon = load_image("Treasure_Room_Icon.png")
Arcade_Icon = load_image("Arcade_Icon.png")
Boss_Challenge_Room_Icon = load_image("Boss_Challenge_Room_Icon.png")
Boss_Room_Icon = load_image("Boss_Room_Icon.png")
Challenge_Room_Icon = load_image("Challenge_Room_Icon.png")
Curse_Room_Icon = load_image("Curse_Room_Icon.png")
Dice_Room_Icon = load_image("Dice_Room_Icon.png")
Library_Icon = load_image("Library_Icon.png")
Sacrifice_Room_Icon = load_image("Sacrifice_Room_Icon.png")
Shop_Icon = load_image("Shop_Icon.png")
Vault_Icon = load_image("Vault_Icon.png")
Nothing_Icon = load_image("Nothing_Icon.png")
Secret_Room_Icon = load_image("Secret_Room_Icon.png")
Super_Secret_Room_Icon = load_image("Super_Secret_Room_Icon.png")
roomIcons = [
    (Nothing_Icon, "n"),
    (Default_Icon, "d"),
    (Treasure_Room_Icon, "tr"),
    (Shop_Icon, "shop"),
    (Curse_Room_Icon, "cur"),
    (Arcade_Icon, "a"),
    (Boss_Challenge_Room_Icon, "bcr"),
    (Boss_Room_Icon, "br"),
    (Challenge_Room_Icon, "cr"),
    (Dice_Room_Icon, "dr"),
    (Library_Icon, "lib"),
    (Sacrifice_Room_Icon, "sr"),
    (Vault_Icon, "v"),
    (Secret_Room_Icon, "sec"),
    (Super_Secret_Room_Icon, "supsec"),
]


def changeRoom(b):
    # print(f"clicked {i}")
    currentImageAcro = b.cget("text")
    currentIndex = next(
        (
            index
            for index, (icon, acro) in enumerate(roomIcons)
            if acro == currentImageAcro
        ),
        None,
    )

    if currentIndex is not None:
        newIndex = (currentIndex + 1) % len(roomIcons)
        newImage, newAcro = roomIcons[newIndex]
        b.configure(image=newImage, text=newAcro)


def resetRoom(b):
    newIndex = 0
    newImage, newAcro = roomIcons[newIndex]
    b.configure(image=newImage, text=newAcro)

def resetAllRooms(b):
    for row in range(sizeOfMap):
        for col in range(sizeOfMap):
            button = btns_frame.grid_slaves(row=row + 1, column=col)[0]
            resetRoom(button)

for row in range(sizeOfMap):
    for col in range(sizeOfMap):
        b = Button(
            btns_frame,
            text="n",
            image=Nothing_Icon,
        )
        b.bind("<Button-1>", lambda event, b=b: changeRoom(b)) # Left click changes room type
        b.bind("<Button-2>", resetAllRooms) # Middle click resets all rooms (new level)
        b.bind("<Button-3>", lambda event, b=b: resetRoom(b)) # Right click resets specific button
        b.grid(row=row + 1, column=col)


def runTest():
    """
    This is the function which will pass through and denote all rooms which could be a secret room or super secret room
    """
    xSize, ySize = btns_frame.grid_size()
    secretRooms = (
        []
    )  # List of all secret rooms, done so that identification of one secret room does not affect another (such as making it think it is connected to 2 rooms when 1 room is a possible secret room)
    superSecretRooms = []
    for row in range(xSize):
        if row == 0 or row == 1 or row == xSize - 1:
            continue
        for col in range(ySize):
            if col == 0 or col == ySize - 1 or col == ySize - 2:
                continue
            try:
                button = btns_frame.grid_slaves(row=row, column=col)[0]
                buttonAbove = btns_frame.grid_slaves(row=row - 1, column=col)[0]
                buttonBelow = btns_frame.grid_slaves(row=row + 1, column=col)[0]
                buttonLeft = btns_frame.grid_slaves(row=row, column=col - 1)[0]
                buttonRight = btns_frame.grid_slaves(row=row, column=col + 1)[0]

                if button.cget("text") != "n":
                    # If already defined with room
                    continue

                textOfSurroundings = [
                    buttonAbove.cget("text"),
                    buttonBelow.cget("text"),
                    buttonLeft.cget("text"),
                    buttonRight.cget("text"),
                ]
                if "br" in textOfSurroundings:
                    # Can't be connected to a boss room
                    continue

                if textOfSurroundings.count("n") == 3 or (
                    textOfSurroundings.count("sec") == 1
                    and textOfSurroundings.count("n") == 2
                ):
                    # check if can be super secret
                    if textOfSurroundings.count("d") == 1:
                        # must be only connected to default room
                        print("SUPER SECRET ROOM IS " + str(row) + "," + str(col))
                        superSecretRooms.append((row, col))
                        continue
                    # If only connected by 1 room or 0 rooms
                    continue
                if textOfSurroundings.count("n") == 4:
                    # If surrounded by non selected rooms, then no room
                    continue

                if textOfSurroundings.count("n") >= 3:
                    continue
                    # If connected to 2 rooms, then it is a secret room

                print("SECRET ROOM IS " + str(row) + "," + str(col))
                secretRooms.append((row, col))

            except:
                print("error")
                continue

    for room in secretRooms:
        btns_frame.grid_slaves(row=room[0], column=room[1])[0].configure(
            image=Secret_Room_Icon, text="sec"
        )

    for room in superSecretRooms:
        btns_frame.grid_slaves(row=room[0], column=room[1])[0].configure(
            image=Super_Secret_Room_Icon, text="supsec"
        )


b = Button(btns_frame, text="Test for Secret Rooms", command=runTest)

b.grid(row=sizeOfMap, column=sizeOfMap)

root.mainloop()
