# About

For a given input image program counts sum of MNIST handwritten digits on it.
Images can be noisy.

# Usage

From bash run:

``` bash
python sum_digits.py -i [--image] <image_path> -c [--classifier] <classifier>
```

There are two classifiers implemented currently:

* [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
* [LeNet](http://yann.lecun.com/exdb/lenet/) Convolutional Neural Network

Default classifier is k-nearest-neighbors.

i.e.

``` bash
python sum_digits.py -i images/img-0.png -c knn

# => Sum: 107.0

python sum_digits.py -i images/img-1.png -c cnn

# => Sum: 88.0
```

For help, run:

``` bash
python sum_digits.py -h [--help]
```

# Algorithm

Assumption is that digits on input images are part of [ MNIST ](http://yann.lecun.com/exdb/mnist/) dataset.
We can train our classification models with full MNIST dataset (70000 digits).

MNIST dataset is fetched from sklearn repo and cached locally.

Model is saved after training so next time we need to use our model we just load
it from file. (In case of CNN we are saving weights to `*.hdf5` file)

KNN model is saved to `knn/knn_model.pkl`
CNN weights are saved to `neural_net/weights.hdf5`

## Image preprocessing

Loaded images are converted to grayscale and to binary afterwards.

We use `skimage.measure.regionprops` to get properties of each labelled connected region.
Using region properties we crop MNIST handwritten digits from the original image
and pass it to our pretrained classifier. Results are predicted digits which are simply summed.

# Results

Because we are training our models on same dataset which we are predicting,
success rate is ~100%.

Response time of KNN is ~2 sec/image where CNN gives < 0.2 sec/image.
Also, after extensive testing CNN proved to give better predictions.
