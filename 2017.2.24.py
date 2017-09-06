import tensorflow as tf

# hello = tf.constant("hello world")
#
# sess = tf.Session()
#
#
# print(hello)
# print(sess.run(hello))
#
# a = tf.constant(2)
# b = tf.constant(3)
#
# c = a + b
#
# print(c)
# print(sess.run(c))

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.multiply(a, b)

with tf.Session() as sess:
    print("addition with variables %i" % sess.run(add, feed_dict={a : 2, b : 3}))
    print("multiplication with variables %i" % sess.run(mul, feed_dict={a : 2, b : 5}))


