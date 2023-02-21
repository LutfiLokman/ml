import tensorflow as tf
from tensorflow.keras.datasets import imdb

top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load.data(num_words=top_words)
