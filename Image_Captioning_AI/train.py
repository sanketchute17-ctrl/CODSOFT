import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add
from tensorflow.keras.preprocessing.text import Tokenizer

# load features
features = pickle.load(open("features.pkl","rb"))

# load tokenizer
tokenizer = pickle.load(open("tokenizer.pkl","rb"))

vocab_size = len(tokenizer.word_index) + 1
max_length = 34

# dummy captions mapping for demo
mapping = {}
for key in features.keys():
    mapping[key] = ["startseq a photo of something endseq"]

# create training data
X1, X2, y = list(), list(), list()

for key, captions in mapping.items():
    feature = features[key][0]
    for caption in captions:
        seq = tokenizer.texts_to_sequences([caption])[0]
        for i in range(1, len(seq)):
            in_seq, out_seq = seq[:i], seq[i]
            in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
            out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]

            X1.append(feature)
            X2.append(in_seq)
            y.append(out_seq)

X1 = np.array(X1)
X2 = np.array(X2)
y = np.array(y)

# define model
inputs1 = Input(shape=(4096,))
fe1 = Dropout(0.5)(inputs1)
fe2 = Dense(256, activation='relu')(fe1)

inputs2 = Input(shape=(max_length,))
se1 = Embedding(vocab_size,256,mask_zero=True)(inputs2)
se2 = Dropout(0.5)(se1)
se3 = LSTM(256)(se2)

decoder1 = add([fe2,se3])
decoder2 = Dense(256,activation='relu')(decoder1)
outputs = Dense(vocab_size,activation='softmax')(decoder2)

model = Model(inputs=[inputs1,inputs2], outputs=outputs)

model.compile(loss='categorical_crossentropy', optimizer='adam')

print(model.summary())

# train
model.fit([X1,X2], y, epochs=3, batch_size=32)

model.save("caption_model.h5")

print("Model saved as caption_model.h5")