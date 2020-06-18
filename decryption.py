from reverse import *
from decomposition import *

def decryption(img, x_0, alpha, beta, hamiltonian_swap_order):
	x = x_0
	decryption_img, x = forward_and_backward_substitution_reverse(img, x, alpha, beta)
	print('Substituded reverse')
	shuffled_img = decompositon(decryption_img)
	print('Decomposed')
	shuffled_img = random_hamiltonian_path_reverse(shuffled_img, hamiltonian_swap_order)
	print('Shuffled reverse')
	original = compose(shuffled_img)
	print("Composed")
	return original
