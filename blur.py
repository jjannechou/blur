"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""
from simpleimage import SimpleImage


def main():
    """
    show 2 images: the original smiley-face image, the blurred smiley-face image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: SimpleImage, the original smiley-face image
    :return: SimpleImage, the blurred smiley-face image
    """
    blurred_img = SimpleImage.blank(img.width, img.height)

    # each blank pixel
    for x in range(img.width):
        for y in range(img.height):
            blur_pixel = blurred_img.get_pixel(x, y)
            # variables needed to be calculated (每一格都歸零重新計算)
            g = 0
            r = 0
            b = 0
            total = 0
            # pixel around
            for i in range(3):
                for j in range(3):
                    if img.width > x+i-1 >= 0 and img.height > y+j-1 >= 0:
                        around_pixel = img.get_pixel(x+i-1, y+j-1)
                        g += around_pixel.green
                        r += around_pixel.red
                        b += around_pixel.blue
                        total += 1
            # start color
            blur_pixel.green = g // total
            blur_pixel.red = r // total
            blur_pixel.blue = b // total
    return blurred_img



if __name__ == '__main__':
    main()
