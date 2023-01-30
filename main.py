import qrcode


def main():
    urlToMakeCode = input("Please copy and paste a website url that you would like converted to a QR code: ")

    img = qrcode.make(urlToMakeCode)
    type(img)

    ImageName = input("Now, please enter a name that the QR code will be saved as (will save as a png photo type): ")

    img.save(ImageName + ".png")

    if img:
        print("A QR code has been created! Check the curreny directory (checking purposes for now)")
        print("It has been saved as: " + ImageName + ".png \n")





if __name__ == "__main__":
    main()