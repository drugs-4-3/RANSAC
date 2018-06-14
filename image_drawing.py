from PIL import Image, ImageDraw
import shutil


def draw_keypoints(filename, keypoints):
    new_img_filename = create_new_img_filename(filename)
    shutil.copy(filename, new_img_filename)

    img = Image.open(new_img_filename)
    draw = ImageDraw.Draw(img)
    for keypoint in keypoints:
        draw.ellipse([(keypoint.x - 5, keypoint.y - 5), (keypoint.x + 5, keypoint.y + 5)], fill=128)
    img.save(new_img_filename)


def create_new_img_filename(filename):
    last_dot_occurence = filename.rfind('.')
    name_part = filename[:last_dot_occurence]
    extension_part = filename[last_dot_occurence:]
    new_filename = name_part + "_keypoints" + extension_part
    return new_filename
