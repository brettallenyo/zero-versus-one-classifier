import AnalyzeImage
import numpy as np
import os
import Image
import pickle

class Train:

	# Pass in zeros and ones, lists of images
	def __init__(self, zeros, ones):
		self.zeros = zeros
		self.ones = ones
		self.data = self.create_data()
		self.labels = self.create_labels()
		self.perceptron()

	def create_data(self):
		data = []
		for i in range(len(self.zeros)):
			toAdd = AnalyzeImage.Analyze.averages(self.zeros[i])
			if(i == 0):
				data = toAdd
			else:
				data = np.append(data, toAdd, 1)

		for i in range(len(self.ones)):
			toAdd = AnalyzeImage.Analyze.averages(self.ones[i])
			data = np.append(data, toAdd, 1)
		return data

	def create_labels(self):
		labels = []
		for i in range(len(self.zeros)):
			toAdd = np.array([[-1]])
			if(i == 0):
				labels = toAdd
			else:
				labels = np.append(labels, toAdd, 1)

		for i in range(len(self.ones)):
			toAdd = np.array([[1]])
			labels = np.append(labels, toAdd, 1)
		return labels

	def perceptron(self):
		T = 10000
		theta = np.zeros((1, len(self.data)))
		theta0 = np.array([0])
		for t in range(T):
			wrongs = 0
			for i in range(len(self.data[0])):
				x_val = self.data[:,i:i+1]
				if((theta.dot(x_val)+theta0)*self.labels[0][i] <= 0):
					theta = theta + self.labels[0][i]*self.data[:,i:i+1].T
					theta0 = theta0 + self.labels[0][i]
					wrongs += 1
			if(wrongs == 0):
				print(1)
				break
		theta.shape = (len(self.data), 1)
		theta0.shape = (1,1)
		pickle.dump(theta, open("theta.p", "wb"))
		pickle.dump(theta0, open("theta0.p", "wb"))


if __name__ == '__main__':

	rootdir = '/Users/brettallen/Documents/CodingProjects/zero-versus-one/TrainOnes'
	one_images = []
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			one_images.append(Image.Image.load(os.path.join(subdir, file)))

	rootdir = '/Users/brettallen/Documents/CodingProjects/zero-versus-one/TrainZeros'
	zero_images = []
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			zero_images.append(Image.Image.load(os.path.join(subdir, file)))

	train = Train(zero_images, one_images)