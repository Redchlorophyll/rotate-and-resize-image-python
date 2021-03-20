from PIL import Image
import os


def list_images(image_dir):
    """ generate list contain name of each file """

    files = os.listdir(image_dir)
    return files


def create_dir(dir_path):
    """ generate new folder if doesn't exists """

    isfile = os.path.isdir(dir_path)

    if not isfile:
        os.mkdir(dir_path)

def rotate_resize_image(image_name, image_path, save_path, rotate_value, resize_value):
    """ convert image to desired property and save it afterward """

    img = Image.open(image_path)
    rotated_image = img.rotate(rotate_value)
    resized_image = rotated_image.resize(resize_value)
    resized_image.save(save_path + "/" + image_name, format="tiff")


if __name__ == "__main__":
    cur_path = os.getcwd()
    img_path = cur_path + "/images"
    output_path = cur_path + "/icons"

    images = list_images(img_path)
    create_dir(output_path)

    for img in images:
        if img == ".DS_Store":
            continue

        img_path = cur_path + "/images/" + img
        rotate_resize_image(img, img_path, output_path, 90, (128,128))
