from utility import *
from decomposition import *

def encryption(img, x_0, alpha, beta):
	x = x_0
	shuffled_img = decompositon(img)
	print("Decomposed")
	shuffled_img, x, hamiltonian_swap_order = random_hamiltonian_path(shuffled_img, x, alpha, beta)
	print("Shuffled")
	shuffled_img = compose(shuffled_img)
	print("Composed")
	encrypted_img, x = forward_and_backward_substitution(shuffled_img, x, alpha, beta)
	print("Substituded")
	return encrypted_img, hamiltonian_swap_order