import tensorflow as tf
import keras
from keras.optimizers import Adam
from keras.models import load_model
from keras.models import Model
from keras.layers import Input, Conv2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from keras import backend as K
K.set_image_data_format('channels_first')

def vgg_face(weights_path=None):
    img = Input(shape=(3, 224, 224))

    pad1_1 = ZeroPadding2D(padding=(1, 1))(img)
    conv1_1 = Conv2D(64, (3, 3), activation='relu', name='conv1_1')(pad1_1)
    pad1_2 = ZeroPadding2D(padding=(1, 1))(conv1_1)
    conv1_2 = Conv2D(64, (3, 3), activation='relu', name='conv1_2')(pad1_2)
    pool1 = MaxPooling2D((2, 2), strides=(2, 2))(conv1_2)

    pad2_1 = ZeroPadding2D((1, 1))(pool1)
    conv2_1 = Conv2D(128, (3, 3), activation='relu', name='conv2_1')(pad2_1)
    pad2_2 = ZeroPadding2D((1, 1))(conv2_1)
    conv2_2 = Conv2D(128, (3, 3), activation='relu', name='conv2_2')(pad2_2)
    pool2 = MaxPooling2D((2, 2), strides=(2, 2))(conv2_2)

    pad3_1 = ZeroPadding2D(padding=(1, 1))(pool2)
    conv3_1 = Conv2D(256, (3, 3), activation='relu', name='conv3_1')(pad3_1)
    pad3_2 = ZeroPadding2D(padding=(1, 1))(conv3_1)
    conv3_2 = Conv2D(256, (3, 3), activation='relu', name='conv3_2')(pad3_2)
    pad3_3 = ZeroPadding2D(padding=(1, 1))(conv3_2)
    conv3_3 = Conv2D(256, (3, 3), activation='relu', name='conv3_3')(pad3_3)
    pool3 = MaxPooling2D((2, 2), strides=(2, 2))(conv3_3)

    pad4_1 = ZeroPadding2D(padding=(1, 1))(pool3)
    conv4_1 = Conv2D(512, (3,3), activation='relu', name='conv4_1')(pad4_1)
    pad4_2 = ZeroPadding2D(padding=(1, 1))(conv4_1)
    conv4_2 = Conv2D(512, (3, 3), activation='relu', name='conv4_2')(pad4_2)
    pad4_3 = ZeroPadding2D(padding=(1, 1))(conv4_2)
    conv4_3 = Conv2D(512, (3, 3), activation='relu', name='conv4_3')(pad4_3)
    pool4 = MaxPooling2D((2, 2), strides=(2, 2))(conv3_3)

    pad5_1 = ZeroPadding2D(padding=(1, 1))(pool4)
    conv5_1 = Conv2D(512, (3, 3), activation='relu', name='conv5_1')(pad5_1)
    pad5_2 = ZeroPadding2D(padding=(1, 1))(conv5_1)
    conv5_2 = Conv2D(512, (3, 3), activation='relu', name='conv5_2')(pad5_2)
    pad5_3 = ZeroPadding2D(padding=(1, 1))(conv5_2)
    conv5_3 = Conv2D(512, (3, 3), activation='relu', name='conv5_3')(pad5_3)
    pool5 = MaxPooling2D((2, 2), strides=(2, 2))(conv5_3)

    fc6 = Conv2D(4096, (7, 7), activation='relu', name='fc6')(pool5)
    fc6_drop = Dropout(0.5)(fc6)
    fc7 = Conv2D(4096, (1, 1), activation='relu', name='fc7')(fc6_drop)
    fc7_drop = Dropout(0.5)(fc7)
    fc8 = Conv2D(2622, (1, 1), activation='relu', name='fc8')(fc7_drop)

    flat = Flatten()(fc8)
    out = Activation('softmax')(flat)

    model = Model(inputs=img, outputs = out)

    if weights_path:
        model.load_weights(weights_path)

    return model
