import numpy as np
import matplotlib.pyplot as plt


print("hello world!")

plt.xlabel('CNN Layer')
plt.ylabel('Accurate')
plt.xticks(np.arange(1, 17, 1))
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y = [0.62, 0.70, 0.73, 0.78, 0.82, 0.86, 0.93, 0.97, 0.97, 0.945, 0.92, 0.90, 0.89, 0.87, 0.86, 0.858]
plt.plot(x, y, '-o')
plt.show()

# plt.xlabel('Number of sketch samples')
# plt.ylabel('Accurate')
# plt.xticks(np.arange(1, 11, 1))
#
# #x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [0.54, 0.58, 0.60, 0.64, 0.672, 0.711, 0.731, 0.753, 0.761, 0.781]


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# y2000 = [0.52, 0.55, 0.58, 0.63, 0.65, 0.68, 0.70, 0.745, 0.78, 0.776, 0.763, 0.750, 0.73, 0.701, 0.684, 0.681]
# y4000 = [0.58, 0.601, 0.629, 0.651, 0.683, 0.721, 0.75, 0.79, 0.83, 0.831, 0.812, 0.781, 0.751, 0.731, 0.723, 0.731]
# y6000 = [0.61, 0.651, 0.701, 0.731, 0.783, 0.822, 0.853, 0.881, 0.921, 0.941, 0.962, 0.948, 0.902, 0.861, 0.841, 0.842]
# y8000 = [0.623, 0.732, 0.781, 0.821, 0.862, 0.901, 0.953, 0.973, 0.962, 0.931, 0.892, 0.861, 0.853, 0.842, 0.843, 0.844]
# y10000 = [0.682, 0.762, 0.821, 0.882, 0.941, 0.9729, 0.965, 0.952, 0.9412, 0.932, 0.912, 0.891, 0.878, 0.871, 0.867, 0.857]
#
# plt.figure()
# plt.xlabel('CNN Layer')
# plt.ylabel('Accurate')
# plt.xticks(np.arange(1, 17, 1))
# plt.yticks(np.arange(0.5, 1.1, 0.05))
#
# l1, = plt.plot(x, y2000, '-bo')
# l2, = plt.plot(x, y4000, '--gp')
# l3, = plt.plot(x, y6000, '-.r*')
# l4, = plt.plot(x, y8000, ':y+')
# l5, = plt.plot(x, y10000, '-.kx')
#
# plt.legend([l1, l2, l3, l4, l5], ['2000', '4000', '6000', '8000', '10000'], loc='lower right')
# plt.show()

#x = [2, 4, 6, 8, 10]
#y_SIFT = [0.57, 0.60, 0.65, 0.70, 0.70]
#y_MLBP = [0.7041, 0.8031, 0.9032, 0.9423, 0.9427]
#y_AMLBP = [0.7341, 0.8131, 0.9332, 0.9623, 0.9627]
#y_SIFT_MLBP = [0.7831, 0.8321, 0.9021, 0.9732, 0.9733]
#y_JDA = [0.54, 0.60, 0.672, 0.731, 0.781]
#y_JDA_CNN = [0.78, 0.86, 0.9721, 0.9732, 0.9745]

#plt.figure()
#plt.xlabel('Number of sketch samples')
#plt.ylabel('Accurate')
#plt.xticks(np.arange(0, 12, 2))
#plt.yticks(np.arange(0.5, 1.1, 0.05))

#l1, = plt.plot(x, y_SIFT, '-bo')
#l2, = plt.plot(x, y_MLBP, '--gp')
#l3, = plt.plot(x, y_AMLBP, '--cv')
#l4, = plt.plot(x, y_SIFT_MLBP, '-.r*')
#l5, = plt.plot(x, y_JDA, ':y+')
#l6, = plt.plot(x, y_JDA_CNN, '-.kx')

#plt.legend([l1, l2, l3, l4, l5, l6], ['SIFT', 'MLBP', 'AMLBP', 'SIFT+MLBP', 'JDA', 'JDA+CNN'], loc='lower right')
#plt.show()

# ax = plt.gca()
# ax.xaxis.get_major_formatter().set_powerlimits((0, 2))

# plt.plot(x, y, '-r*')
# plt.show()


# group, labels = KNN.createDataSet()
#
# print(group)
# print(labels)
#
# a = [1,2,3]
# b = tile(a,(6,1))
#
# c = [[1,2,3],[4,5,6]]
# print(len(c[0]))
# print(b)

# datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
# print(datingLabels[0:20])
# plt.show()

# print(datingDataMat[0:20])
# print(datingLabels[0:20])

#print(kNN.datingClassTest())
#print(kNN.classiyfyPerson())

#print(kNN.handwritingClassTest())

# xArr, yArr = regression.loadDataset('ex0.txt')
# ws = regression.standRegres(xArr,yArr)
# xMat = mat(xArr)
# yMat = mat(yArr)
#
# print(xMat[:,1].flatten().A[0])

# print(xMat[:,1])

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(xMat[:,1].flatten().A[0], yMat.flatten().A[0])

#print(ws)
#print(xArr[0:2])
