from suite import *
import numpy as np

x_0 = np.double(0.123456789)
alpha = np.double(10.45678)
beta = np.double(10.123)

img = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)
encrypted_img = encryption(img, x_0, alpha, beta)
cv2.imwrite('encrypted.png', encrypted_img)
