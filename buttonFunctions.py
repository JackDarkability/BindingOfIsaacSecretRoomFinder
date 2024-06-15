def changeRoom(b, roomIcons):
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


def resetRoom(b, roomIcons):
    newIndex = 0
    newImage, newAcro = roomIcons[newIndex]
    b.configure(image=newImage, text=newAcro)


def resetAllRooms(b, sizeOfMap, btns_frame, roomIcons):
    for row in range(sizeOfMap):
        for col in range(sizeOfMap):
            button = btns_frame.grid_slaves(row=row + 1, column=col)[0]
            resetRoom(button, roomIcons)


def runTest(btns_frame, roomIcons):
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
            image=roomIcons[-2][0], text="sec"
        )

    for room in superSecretRooms:
        btns_frame.grid_slaves(row=room[0], column=room[1])[0].configure(
            image=roomIcons[-1][0], text="supsec"
        )
