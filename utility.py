
def twoD2oneD(row, col, width):
	return row * width + col

def oneD2twoD(ind, width):
	return ind // width, ind % width

def generate_abm(x_0, alpha, beta):
	assert type(x_0) != 'double' or type(alpha) != 'double' or type(beta) != 'double', 'generate_abm(): parameter type error'
	return beta * (alpha * x_0 % 1) % 1

def random_hamiltonian_path(img, x_0, alpha, beta):
	img_size = img.shape
	x = x_0
	for row in range(img_size[0]-1, -1, -1):
		for col in range(img_size[1]-1, -1, -1):
			x = generate_abm(x, alpha, beta)
			swap_row, swap_col = oneD2twoD(round(x * (10**14)) % twoD2oneD(row, col, img_size[0]))
			img[swap_row][swap_col], img[row][col] = img[row][col], img[swap_row][swap_col]

	return img, x
