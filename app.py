import os
import time
import numpy as np 
from PIL import Image
from image_processor import *
from flask import Flask,redirect,request,render_template,send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

for file in ["original.jpg","current.jpg"]:
        path = os.path.join(UPLOAD_FOLDER,file)
        if os.path.exists(path):
            os.remove(path)

def clear():
    for file in ["original.jpg","current.jpg"]:
        path = os.path.join(UPLOAD_FOLDER,file)
        if os.path.exists(path):
            os.remove(path)

@app.route("/upload",methods=["POST"])
def upload():
    file = request.files.get("image")

    if not file or file.filename == "":
        return redirect("/")
    
    try:
        img = Image.open(file).convert("RGB")
        img.verify()
    except Exception:
        return "Invalid image file"
        
    original_path = os.path.join(UPLOAD_FOLDER,"original.jpg")
    current_path = os.path.join(UPLOAD_FOLDER,"current.jpg")

    img.save(original_path)
    img.save(current_path)

    return redirect("/")

@app.route("/download")
def download():
    return send_from_directory(UPLOAD_FOLDER,"current.jpg",as_attachment=True)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)

@app.route("/",methods=["GET","POST"])
def home():

    original_path = os.path.join(UPLOAD_FOLDER,"original.jpg")
    current_path = os.path.join(UPLOAD_FOLDER,"current.jpg")

    if request.method == "GET" and "clear" in request.args:
        clear()
        return redirect("/")
    
    if request.method == "POST":
        action = request.form.get("action")

        if action and os.path.exists(current_path):
            
            if action == "reset":
                Image.open(original_path).save(current_path)
                return redirect("/")
            
            img = Image.open(current_path)
            img_arr = np.array(img)

            brightness_slider = int(request.form.get("brightness_value",0))
            contrast_slider = int(request.form.get("contrast_value",0))

            if action == "grayscale":
                result = gray_scale(img_arr)

            elif action == "inversion":
                result = inversion(img_arr)

            elif action == "vertically":
                result = flip_vertically(img_arr)

            elif action == "horizontally":
                result = flip_horizontally(img_arr)

            elif action == "rotate_cw":
                result = rotate_clockwise(img_arr)

            elif action == "rotate_acw":
                result = rotate_anti_clockwise(img_arr)

            elif action == "brightness":
                result = adjust_brightness(img_arr,brightness_slider)

            elif action == "contrast":
                result = adjust_contrast(img_arr,contrast_slider)

            else:
                return redirect("/")
            
            Image.fromarray(result).save(current_path)
            return redirect("/")
    
    image_exists = os.path.exists(current_path)

    return render_template("index.html",image_exists=image_exists,timestamp=time.time())

if __name__ == "__main__":
    app.run(debug=True)