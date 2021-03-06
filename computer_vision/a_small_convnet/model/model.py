from keras import layers
from keras import models


class Model:

    """Sequential groups linear stack of layers into a `tf.keras.Model`.
    is the most common way of layers.
    The Functional api the the other way for undirected acycle graphs to
    build arbitrary architectures(very advanced)
    """
    model = models.Sequential()
    """ Images are in RGB => three features => three layers each of 28x28 = hxw
    (3,3) patches size ,32 = output feature map /features/filters/channels
    """
    def __init__(self):
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1),
                                     strides=(1, 1), padding='valid'))
        """
        MaxPool2D: It is basically used to down sample the data.
        Reduce the size of the image because the larger number
        of pixels contribute to more parameters which can involve large chunks of data.
        Thus we need less parameters such that a CNN can still identify the image.
        Choose or the Max  - most of the times -  or less the the Average.
        """
        self.model.add(layers.MaxPool2D(2, 2))  # downsample feature maps by two
        """[in keras]The second layer did n’t receive an input shape argument—instead,
        it automatically inferred its input shape as being the output
        shape of the layer that came before.
        """
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu', strides=(1, 1), padding='valid'))
        self.model.add(layers.MaxPool2D(2, 2))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu', strides=(1, 1), padding='valid'))

        """The output of every Conv2D and MaxPooling2D layer is a 3D tensor of
        shape (height, width, channels). 
        The width and height dimensions tend to shrink as we go deeper.
        The number of channels is controlled by the first argument passed to 
        the Conv2D layers (32 or 64).
        Feed the last output tensor (of shape (3, 3, 64) ) into a densely
        connected classifier network: a stack of Dense layers, they process vectors. so
        we flatten 3D tensor to 1D before.
        
        Convolution (Conv2D) layers learn local patterns
        Dense layers learn global patterns
        """
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(10, activation='softmax'))
        self.model.summary()
