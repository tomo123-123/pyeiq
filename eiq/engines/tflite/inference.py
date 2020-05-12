import numpy as np
from tflite_runtime.interpreter import Interpreter

from eiq.utils import timeit

class TFLiteInterpreter:
    def __init__(self, model=None):
        self.interpreter = None
        self.input_details = None
        self.output_details = None

        if model is not None:
            self.interpreter = Interpreter(model)
            self.interpreter.allocate_tensors()
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()

    def dtype(self):
        return self.input_details[0]['dtype']

    def get_tensor(self, index, squeeze=False):
        if squeeze:
            return np.squeeze(self.interpreter.get_tensor(
                                   self.output_details[index]['index']))

        return self.interpreter.get_tensor(
                    self.output_details[index]['index'])

    def set_tensor(self, image):
        self.interpreter.set_tensor(self.input_details[0]['index'], image)

    def run_inference(self):
        with timeit("Inference time"):
            self.interpreter.invoke()


def get_details(interpreter):
    return interpreter.get_input_details(), interpreter.get_output_details()


def inference(interpreter):
    with timeit("Inference time"):
        interpreter.invoke()


def load_model(model):
    interpreter = Interpreter(model)
    interpreter.allocate_tensors()

    return interpreter
