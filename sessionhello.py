import tensorflow as tf
hello = tf.constant('Hello, Tensorflow!')   #constant是tf 的常量
sess = tf.Session()                         #建立session
print(sess.run(hello))                      #用run来运行， 直接print(hello)是不行的
#print(hello)
sess.close()                                #关闭sess