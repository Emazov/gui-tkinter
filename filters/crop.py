import os.path

from PIL import Image, ImageDraw, ImageFont

path = '../img'
new_path = '../cropped-img//'
dirs = os.listdir(path)


def crop():
    for i in dirs:
        fullpath = os.path.join(path, i)
        if os.path.isfile(fullpath):
            image = Image.open(fullpath)
            file_name = os.path.basename(fullpath)
            f, e = os.path.splitext(file_name)

            width, height = image.size
            new_width, new_height = 1080, 1080

            left = (width - new_width) / 2
            top = (height - new_height) / 2
            right = (width + new_width) / 2
            bottom = (height + new_height) / 2

            new_image = image.crop((left, top, right, bottom))

            new_image.save(new_path + f + '.jpg', "JPEG", quality=100)


crop()