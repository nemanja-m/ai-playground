from keras.models import Sequential
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.optimizers import SGD
import os.path

class LeNet:

    @staticmethod
    def build(train_data, train_labels):
        width   = 28
        height  = 28
        depth   = 1
        classes = 10

        # Initialize the model
        model = Sequential()

        # CONV => RELU => POOL
        model.add(Convolution2D(20, 5, 5, border_mode="same", input_shape=(depth, height, width)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # CONV => RELU => POOL
        model.add(Convolution2D(50, 5, 5, border_mode="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # FC => RELU
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))

        # Softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        if os.path.isfile('neural_net/weights.hdf5'):
            model.load_weights('neural_net/weights.hdf5')

        # Compile model
        model.compile(loss="categorical_crossentropy",
                      optimizer=SGD(lr=0.1),
                      metrics=["accuracy"])

        if not os.path.isfile('neural_net/weights.hdf5'):
            # Train model
            model.fit(train_data, train_labels, batch_size=128, nb_epoch=30,
                    verbose=1)

            # Save trained model
            print '\n=> Saving trained model ...\n'
            model.save_weights('neural_net/weights.hdf5', overwrite=True)

        return model
