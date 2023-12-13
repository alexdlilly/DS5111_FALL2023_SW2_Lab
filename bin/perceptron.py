"""Module for Perceptron class and associated methods"""
class Perceptron:
    """
    The Perceptron class has methods train(inputs, labels) and predict(inputs).
    """
    def __init__(self):
        """
        Initialization method
        """
        self._weights = None

    def train(self, inputs, labels):
        """
        The train method of the Perceptron class will train a perceptron
        using inputs and labels.
        """
        dummied_inputs = [iter_inputs + [-1] for iter_inputs in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for inputs_ele, label_ele in zip(dummied_inputs, labels):
                label_delta = label_ele - self.predict(inputs_ele)
                for index, iter_inputs in enumerate(inputs_ele):
                    self._weights[index] += .1 * iter_inputs * label_delta
    def predict(self, inputs):
        """
        The predict method of the Perceptron class will predict on inputs 
        based on the train object.
        """
        if len(inputs) == 0:
            return None
        inputs = inputs + [-1]
        return int(0 < sum([dot_iter[0]*dot_iter[1] for dot_iter in zip(self._weights, inputs)]))
