import numpy as np
def twoD2oneD(row, col, width):
	return row * width + col

def oneD2twoD(ind, width):
	return int(ind // width), int(ind % width)

def generate_abm(x_0, alpha, beta):
	assert type(x_0) != 'numpy.float64' or type(alpha) != 'numpy.float64' or type(beta) != 'numpy.float64', 'generate_abm(): parameter type error'
	return beta * (alpha * x_0 % 1) % 1

def random_hamiltonian_path(img, x_0, alpha, beta):
	img_size = img.shape
	x = x_0
	for row in range(img_size[0]-1, -1, -1):
		for col in range(img_size[1]-1, -1, -1):
			if row == 0 and col == 0:
				break
			x = generate_abm(x, alpha, beta)
			swap_row, swap_col = oneD2twoD(int(round(x * (10**14))) % twoD2oneD(row, col, img_size[1]), img_size[1])
			img[swap_row][swap_col], img[row][col] = int(img[row][col]), int(img[swap_row][swap_col])

	return img, x

def forward_and_backward_substitution(img, x_0, alpha, beta):
	x = x_0
	s_list = [i for i in range(256)]
	for i in range(255, 0, -1):
		x = generate_abm(x, alpha, beta)
		swap_index = int(int(round(x * (10**14))) % i)
		s_list[i], s_list[swap_index] = s_list[swap_index], s_list[i]
	t_list = [i for i in range(256)]
	for i in range(255, 0, -1):
		x = generate_abm(x, alpha, beta)
		swap_index = int(int(round(x * (10**14))) % i)
		t_list[i], t_list[swap_index] = t_list[swap_index], t_list[i]

	img_size = img.shape
	for i in range(1, img_size[0] * img_size[1]):
		row, col = int(i//img_size[1]), int(i%img_size[1])
		prev_row, prev_col = (i-1)//img_size[1], (i-1)%img_size[1]
		x = generate_abm(x, alpha, beta)
		xor_value = int(int(round(x * (10**14))) % 256)
		img[row][col] = float(int(img[row][col]) ^ (s_list[t_list[int(img[prev_row][prev_col])]]) ^ xor_value)

	for i in range(img_size[0] * img_size[1]-1, 0, -1):
		cur_row, cur_col = int(i//img_size[1]), int(i%img_size[1])
		prev_row, prev_col = int((i-1)//img_size[1]), int((i-1)%img_size[1])
		x = generate_abm(x, alpha, beta)
		xor_value = int(int(round(x * (10**14))) % 256)
		img[prev_row][prev_col] = float(int(img[prev_row][prev_col]) ^ (t_list[s_list[int(img[cur_row][cur_col])]]) ^ xor_value)

	return img, x

