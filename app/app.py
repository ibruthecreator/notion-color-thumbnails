from flask import Flask, request, send_file
import os
from os.path import join, dirname, realpath
from PIL import Image

UPLOAD_FOLDER = join(dirname(realpath(__file__)), '')

app = Flask(__name__, static_url_path='/colors')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/<hexcode>',  methods=["GET"])
def index(hexcode):
    hex = hexcode[:6].upper() # make all letters uppercase
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    img = Image.new('RGB', (500, 500), rgb)
    
    if not os.path.exists("colors/" + hex + ".jpg"): # if color doesn't already exist
        img.save("colors/" + hex + ".jpg", "JPEG") # save image to UPLOAD_FOLDER path

    return send_file("colors/" + hex + ".jpg", mimetype='image/gif') # return image
    
if __name__ == '__main__':
    app.run(threaded=True, port=5000)