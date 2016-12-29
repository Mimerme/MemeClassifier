from sklearn import tree
import tensorflow
#Features of the apples/oranges
# 0 - bumpy : 1 - smooth
features = [[140,1],[130,1],[150,0],[170,0]]
#The actual object
#0 - apple : 1 - orange
lables = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf.fit(features, lables)
print clf.predict([[160, 0]])
