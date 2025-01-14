"""
Created by Vanzio on 18/02/2024
last modified: 09/04/2024 13:16
"""

from keras.models import Sequential
from keras.layers import LSTM, Dense, TimeDistributed, Conv1D, MaxPooling1D, Flatten, Reshape
from constants import CLASS_OUTPUT, SEQUENCE_LENGTH, MODEL_INPUT
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy as sparse
import tensorflow as tf


# Function create an tensor flow model structure which can be called and trained on
# takes input as input shape and give an tensor object as an output
def create_model(input_shape):

    model = Sequential()

    # layers in the model
    #####################################################################################

    model.add(Reshape((SEQUENCE_LENGTH, MODEL_INPUT, 1), input_shape=input_shape, dtype=tf.float32))
    model.add(TimeDistributed(Conv1D(filters=64, kernel_size=3, activation='tanh', dtype=tf.float32)))
    model.add(TimeDistributed(MaxPooling1D(pool_size=2, dtype=tf.float32)))
    model.add(TimeDistributed(Conv1D(filters=32, kernel_size=3, activation='tanh', dtype=tf.float32)))
    model.add(TimeDistributed(MaxPooling1D(pool_size=2, dtype=tf.float32)))
    model.add(TimeDistributed(Conv1D(filters=16, kernel_size=3, activation='tanh', dtype=tf.float32)))
    model.add(TimeDistributed(MaxPooling1D(pool_size=2, dtype=tf.float32)))
    model.add(TimeDistributed(Flatten(dtype=tf.float32)))
    model.add(LSTM(units=16, return_sequences=True, dtype=tf.float32))
    model.add(Dense(units=CLASS_OUTPUT, activation='softmax', dtype=tf.float32))

    ######################################################################################

    # This line builds the model architecture
    model.compile(optimizer=Adam(), loss=sparse, metrics=['accuracy'])

    # print(model.summary())

    return model
