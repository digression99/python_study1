#deep learning
import tensorflow as tf
import matplotlib.pyplot as plt

X = [1., 2., 3.]
Y = [1., 2., 3.]

m = n_samples = len(X)
W = tf.placeholder(tf.float32)

hypothesis = tf.multiply(X, W)

cost = tf.reduce_sum(tf.pow(hypothesis - Y, 2)) / (m)

init = tf.global_variables_initializer()

W_val = []
cost_val = []

sess = tf.Session()
sess.run(init)

for i in range(-30, 50):
    i2 = i * 0.1
    print(i2, sess.run(cost, feed_dict={W:i2}))
    W_val.append(i2)
    cost_val.append(sess.run(cost, feed_dict={W:i2}))

plt.plot(W_val, cost_val, 'ro')
plt.ylabel('cost')
plt.xlabel('W')
plt.show()
