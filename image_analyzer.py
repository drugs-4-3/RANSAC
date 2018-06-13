import feature_extractor

def get_nearest_neighbours_list(keypoints1, keypoints2):
    nearest_neighbours1 = get_nearest_neighbours(keypoints1, keypoints2)
    nearest_neighbours2 = get_nearest_neighbours(keypoints2, keypoints1)


def get_nearest_neighbours(keypoints_seeking_neighbours, keypoints_possible_neighbours):
    """
    For each Keypoint from list keypoints_seeking_neighbours
     matches nearest neighbour in list "keypoints_possible_neighbours".
    Returns simple int list (index => value):
    index corresponds to index in first list (keypoints seeking),
    value corresponds to index in seconf list (keypoints possible neighbours)

    :param keypoints_seeking_neighbours:
    :param keypoints_possible_neighbours:
    :return: []int
    """
    result = []
    for keypoint in keypoints_seeking_neighbours:
        result.append(find_index_of_nearest_neighbour(keypoint, keypoints_possible_neighbours))


def find_index_of_nearest_neighbour(keypoint, keypoints_possible_neighbours):
    distances = [keypoint.get_distance(neighbour) for neighbour in keypoints_possible_neighbours]
    return distances.index(min(distances))

