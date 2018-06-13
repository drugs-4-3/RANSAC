

class Keypoint:

    def __init__(self, x, y, a, b, c, features):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.c = c
        self.features= [float(param) for param in features]

    def get_distance(self, keypoint):
        """
        Returns number indicating visual distance from self and given Keypoint
        :param keypoint:
        :return:
        """
        distances = [abs(self.features[index] - keypoint.params_list[index]) for index in range(len(self.features))]
        return sum(distances)

