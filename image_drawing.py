from PIL import Image, ImageDraw, ImageColor
import shutil
import os
import image_analyzer
from random import randint


def draw_keypoints(filename, keypoints):
    """
    Creates new image with keypoints drawn in the same directory as given image file
    """
    new_img_filename = get_filename_with_keypoints(filename)
    shutil.copy(filename, new_img_filename)

    img = Image.open(new_img_filename)
    draw = ImageDraw.Draw(img)
    for keypoint in keypoints:
        draw.ellipse([(keypoint.x - 3, keypoint.y - 3), (keypoint.x + 3, keypoint.y + 3)], fill=128)
    img.save(new_img_filename)


def get_filename_with_keypoints(filename):
    """
    Attaches "_keypoints" text to the end of filename before extension
    """
    name, extension = os.path.splitext(filename)
    return name + "_keypoints" + extension


def draw_corresponding_keypoints(filename1, filename2, keypoints1, keypoints2):
    """
    Returns filename to img file
    Combines two images vertically - one under another and draws lines connecting corresponding keypoints

    Argument image files must be of the same format and identical dimensions
    """
    output_file = "keypoints_draw.png"
    combined_img_filename = combine_images(filename1, filename2, output_file)
    corresponding_keypoints_indices = image_analyzer.get_corresponding_keypoints_indices(keypoints1, keypoints2)
    img = Image.open(combined_img_filename)

    for (i1, i2) in corresponding_keypoints_indices:
        draw_line(img, keypoints1[i1], keypoints2[i2])
    img.save(output_file)
    return combined_img_filename


def draw_line(img, keypoint1, keypoint2):
    _, height = img.size
    additional_height = height/2

    draw = ImageDraw.Draw(img)
    p1 = (keypoint1.x, keypoint1.y)
    p2 = (keypoint2.x, keypoint2.y + additional_height)
    draw.line([p1, p2], fill=get_random_color())


def get_random_color():
    """
    Returns random color tuple.
    """
    return randint(0, 255), randint(0, 255), randint(0, 255)


def combine_images(filename1, filename2, out_filename):
    """
    Returns filename of image combined of 2 images vertically - one under another
    """

    img1 = Image.open(filename1)
    img2 = Image.open(filename2)

    width1, height1 = img1.size
    width2, height2 = img2.size

    result_img = Image.new('RGB', (max(width1, width2), height1 + height2))
    result_img.paste(img1, (0, 0))
    result_img.paste(img2, (0, height1))
    result_img.save(out_filename)
    return out_filename




