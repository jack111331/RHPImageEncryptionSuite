from utility import *
import numpy as np

def forward_and_backward_substitution_reverse(img, x_0, alpha, beta):
    x = x_0
    img_size = img.shape
    for row in range(img_size[0]*2-1, -1, -1):
        for col in range(img_size[1]*2-1, -1, -1):
            if row == 0 and col == 0:
                break
            x = generate_abm(x, alpha, beta)

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

    x_list_forward = []
    x_list_backward = []
    for i in range(img_size[0] * img_size[1]-1, 0, -1):
        x = generate_abm(x, alpha, beta)
        x_list_forward.append(x)

    for i in range(1, img_size[0] * img_size[1]):
        x = generate_abm(x, alpha, beta)
        x_list_backward.append(x)

    for i in range(1, img_size[0] * img_size[1]):
        cur_row, cur_col = int(i//img_size[1]), int(i%img_size[1])
        prev_row, prev_col = int((i-1)//img_size[1]), int((i-1)%img_size[1])
        xor_value = int(int(round(x_list_backward[len(x_list_backward)-i] * (10**14))) % 256)
        img[prev_row][prev_col] = float(int(img[prev_row][prev_col]) ^ (t_list[s_list[int(img[cur_row][cur_col])]]) ^ xor_value)

    for i in range(img_size[0] * img_size[1]-1, 0, -1):
        row, col = int(i//img_size[1]), int(i%img_size[1])
        prev_row, prev_col = (i-1)//img_size[1], (i-1)%img_size[1]
        xor_value = int(int(round(x_list_forward[i-1] * (10**14))) % 256)
        img[row][col] = float(int(img[row][col]) ^ (s_list[t_list[int(img[prev_row][prev_col])]]) ^ xor_value)
    
    return img, x

def random_hamiltonian_path_reverse(img, swap_order):
    img_size = img.shape
    count = len(swap_order)
    for row in range(0, img_size[0]):
        for col in range(0, img_size[1]):
            if(row == 0 and col == 0):
                continue
            swap_row = swap_order[count-1][0]
            swap_col = swap_order[count-1][1]
            img[swap_row][swap_col], img[row][col] = img[row][col], img[swap_row][swap_col]
            count -= 1

    return img