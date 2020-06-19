from suite import *
from decryption import *
import numpy as np

x_0 = np.double(0.123456789)
alpha = np.double(10.45678)
beta = np.double(10.123)

img = cv2.imread("image_1.jpg", cv2.IMREAD_GRAYSCALE)
encrypted_img, hamiltonian_swap_order = encryption(img, x_0, alpha, beta)
cv2.imwrite('encrypted.png', encrypted_img)

encrypted_img = cv2.imread("encrypted.png", cv2.IMREAD_GRAYSCALE)
decrypted_img = decryption(encrypted_img, x_0, alpha, beta, hamiltonian_swap_order)
cv2.imwrite('decrypted.png', decrypted_img)