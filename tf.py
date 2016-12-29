import tensorflow as tf
import numpy as np

x = tf.constant(np.random.randint(1000, size=5), name='x')
y = tf.Variable(tf.add_n(x), name='y')


with tf.Session() as session:
    merged = tf.merge_all_summaries()
    writer = tf.train.SummaryWriter("/tmp/basic123", session.graph_def)
    model = tf.initialize_all_variables()
    session.run(model)
    print session.run(y)
    #for i in range(5):
    #    session.run(model)
    #    x = x + np.random.randint(1000)
    #    y = x/(i + 1)
    #    print session.run(y)

#print tf.Session().run(y)
