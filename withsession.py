import tensorflow as tf
a = tf.constant(3)      #常量3
b = tf.constant(4)      #常量4
with tf.Session() as sess:
    print("add: %i" %sess.run(a+b))
    print("mutiple: %i" %sess.run(a*b))