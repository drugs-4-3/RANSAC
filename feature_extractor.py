from keypoint import Keypoint

SIFT_FEATURES_NUMBER = 128


class ExtractorException(Exception):
    pass


def get_keypoints(filename):
    """
    Returns list of keypoints from file of given filename.
    File must be provided in specific format.
    If file is corrupted then exception is raised.
    :param filename:
    :return: []Keypoint
    """
    keypoint_lines = get_keypoint_lines_from_sift_file(filename)
    return create_keypoints_list(keypoint_lines)


def get_keypoint_lines_from_sift_file(filename):
    """
    Returns list of strings, where each is describing key point of given file
    :param filename: filename from which to extract data
    :return:
    """
    lines = open(filename, 'r').readlines()

    check_file_length(lines)

    features_number = int(lines[0].strip(" \n\r"))
    keypoints_number = int(lines[1].strip(" \n\r"))
    keypoint_lines = [lines[i].strip(" \n\r").split(' ') for i in range(2, len(lines))]

    check_correct_features_number(features_number)
    check_correct_keypoints_number(keypoint_lines, keypoints_number)

    return keypoint_lines


def check_file_length(lines):
    if len(lines) < 2:
        raise ExtractorException("Filename too short or corrupted format")


def check_correct_features_number(features_number):
    if features_number != 128:
        raise ExtractorException("File corrupted: features count is not 128")


def check_correct_keypoints_number(keypoint_lines, keypoints_number):
    if len(keypoint_lines) != keypoints_number:
        raise ExtractorException("File corrupted: file length and content don't correspond")


def create_keypoints_list(keypoint_lines):
    """
    Given list of strings describing keypoints in specific format returns list of Keypoint objects
    :param keypoint_lines: []string
    :return: []Keypoint
    """
    keypoints = []
    for line in keypoint_lines:
        x = float(line[0])
        y = float(line[1])
        a = float(line[2])
        b = float(line[3])
        c = float(line[4])
        features = [int(elem) for elem in line[5:]]

        check_features_count(features)
        keypoints.append(Keypoint(x, y, a, b, c, features))

    return keypoints


def check_features_count(features):
    if len(features) != SIFT_FEATURES_NUMBER:
        raise ExtractorException("File corrupted: not enough features for some key point")