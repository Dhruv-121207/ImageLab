# ImageLab 🖼️

ImageLab is a Flask-based web application that allows users to upload an image, apply multiple transformations, compare results side-by-side, and download the edited output.

The core image transformations are implemented using **NumPy-based array manipulation**, not high-level image processing libraries.

---

# 🚀 Features

* Upload and validate image files
* Side-by-side preview (Original vs Edited)
* Multiple image transformations
* Brightness and contrast adjustments
* Reset to original image
* Clear uploaded images
* Download edited image

---

# 🧮 Image Transformations 

All transformations are performed by converting images into NumPy arrays and manipulating pixel values directly.

Implemented operations:

* Grayscale
* Inversion 
* Horizontal & Vertical Flip 
* Rotate Clockwise & Anti-Clockwise 
* Brightness adjustment 
* Contrast adjustment
* All outputs are clipped safely within the `[0, 255]` pixel range.

---

# ⚙️ Technologies Used

* Python 3
* Flask
* NumPy
* Pillow (PIL)
* HTML5
* CSS3

---

# 📥 Installation & Setup

## Clone the Repository

```bash
git clone https://github.com/Dhruv-121207/ImageLab.git
cd ImageLab
```

## Create & Activate Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000/
```

---

# 📌 Notes

* Images are processed in RGB format.
* The application runs in debug mode by default.
* Uploaded files are stored temporarily in the `uploads/` directory.

---

# 📜 License

Open for personal and educational use.
