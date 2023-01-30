import qrcode

from pathlib import Path
import os

from flask import Flask, render_template, request
import io
import base64
from PIL import Image
import shutil

app = Flask(__name__)

@app.route("/")
def home():
    start = True
    return render_template("index.html", start=start)


@app.route("/", methods=['POST'])
def createOrSaveQR():
    if request.method == "POST":
        if 'url' in request.form:
            # https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
            url = request.form['url']
            img = qrcode.make(url)
            type(img)
            img.save("qrCode.png")

            # https://buraksenol.medium.com/pass-images-to-html-without-saving-them-as-files-using-python-flask-b055f29908a
            # was trying something earlier w/o saving to static folder but ehhh ...
            # data = io.BytesIO()
            # img.save(data, "PNG")
            # encodedImgData = base64.b64encode(data.getvalue())
            # type(img)
            # img.show()

            # https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files !!!
            # https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
            qrCodePath = Path(str(Path.cwd()) + "/qrCode.png").rename(str(Path.cwd()) + "/static/qrCode.png")

            return render_template("index.html", data="/static/qrCode.png")


@app.route("/save", methods=['POST'])
def saveQRClicked():
    if request.method == "POST":
        if 'save' in request.form:
            # https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
            # (referenced for using os library to get specific path. not sure if it will work for Winows as am using Mac)
            source = str(os.path.join(Path.cwd(), "static", "qrCode.png"))
            dest = str(os.path.join(Path.home(), "Downloads", "qrCode.png"))

            # https://stackoverflow.com/questions/123198/how-to-copy-files
            shutil.copyfile(source, dest)

            #data = True
            saveVal = True
            saveMessage = "The QR code has been saved. Check your Downloads folder!"


            return render_template("index.html", saveMsg=saveMessage, save=saveVal)


@app.route("/goBackAndCreateAnotherOne", methods=['POST'])
def backButton():
    if request.method == "POST":
        if 'anotherOne' in request.form:
            start = True
            return render_template("index.html", start=start)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7676, debug=True)


# # https://pypi.org/project/qrcode/
# # (referenced this library to create qr codes)
# def main():
#     urlToMakeCode = input("Please copy and paste a website url that you would like converted to a QR code: ")
#
#     img = qrcode.make(urlToMakeCode)
#     type(img)
#
#     imageName = input("Now, please enter a name that the QR code will be saved as (will save as a png photo type): ")
#     imageNameWithType = imageName + ".png"
#
#     img.save(imageNameWithType)
#     img.show(imageNameWithType) # for checking purposes
#
#     if img:
#         print("A QR code has been created! Check the current directory (checking purposes for now)")
#         print("It has been saved as: " + imageName + ".png \n")
#
#     # NOT SURE IF WHAT'S BELOW WILL WORK FOR NON-LINUX LIKE WINDOWS (cuz this works for linux based like Mac)
#     # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
#     saveInDownloads = input("Would you like this QR code saved to your downloads folder? ('Y' for yes, 'N' for no): ")
#     if saveInDownloads == "Y":
#         # https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
#         # (referenced for using os library to get specific path)
#         path = str(os.path.join(Path.home(), "Downloads", imageNameWithType))
#         # https://stackoverflow.com/questions/31434278/how-do-i-use-python-pil-to-save-an-image-to-a-particular-directory
#         # (referenced for saving )
#         img.save(path, "PNG")
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     main()