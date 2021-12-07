import cv2
import numpy as np
import matplotlib.pyplot as plt
from globals import classes,classes_de

def get_partitions(img, dim):
    dims = [3, 4, 5, 6]
    partitions = []
    for i in range(len(dims)):
        if dim % dims[i] == 0:
            division = dims[i]
            gap = dim//dims[i]
            for j in range(dims[i]+1):
                partitions.append(gap*j)
            partitions[-1] -= 1
            return partitions, division


def img2grid(img):
    h, w, channels = img.shape
    x, rows = get_partitions(img, h)
    y, columns = get_partitions(img, w)
    # plt.imshow(img)
    grid = []
    for i in range(len(x)-1):
        for j in range(len(y)-1):
            grid.append(img[x[i]:x[i+1], y[j]:y[j+1]])
    grid = np.array(grid)
    return grid, rows, columns


def visualise(img):
    grid_no = 0
    grid, rows, columns = img2grid(img)
    print(grid.shape)
    for i in range(rows):
        for j in range(columns):
            plt.subplot(rows, columns, grid_no+1)
            plt.imshow(grid[grid_no])
            grid_no += 1
    plt.show()


def hello(output,dic):
    grids_array, rows, columns = img2grid(output)
   
    grid = grids_array
    grid_no = 0
    total_area = columns*rows
    for x in range(rows):
        for y in range(columns):

        # converting 3d image to 2d grayscale
            grids_array[grid_no] = grids_array[grid_no][:, :, 0]
        # 2d to 1d
            flat_list = list(grids_array[grid_no].flatten())

            count = flat_list.count(255.0)
            if (count/total_area)>0.2:
                dic[classes_detected[i]].append(grid_no)
            grid_no += 1
    result = {}
    for clas in dic.keys():
        result[classes[clas]] = list(set(dic[clas]))
    
    return result
