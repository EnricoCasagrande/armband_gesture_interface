import glob
import numpy as np
from keras.utils import to_categorical

csv = './data/train_data_set.csv'
npz = './data/train_set.npz'

filenames = glob.glob("./data/dataset-*-*.csv")

with open(csv, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

x = np.loadtxt(csv, delimiter=';', usecols=list(range(0, 64)))
y = to_categorical(np.loadtxt(csv, delimiter=';', usecols=64))

print(x)
print(y)

np.savez(npz, x=x, y=y)  
