# import scipy.misc as misc
#
# img = misc.imread('catcat.jpeg')
#
# print(img.dtype, img.shape)
#
#
# imgTinted = img * [1, 0.1, 0.1]
# imgTinted = misc.imresize(imgTinted, (300, 300))
#
# misc.imsave('catcat_tinted.jpeg', imgTinted)
#

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('sine and cosine')
# plt.legend(['sine', 'cosine'])
# plt.show()




# subplot 활용하기
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# plt.subplot(2, 1, 1)
# plt.plot(x, y_sin)
# plt.title('sine')
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('cosine')
#
# plt.show()



# image 로 나타내보기
import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('catcat.jpeg')
img_tinted = img * [1, 0.65, 0.6]

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))
plt.show()
