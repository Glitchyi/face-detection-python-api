import cv2
import pathlib
import numpy as np
import onnxruntime as ort

#Passing the input to the model

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load the ONNX model
ort_session = ort.InferenceSession('models/best.onnx')

input_img = cv2.imread('test.jpg')
input_img = cv2.resize(input_img, (640, 640))
input_img = np.expand_dims(np.transpose(input_img, (2, 0, 1)), axis=0).astype(float)

# Convert to float32
input_img = input_img.astype('float32')
results = ort_session.run(None, {ort_session.get_inputs()[0].name: input_img})
results = results[0][0]
covered_prob = results[:, 0].max()
not_covered_prob = results[:, 1].max()
if covered_prob > not_covered_prob:
    result = "not-covered"
    print(f"{result} | NC: {not_covered_prob} | C: {covered_prob} ")
else:
    result = "covered"
    print(f"{result} | NC: {not_covered_prob} | C: {covered_prob} ")