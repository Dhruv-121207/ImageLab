# 📸 ImageLab — Image Processing Toolkit

A Python-based image processing toolkit built using **NumPy and Pillow**. ImageLab allows users to perform common image transformations via a **CLI interface** and save the processed results automatically.

This project supports inversion, grayscale conversion, brightness and contrast adjustment, flipping, rotation, and inspection of image properties.

---

## 🚀 Features

* View and inspect images
* Image inversion and grayscale conversion
* Brightness and contrast adjustment
* Horizontal and vertical flipping
* Clockwise and anti-clockwise rotation
* Automatic saving of processed images

---

## 🧠 Concepts Used

* NumPy arrays (2D & 3D) for image representation
* Indexing, slicing, and broadcasting
* Data type conversion and clipping
* Modular Python functions
* CLI-based user interaction
* Basic image processing algorithms

---

## 📁 Project Structure

```
ImageLab/
├── image_processor.py      # Core image processing functions (NumPy-based)
├── utils.py                # Helper functions for image inspection and type conversion
├── pipeline.py             # Routes operations to the correct image processing function
├── main.py                 # CLI entry point for the application
├── data/
│   └── image.jpg           # Input images
├── output/
│   └── processed_images/   # Folder to save output images
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🖼️ Image Handling

* RGB images with three channels
* Data type: `uint8`
* Pixel values range from 0 to 255

---

## ▶️ How to Run

1. Install Python 3.8+.
2. Install dependencies:

```bash
pip install numpy pillow
```

3. Run the program:

```bash
python main.py
```

Follow the on-screen menu to apply various image operations.

---

## 📜 License

This project is licensed under the **MIT License**, allowing free use, modification, and distribution provided that the original copyright notice is included.

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only** and is not optimized for production-grade or performance-critical image processing. The author makes no warranties regarding accuracy, reliability, or suitability for professional, medical, or commercial applications.
