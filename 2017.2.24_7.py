import numpy as np
import tensorflow as tf

xy = np.loadtxt('train.txt', unpack=True, dtype='float32')
x_data = xy[0:-1]
y_data = xy[-1]

print(x_data)
print(y_data)


# x_data = [[1, 1, 1, 1, 1], # 첫 번째 element를 b로 만든다.
#         [0., 2., 0., 4., 0.],
#         [1., 0., 3., 0., 5.]]
# y_data = [1, 2, 3, 4, 5]

W = tf.Variable(tf.random_uniform([1, 3], -1.0, 1.0))
#b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

hypothesis = tf.matmul(W, x_data)# + b

cost = tf.reduce_mean(tf.square(hypothesis - y_data))

a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W))#, sess.run(b))
              #sess.run(W1), sess.run(W2), sess.run(b))


