# Run this cell to see how Pylab plots graphs
import pylab as pyl
'''
Xs = [0, 1, 2]
Ys = [1.2, 2.2, 1.8]
pyl.plot(Xs,Ys)
pyl.show()
'''
# Multiple figures are displayed in this case (first two figures below)
print("Multiple figures")
Xs = [0, 1, 2]
Ys1 = [1.2, 2.2, 1.8]
Ys2 = [1.5, 2.0, 2.6]
pyl.plot(Xs, Ys1)
pyl.figure()
pyl.plot(Xs, Ys2)
pyl.show()

print("\n", "Subplot function")
# One figure containing multiple graphs displayed (last figure)
Xs = [0, 1, 2]
Ys1 = [1.2, 2.2, 1.8]
Ys2 = [1.5, 2.0, 2.6]
pyl.subplot(211)
pyl.plot(Xs, Ys1)
pyl.subplot(212)
pyl.plot(Xs, Ys2)
pyl.show()