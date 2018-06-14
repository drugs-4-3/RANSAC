
# extracting features command:
# ./extract_features_32bit.ln -haraff -sift -i obraz.png -DE

import sys
import feature_extractor
import image_drawing
import image_analyzer
import time
import os


def curr_time():
    return int(round(time.time() * 1000))


def generate_neighbours():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    keypoints1 = feature_extractor.get_keypoints(filename1)
    keypoints2 = feature_extractor.get_keypoints(filename2)

    t1 = curr_time()
    asd = image_analyzer.get_corresponding_keypoints_indices(keypoints1, keypoints2)
    t2 = curr_time()
    print("execution took: " + str(t2-t1) + " ms.")
    print("results count: " + str(len(asd)))
    print(asd)


def draw_keypoints():
    img_file = sys.argv[1]
    keypoints_file = sys.argv[2]
    keypoints = feature_extractor.get_keypoints(keypoints_file)

    t1 = curr_time()
    asd = image_drawing.draw_keypoints(img_file, keypoints)
    t2 = curr_time()
    print("execution took: " + str(t2 - t1) + " ms.")


def combine_images():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    image_drawing.combine_images(file1, file2, "combined_images.png")


def generate_keypoints_file(img_filename):
    """
    Generates keypoints file for given img and returns its filename
    """
    command = "./extract_features_64bit.ln -haraff -sift -i {filename} -DE"
    command = command.replace("{filename}", img_filename)
    os.system(command)
    return img_filename + ".haraff.sift"


arguments = sys.argv
if len(arguments) < 2:
    print("ERROR: not enough arguments for the program. Terminating.")
    exit()

img_file1 = arguments[1]
img_file2 = arguments[2]

keypoints_file1 = generate_keypoints_file(img_file1)
keypoints_file2 = generate_keypoints_file(img_file2)

keypoints1 = feature_extractor.get_keypoints(keypoints_file1)
keypoints2 = feature_extractor.get_keypoints(keypoints_file2)

print("Drawing image...")
t1 = curr_time()
image_drawing.draw_corresponding_keypoints(img_file1, img_file2, keypoints1, keypoints2)
t2 = curr_time()
print ("Finished! Execution took " + str(t2-t1) + " ms.")


