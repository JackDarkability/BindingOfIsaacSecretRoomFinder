from PIL import Image, ImageTk


def load_image(file_path, zoomAmountX=50, zoomAmountY=50):
    pil_image = Image.open(file_path).resize((zoomAmountX, zoomAmountY))
    return ImageTk.PhotoImage(pil_image)


def getImages(zoomX, zoomY):
    Default_Icon = load_image("greySquareIcon.png", zoomX, zoomY)
    # Default room icon with nothing special
    Treasure_Room_Icon = load_image("Treasure_Room_Icon.png", zoomX, zoomY)
    Arcade_Icon = load_image("Arcade_Icon.png", zoomX, zoomY)
    Boss_Challenge_Room_Icon = load_image("Boss_Challenge_Room_Icon.png", zoomX, zoomY)
    Boss_Room_Icon = load_image("Boss_Room_Icon.png", zoomX, zoomY)
    Challenge_Room_Icon = load_image("Challenge_Room_Icon.png", zoomX, zoomY)
    Curse_Room_Icon = load_image("Curse_Room_Icon.png", zoomX, zoomY)
    Dice_Room_Icon = load_image("Dice_Room_Icon.png", zoomX, zoomY)
    Library_Icon = load_image("Library_Icon.png", zoomX, zoomY)
    Sacrifice_Room_Icon = load_image("Sacrifice_Room_Icon.png", zoomX, zoomY)
    Shop_Icon = load_image("Shop_Icon.png", zoomX, zoomY)
    Vault_Icon = load_image("Vault_Icon.png", zoomX, zoomY)
    Nothing_Icon = load_image("Nothing_Icon.png", zoomX, zoomY)
    Secret_Room_Icon = load_image("Secret_Room_Icon.png", zoomX, zoomY)
    Super_Secret_Room_Icon = load_image("Super_Secret_Room_Icon.png", zoomX, zoomY)
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

    return roomIcons
