import qrcode

from pathlib import Path
import os

def main():
    urlToMakeCode = input("Please copy and paste a website url that you would like converted to a QR code: ")

    img = qrcode.make(urlToMakeCode)
    type(img)

    imageName = input("Now, please enter a name that the QR code will be saved as (will save as a png photo type): ")
    imageNameWithType = imageName + ".png"

    img.save(imageNameWithType)

    if img:
        print("A QR code has been created! Check the current directory (checking purposes for now)")
        print("It has been saved as: " + imageName + ".png \n")

    # NOT SURE IF WHAT'S BELOW WILL WORK FOR NON-LINUX LIKE WINDOWS (cuz this works for linux based like Mac)
    # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
    saveInDownloads = input("Would you like this QR code saved to your downloads folder? ('Y' for yes, 'N' for no): ")
    if saveInDownloads == "Y":
        # https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
        path = str(os.path.join(Path.home(), "Downloads", imageNameWithType))
        # https://stackoverflow.com/questions/31434278/how-do-i-use-python-pil-to-save-an-image-to-a-particular-directory
        img.save(path, "PNG")







if __name__ == "__main__":
    main()