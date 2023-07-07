import sys


sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_
import cv2
import numpy as np
from function import imgs_set_

def go_test():
    print("tst")

    from function import click_pos_2, click_pos_reg

    cla = "three"

    click_pos_2(920, 100, cla)




