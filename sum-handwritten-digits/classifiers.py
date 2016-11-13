from sklearn.datasets import fetch_mldata
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
import numpy as np
import importlib
import os
import errno

class Classifier:

    def __init__(self, clsf):
        # Save classifier type
        self.classifier = clsf

        # Get MNIST dataset
        print '\n=> Fetching dataset ...'
        mnist = fetch_mldata('MNIST original')

        # Create classifier model
        if clsf == 'knn':
            print '=> Creating KNN classifier model ...'

            if os.path.isfile('knn/knn_model.pkl'):
                print '=> Loading model ...'
                self.model = joblib.load('knn/knn_model.pkl')
                print '=> Model loaded successfully'
            else:
                print '=> Training model ...'
                self.model = KNeighborsClassifier(n_neighbors = 1)
                self.model.fit(mnist.data, mnist.target)

                print '=> Saving trained model ...'

                # Try to create folder. If already exists ignore exception
                # Any other error gets reported.
                try:
                    os.makedirs('knn')
                except OSError as exception:
                    if exception.errno != errno.EEXIST:
                        raise

                joblib.dump(self.model, 'knn/knn_model.pkl')
                print '=> KNN model saved successfully to \'knn/knn_model.pkl\''

        elif clsf == 'cnn':
            print '=> Creating CNN classifier model ...\n'
            # Reshape the MNIST dataset from a flat list of 784-dim vectors, to
            # 28 x 28 pixel images, then scale the data to the range [0, 1.0]
            data         = mnist.data.reshape((mnist.data.shape[0], 28, 28))
            train_data   = data[:, np.newaxis, :, :] / 255.0
            train_labels = mnist.target.astype('int')

            # Load np_utils dynamically
            module   = importlib.import_module('keras.utils')
            np_utils = getattr(module, 'np_utils')

            # Transform the training labels into vectors in the
            # range [0, 10] -- this generates a vector for each label,
            # where the index of the label is set to `1` and all other entries
            # to `0`; in the case of MNIST, there are 10 class labels
            train_labels = np_utils.to_categorical(train_labels, 10)

            # Load LeNet class dynamically
            module = importlib.import_module('neural_net.lenet')
            LeNet  = getattr(module, 'LeNet')

            # Initialize LeNet
            self.model = LeNet.build(train_data, train_labels)

    def predict(self, image):
        if self.classifier == 'knn':
            flatten = image.astype('uint8').flatten().reshape(1, -1)
            return self.model.predict(flatten)

        if self.classifier == 'cnn':
            data = image.reshape((1, 1) + image.shape)
            # Count probabilities for each class / digit
            probabilities = self.model.predict(data)

            # Return digit with the highest probability
            return probabilities.argmax(axis=1)[0]
