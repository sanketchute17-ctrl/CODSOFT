from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import os
import pickle
from tqdm import tqdm

# load model
model = VGG16()
model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

print("VGG16 Model Loaded")

dataset = "dataset/Flickr8k_Dataset"

features = {}

image_list = os.listdir(dataset)[:500]

for img_name in tqdm(image_list):

    img_path = os.path.join(dataset, img_name)

    image = load_img(img_path, target_size=(224,224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)

    feature = model.predict(image, verbose=0)

    image_id = img_name.split('.')[0]

    features[image_id] = feature

print("Features Extracted:", len(features))

pickle.dump(features, open("features.pkl","wb"))

print("Features saved to features.pkl")