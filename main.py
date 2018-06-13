import sys
import feature_extractor

arguments = sys.argv

if len(arguments) < 2:
    print("ERROR: not enough arguments for the program. Terminating.")
    exit()

filename1 = sys.argv[1]
filename2 = sys.argv[2]

keypoints1 = feature_extractor.get_keypoints(filename1)
keypoints2 = feature_extractor.get_keypoints(filename2)

keypoint = keypoints1[0]
keypoint2 = keypoints1[1]

print(keypoint.params_list)
print(keypoint.get_distance(keypoint2))





