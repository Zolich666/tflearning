import tensorflow as tf
import pylab

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot =True)

#print('输入数据：', mnist.train.images)
#print('输入数据打shape：', mnist.train.images.shape)
# im = mnist.train.images[2]
# im = im.reshape(-1,28)
# pylab.imshow(im)
# pylab.show()

tf.reset_default_graph()
#定义占位符
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
