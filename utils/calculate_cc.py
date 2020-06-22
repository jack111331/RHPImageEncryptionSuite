import cv2
import numpy as np
import matplotlib.pyplot as plt

def hor_adjancy_corr_pixel(img):
	img_size = img.shape
	x1 = img[:,1:img.shape[1]-1]
	y1 = img[:,2:img.shape[1]]
	print(x1[:])
	plt.scatter(x1, y1, s=1)
	plt.title("Horizontal Scatter Plot")
	plt.show()
	all_x1 = x1.flatten()
	all_y1 = y1.flatten()
	return np.corrcoef(all_x1,all_y1)[1,0]	

def ver_adjancy_corr_pixel(img):
	img_size = img.shape
	x1 = img[1:img.shape[0]-1,:]
	y1 = img[2:img.shape[0],:]
	plt.scatter(x1, y1, s=1)
	plt.title("Vertical Scatter Plot")
	plt.show()
	all_x1 = x1.flatten()
	all_y1 = y1.flatten()
	return np.corrcoef(all_x1,all_y1)[1,0]	

def diag_adjancy_corr_pixel(img):
	img_size = img.shape
	x1 = img[1:img_size[0]-1,1:img_size[1]-1]
	y1 = img[2:img_size[0],2:img_size[1]]
	plt.scatter(x1, y1, s=1)
	plt.title("Diagonal Scatter Plot")
	plt.show()
	all_x1 = x1.flatten()
	all_y1 = y1.flatten()
	return np.corrcoef(all_x1,all_y1)[1,0]	

def a_diag_adjancy_corr_pixel(img):
	img_size = img.shape
	x1 = img[2:img_size[0],1:img_size[1]-1]
	y1 = img[1:img_size[0]-1,2:img_size[1]];
	plt.scatter(x1, y1, s=1)
	plt.title("Anti-Diagonal Scatter Plot")
	plt.show()
	all_x1 = x1.flatten()
	all_y1 = y1.flatten()
	return np.corrcoef(all_x1,all_y1)[1,0]	


n = 1
img = cv2.imread("image_1.jpg", cv2.IMREAD_GRAYSCALE)
horizontal = hor_adjancy_corr_pixel(img)
print("Horizontal corelation coefficient:", horizontal)
vertical = ver_adjancy_corr_pixel(img)
print("Vertical corelation coefficient:", vertical)
diagonal = diag_adjancy_corr_pixel(img)
print("Diagonal corelation coefficient:", diagonal)
anti_diagonal = a_diag_adjancy_corr_pixel(img)
print("Anti-Diagonal corelation coefficient:", anti_diagonal)
