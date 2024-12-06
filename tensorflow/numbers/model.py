import numpy as np
import tensorflow as tf
def create()->tf.keras.Sequential:
    mnist = tf.keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    # объединим 2 массива 
    train_images = np.concatenate((train_images, test_images), axis=0)
    train_labels = np.concatenate((train_labels, test_labels), axis=0)

    train_images = train_images/255
    test_images = test_images/255 
    
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])
    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=10)
    #model.save('model.h5')
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

    print('Test accuracy:', test_acc)
    probability_model.save('model.h5')
create()