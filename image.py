import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import tensorflow as tf

pic = "pic.jpg"
image = mpimg.imread(pic)
height, width, depth = image.shape

x = tf.Variable(image, name='x')
model = tf.initialize_all_variables()

with tf.Session() as session:
    x = tf.transpose(x, perm=[1,0,2])
    x = tf.reverse(x, [False, True, False], name='m')
    session.run(model)
    result = session.run(x)

plt.imshow(result)
plt.show()
