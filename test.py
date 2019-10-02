import pickle
import numpy as np
import Image
import os
import AnalyzeImage

'''
x = np.array([1,2,3])
print(type(x))
print(x)
pickle.dump(x, open("save.p", "wb"))

y = pickle.load(open("save.p", "rb"))

print(type(y))
print(y)
'''

'''
x = [1, 2, 3, 4]
y = np.reshape(x, (len(x), 1))
print(y)
'''


rootdir = '/Users/brettallen/Documents/CodingProjects/zero-versus-one/OneImages'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(AnalyzeImage.Analyze.averages(Image.Image.load(os.path.join(subdir, file))))


print("--------------------------------------------")

rootdir1 = '/Users/brettallen/Documents/CodingProjects/zero-versus-one/ZeroImages'

for subdir, dirs, files in os.walk(rootdir1):
    for file in files:
        print(AnalyzeImage.Analyze.averages(Image.Image.load(os.path.join(subdir, file))))