import numpy as np
import pandas as pd
import os
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt

def load_data(folder, annotations):
    data = []
    labels = []
    for filename in os.listdir(folder):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(folder, filename))
            img = img.resize((256, 256))  # Resize images to a fixed size
            data.append(np.array(img))
            label = annotations.loc[annotations['filename'] == filename]['class'].values[0]
            labels.append(label)
    return np.array(data), np.array(labels)

# Load annotations
train_annotations = pd.read_csv("train/_annotations.csv")
test_annotations = pd.read_csv("test/_annotations.csv")
val_annotations = pd.read_csv("valid/_annotations.csv")

# Load data with equal number of images and labels
train_data, train_labels = load_data('train', train_annotations)
test_data, test_labels = load_data('test', test_annotations)
validation_data, validation_labels = load_data('valid', val_annotations)

class_labels = ['Drunk', 'Sober']

plt.figure(figsize=(15, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(train_data[i])
    plt.title(train_labels[i])
    plt.axis('off')
plt.show()

train_data = train_data / 255.0
test_data = test_data / 255.0
validation_data = validation_data / 255.0

# Encode labels
# Convert labels to pandas Series
train_labels_series = pd.Series(train_labels)
test_labels_series = pd.Series(test_labels)
validation_labels_series = pd.Series(validation_labels)

# Replace labels
train_labels_series = train_labels_series.replace({'Drunk': 0, 'Sober': 1})
test_labels_series = test_labels_series.replace({'Drunk': 0, 'Sober': 1})
validation_labels_series = validation_labels_series.replace({'Drunk': 0, 'Sober': 1})

# Encode labels
label_encoder = LabelEncoder()
train_labels = label_encoder.fit_transform(train_labels_series)
test_labels = label_encoder.transform(test_labels_series)
validation_labels = label_encoder.transform(validation_labels_series)


plt.figure(figsize=(15, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(train_data[i])
    plt.title(train_labels[i])
    plt.axis('off')
plt.show()

print("Train data shape:", train_data.shape)
print("Train labels shape:", train_labels.shape)
print("Test data shape:", test_data.shape)
print("Test labels shape:", test_labels.shape)
print("Validation data shape:", validation_data.shape)
print("Validation labels shape:", validation_labels.shape)


model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_data=(validation_data, validation_labels))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

test_loss, test_acc = model.evaluate(test_data, test_labels)
print('Test Accuracy:', test_acc)

model.save("drunk_detector_model.h5")
