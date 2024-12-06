import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(test_images.shape, train_labels.shape)
train_images = np.concatenate((train_images, test_images), axis=0)
train_labels = np.concatenate((train_labels, test_labels), axis=0)
train_images = train_images/255
test_images = test_images/255 
print(test_images.shape, test_labels.shape)

print(len(train_images), len(train_images))
i=60234
plt.figure()
plt.imshow(train_images[i], cmap=plt.cm.binary)
plt.xlabel(train_labels[i])
plt.show()