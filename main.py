
# extracting features command:
# ./extract_features_32bit.ln -haraff -sift -i obraz.png -DE

import sys
import feature_extractor
import image_drawing
import image_analyzer
import time


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

arguments = sys.argv

if len(arguments) < 2:
    print("ERROR: not enough arguments for the program. Terminating.")
    exit()

# img_filename = sys.argv[1]
# features_filename = sys.argv[2]
#
# keypoints = feature_extractor.get_keypoints(features_filename)
# image_drawing.draw_keypoints(img_filename, keypoints)

# generate_neighbours()

draw_keypoints()


