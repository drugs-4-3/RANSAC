
def get_corresponding_keypoints_indices(keypoints1, keypoints2):
    """
    Returns list of tuples in format(index1, index2).
    Each tuple contains indexes of corresponding to each other keypoints1 and keypoints2
    """
    nearest_neighbours1, nearest_neighbours2 = get_nearest_neighbours_list(keypoints1, keypoints2)
    corresponding_keypoints_indices = []
    for index, val in enumerate(nearest_neighbours1):
        if nearest_neighbours2[val] == index:
            corresponding_keypoints_indices.append((index, val))
    return corresponding_keypoints_indices


def get_nearest_neighbours_list(keypoints1, keypoints2):
    """
    For given list of Keypoints returns 2 lists:
        1) for each keypoint1 nearest neighbour from keypoints2
        2) for each keypoint2 nearest neighbour from keypoints1
    """
    nearest_neighbours1 = get_nearest_neighbours(keypoints1, keypoints2)
    nearest_neighbours2 = get_nearest_neighbours(keypoints2, keypoints1)
    return nearest_neighbours1, nearest_neighbours2


def get_nearest_neighbours(keypoints_seeking_neighbours, keypoints_possible_neighbours):
    """
    For each Keypoint from list keypoints_seeking_neighbours
     matches nearest neighbour in list "keypoints_possible_neighbours".
    Returns simple int list (index => value):
    index corresponds to index in first list (keypoints seeking),
    value corresponds to index in seconf list (keypoints possible neighbours)
    """
    result = []
    for keypoint in keypoints_seeking_neighbours:
        result.append(find_index_of_nearest_neighbour(keypoint, keypoints_possible_neighbours))
    return result


def find_index_of_nearest_neighbour(keypoint, keypoints_possible_neighbours):
    """
    Returns index of nearest neighbour for given keypoint from list of keypoints
    """
    distances = [keypoint.get_distance(neighbour) for neighbour in keypoints_possible_neighbours]
    return distances.index(min(distances))

