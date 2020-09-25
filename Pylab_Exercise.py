import pylab as pyl
x = []
y = []
z = []

t = 2**6
print(t)
for i in range(21):
    x.append(i)
print(x)

for i in x:
    f_x = i*i + 20
    y.append(f_x)
print(y)

for i in x:
    g_x = (i/2)**3 - 100
    z.append(g_x)

pyl.subplot(211)
pyl.plot(x, y)

pyl.subplot(212)
pyl.plot(x, z)
pyl.show()