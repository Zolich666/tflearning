import tensorflow as tf
a = tf.placeholder(tf.int16)    #占位符
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b)
with tf.Session() as sess:
    #计算
    print("add: %i" % sess.run(add, feed_dict = {a: 3, b: 4}))
    print("multiply: %i" % sess.run(mul, feed_dict = {a: 3, b: 4}))

    print(sess.run([mul, add], feed_dict = {a: 3, b: 4}))
