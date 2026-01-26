from PIL import Image
import numpy as np
from pipeline import run_pipeline
from utils import inspect_image

img = Image.open("data/image.jpg")
img_arr = np.array(img)

def menu():
    print("\n" + "=" * 30)
    print("       IMAGE PROCESSOR")
    print("=" * 30)
    print("1. VIEW IMAGE")
    print("2. INSPECT IMAGE")
    print("3. INVERT IMAGE")
    print("4. GRAYSCALE")
    print("5. ADJUST BRIGHTNESS")
    print("6. ADJUST CONTRAST")
    print("7. FLIP HORIZONTAL")
    print("8. FLIP VERTICAL")
    print("9. ROTATE CLOCKWISE")
    print("10. ROTATE ANTI-CLOCKWISE")
    print("0. EXIT")

def main():
    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            Image.fromarray(img_arr).show()

        elif choice == "2":
            info = inspect_image(img_arr)
            for k, v in info.items():
                print(f"{k}: {v}")

        elif choice == "3":
            out = run_pipeline(img_arr, "invert")
            Image.fromarray(out).save("output/inverted.jpg")
            Image.fromarray(out).show()

        elif choice == "4":
            out = run_pipeline(img_arr, "grayscale")
            Image.fromarray(out).save("output/grayscale.jpg")
            Image.fromarray(out).show()

        elif choice == "5":
            val = int(input("Brightness (-100 to 100): "))
            out = run_pipeline(img_arr, "brightness", val)
            Image.fromarray(out).save("output/brightness.jpg")
            Image.fromarray(out).show()

        elif choice == "6":
            val = int(input("Contrast (-100 to 100): "))
            out = run_pipeline(img_arr, "contrast", val)
            Image.fromarray(out).save("output/contrast.jpg")
            Image.fromarray(out).show()

        elif choice == "7":
            out = run_pipeline(img_arr, "flip_h")
            Image.fromarray(out).save("output/flip_h.jpg")
            Image.fromarray(out).show()

        elif choice == "8":
            out = run_pipeline(img_arr, "flip_v")
            Image.fromarray(out).save("output/flip_v.jpg")
            Image.fromarray(out).show()

        elif choice == "9":
            out = run_pipeline(img_arr, "rotate_cw")
            Image.fromarray(out).save("output/rotate_cw.jpg")
            Image.fromarray(out).show()

        elif choice == "10":
            out = run_pipeline(img_arr, "rotate_ccw")
            Image.fromarray(out).save("output/rotate_ccw.jpg")
            Image.fromarray(out).show()

        elif choice == "0":
            print('Exiting...')
            break

if __name__ == "__main__":
    main()
