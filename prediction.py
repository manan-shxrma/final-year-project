import numpy as np
from PIL import Image
from keras.preprocessing import image as keras_image
from keras.models import load_model
import matplotlib.pyplot as plt

# for predicting drowsiness
def preprocess_image(image_path, target_size=(128, 128)):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize(target_size)

    img_array = keras_image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def convert_to_category(prediction, threshold=0.5):
    if prediction >= threshold:
        return 1  # drowsy
    else:
        return 0  # non-drowsy

def deploy_model_for_prediction(image_path, model_path):
    saved_model = load_model(model_path)
    preprocessed_image = preprocess_image(image_path)
    prediction = saved_model.predict(preprocessed_image)
    category = convert_to_category(prediction[0][0])
    return category


# for predicting drunkness
def load_data(image_path):
    img = Image.open(image_path)
    img = img.resize((256, 256))
    img = img.convert('RGB')
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img


def predict_image(model_path, image_path):
    loaded_model = load_model(model_path)
    image = load_data(image_path)
    prediction = loaded_model.predict(image)

    if prediction < 0.5:
        return 0
    else:
        return 1


def classifier(image_path):
    drowsiness_model_path = "drowsiness_detection_model.h5"
    drunk_model_path = "drunk_detector_model.h5"
    prediction_drowsiness = deploy_model_for_prediction(image_path, drowsiness_model_path)
    prediction_drunk = predict_image(drunk_model_path, image_path)

    return [prediction_drowsiness, prediction_drunk]


def inference(predictions):
    if predictions[0] == 0 and predictions[1] == 0:
        return 'neither drowsy nor drunk '

    if predictions[0] == 1 and predictions[1] == 1:
        return 'both drowsy and drunk '

    if predictions[0] == 1 and predictions[1] != 1:
        return 'drowsy but not drunk'

    if predictions[0] == 0 and predictions[1] == 1:
        return 'not drowsy but drunk'

image_path = "ae821778-1557-49bd-af9a-2851ab2f0128.jpg"
predictions = classifier(image_path)
print(predictions)
print(inference(predictions))


image = Image.open(image_path)
plt.imshow(image)
plt.title(inference(predictions))
plt.axis('off')
plt.show()