import pickle
import random

# load features
features = pickle.load(open("features.pkl", "rb"))

print("Features loaded:", len(features))

# dummy caption generator
captions = [
    "A dog running in the grass",
    "A child playing with a ball",
    "People walking on the street",
    "A man riding a bicycle",
    "A group of people standing together"
]

# show captions for some images
for key in list(features.keys())[:5]:

    caption = random.choice(captions)

    print("\nImage ID:", key)
    print("Generated Caption:", caption)