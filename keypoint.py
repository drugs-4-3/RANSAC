import time
import scipy.spatial.distance
import numpy


class Keypoint:

    def __init__(self, x, y, a, b, c, features):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.c = c
        self.features = numpy.array([float(param) for param in features])
        self.key = str(features)

    def get_distance(self, keypoint):
        """
        Returns number indicating visual distance from self and given Keypoint
        :param keypoint:
        :return:
        """
        if self.distance_in_cache(keypoint):
            return self.distance_from_cache(keypoint)

        # other - slower implementations of distance function:
        # dist = sum([abs(self.features[index] - keypoint.features[index]) for index in range(len(self.features))])
        # dist = sum(map(lambda xy: (xy[0]-xy[1])**2, zip(self.features, keypoint.features)))
        dist = numpy.absolute(numpy.sum(self.features - keypoint.features))

        self.save_to_cache(keypoint, dist)
        return dist

    def distance_in_cache(self, keypoint):
        key1 = self.key + ":" + keypoint.key
        key2 = keypoint.key + ":" + self.key
        return key1 in DistanceCacher.cache or key2 in DistanceCacher.cache

    def distance_from_cache(self, keypoint):
        key1 = self.key + ":" + keypoint.key
        key2 = keypoint.key + ":" + self.key

        if key1 in DistanceCacher.cache:
            return DistanceCacher.cache[key1]
        else:
            return DistanceCacher.cache[key2]

    def save_to_cache(self, keypoint, dist):
        key = self.key + ":" + keypoint.key
        DistanceCacher.cache[key] = dist


class DistanceCacher:
    cache = {}



