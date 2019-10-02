
import numpy as np
import Image
import math
import pickle
import os

class Analyze:

	def __init__(self, im):
		self.image = im
		self.th = pickle.load(open("theta.p", "rb"))
		self.th0 = pickle.load(open("theta0.p", "rb"))
		self.averages = Analyze.averages(self.image)

	def get_splits(im, num_splits):
		row_cutoffs = []
		col_cutoffs = []
		for i in range(num_splits+1):
			row_cutoffs.append(math.floor(im.height*i/num_splits))
			col_cutoffs.append(math.floor(im.width*i/num_splits))
		return (row_cutoffs, col_cutoffs)

	def averages(im):
		averages = []
		row_cutoffs,col_cutoffs = Analyze.get_splits(im, 3)
		for row in range(3):
			for col in range(3):
				averages.append(im.get_average(row_cutoffs[row], col_cutoffs[col], row_cutoffs[row+1], col_cutoffs[col+1]))
		return np.reshape(averages, (len(averages), 1))

	'''
	averages must be a numpy array of shape (4,1)
	th must be the same type and shape as averages
	th0 must be a numpy array of shape (1,1)
	'''
	def calc_val(averages, th, th0):
		return np.dot(th.T, averages) + th0

	def analyze(self):
		if(Analyze.calc_val(self.averages, self.th, self.th0) > 0):
			return 1
		else:
			return 0


if __name__ == '__main__':
	'''
	im = Image.Image.load('/Users/brettallen/Documents/CodingProjects/zero-versus-one-classifier/TestZeros/NotesZero.png')
	analytics = Analyze(im)
	print(analytics.analyze())

	im = Image.Image.load('/Users/brettallen/Documents/CodingProjects/zero-versus-one-classifier/TestOnes/NotesOne.png')
	analytics = Analyze(im)
	print(analytics.analyze())
	'''
	failed = []

	rootdir = '/Users/brettallen/Documents/CodingProjects/zero-versus-one-classifier/TestZeros'
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			analytics = Analyze(Image.Image.load(os.path.join(subdir, file)))
			if(analytics.analyze() != 0):
				failed.append(file)

	rootdir = '/Users/brettallen/Documents/CodingProjects/zero-versus-one-classifier/TestOnes'
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			analytics = Analyze(Image.Image.load(os.path.join(subdir, file)))
			if(analytics.analyze() != 1):
				failed.append(file)

	if(len(failed) == 0):
		print("All tests passed!")
	else:
		print(str(len(failed)) + " failures: " + str(failed))
	
