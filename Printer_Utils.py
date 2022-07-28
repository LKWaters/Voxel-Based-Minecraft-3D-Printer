import numpy as np
import collections
from pynput.mouse import Controller as Controller
from pynput.mouse import Button
from pynput.keyboard import Controller as Controller2
from pynput.keyboard import Key
import time

Cont = Controller()
Cont2 = Controller2()


def Voxel2Array(Voxel_main):

    voxels = Voxel_main
    # Map and sort the values
    x_map_d = {}
    y_map_d = {}
    z_map_d = {}

    for item in voxels.points:
        x_map_d[item[0]] = 0
        y_map_d[item[1]] = 0
        z_map_d[item[2]] = 0

    x_map_d = collections.OrderedDict(sorted(x_map_d.items()))
    y_map_d = collections.OrderedDict(sorted(y_map_d.items()))
    z_map_d = collections.OrderedDict(sorted(z_map_d.items()))

    # Map the point values to "block" values by mapping to incrementing integers with incrementing float values
    x_count = 0
    for items in x_map_d:
        x_map_d[items] = x_count
        x_count = x_count + 1

    y_count = 0
    for items in y_map_d:
        y_map_d[items] = y_count
        y_count = y_count + 1

    z_count = 0
    for items in z_map_d:
        z_map_d[items] = z_count
        z_count = z_count + 1

    # Create a 3D array representing the block values in MC
    bin_arr = np.zeros((x_count, y_count, z_count))
    for x in range(0, len(voxels.points)):
        x_pos = x_map_d[voxels.points[x][0]]
        y_pos = y_map_d[voxels.points[x][1]]
        z_pos = z_map_d[voxels.points[x][2]]
        bin_arr[x_pos, y_pos, z_pos] = 1

    return bin_arr

def TP(x,y,z):

    Cont2.press('t')
    time.sleep(0.01)
    Cont2.release('t')
    time.sleep(0.05)

    for item in '/tp ' + str(x) + ' ' + str(y) + ' ' + str(z):
        Cont2.press(item)
        time.sleep(0.02)
        Cont2.release(item)
        time.sleep(0.02)

    Cont2.press(Key.enter)
    time.sleep(0.01)
    Cont2.release(Key.enter)

def Down():
    for temp in range(0, 10):
        Cont.move(0, 1000)
        time.sleep(0.2)

def Up():
    for temp in range(0, 10):
        Cont.move(0, -1000)
        time.sleep(0.2)

def CheckSum(vec):
    if sum(vec) == 0:
        return True
    else:
        return False




def Place(blank_count, x, y, z, arr, start_x, start_y, start_z):
    if arr[x,z,y] == 1:
        if not blank_count == 0:
            TP(start_x+x,start_y+y,start_z+z)
            Down()

            Cont2.press('1')
            time.sleep(0.05)
            Cont2.release('1')

        Cont2.press(Key.space)
        time.sleep(0.1)
        Cont2.release(Key.space)
        time.sleep(0.1)
        Cont.press(Button.right)
        time.sleep(0.1)
        Cont.release(Button.right)
        time.sleep(0.2)

        return 0

    elif blank_count == 0:
        Cont2.press('2')
        time.sleep(0.05)
        Cont2.release('2')

        Cont.press(Button.right)
        time.sleep(0.1)
        Cont.release(Button.right)
        time.sleep(0.1)

        return 1

    elif blank_count == 1:

        Cont2.press(Key.shift)
        time.sleep(0.2)
        Cont.press(Button.right)
        time.sleep(0.1)
        Cont.release(Button.right)
        time.sleep(0.1)
        Cont2.release(Key.shift)

        return 2

    elif blank_count == 2:
        Up()
        Cont.press(Button.right)
        time.sleep(0.1)
        Cont.release(Button.right)
        time.sleep(0.1)

        return 3

    else:
        Cont.press(Button.right)
        time.sleep(0.1)
        Cont.release(Button.right)
        time.sleep(0.1)

        return blank_count + 1

