import numpy as np
from PIL import Image


def make_image (amp_pixel_arr):
    size = len(amp_pixel_arr)

    # MAKING THE IMAGE WIDTH AND HEIGHT
    img_w = 100
    img_h = size // 100
    print(f'HEIGH HEIGHT HEIGHT HEIGHT HEIGHT HEIGHT HEIGHT HEIGHT HEIGHT HEIGHT HEIGHT{img_h}')

    # MAKING THE TEMPLATE FOR THE IMAGE
    image = np.zeros((img_h, img_w, 3), dtype=np.uint8)

    # CREATING THE PIXELS
    for i in range(size):
        row = i // img_w # FINDING WHAT ROW IT IS ON
        column = i % img_w # FINDING WHAT COLUMN IT IS ON

        print(amp_pixel_arr[i][:3])
        #try:
        image[row, column] = tuple(amp_pixel_arr[i])
        #except Exception as e:
            #print(f"=======EEERRRROOOORRRRR======================= {amp_pixel_arr[i]}")# SETTING THE PIXEL

    # MAKING THE IMAGE
    actual_image = Image.fromarray(image, "RGB")
    actual_image.save("TEST1.png")
    actual_image.show()
