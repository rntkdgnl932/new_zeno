import sys
import time
import requests

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_
import cv2
import numpy as np
from function import imgs_set_

def go_test():
    print("tst")

    from function import click_pos_2, click_pos_reg, text_check_get, in_number_check, int_put_
    from jadong_zeno import jadong_start
    from action_zeno import gold_check_open, out_check, now_hunting, get_items, clean_screen, character_change, confirm_all
    from server import server_get_version, server_get_zeno
    from potion_zeno import juljun_potion_check, juljun_maul_potion
    from realtime import collection, boonhae, chango_in, all_realtime
    cla = "three"
    v_.now_cla = cla


    character_change(cla, 1)





