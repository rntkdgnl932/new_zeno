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
    import pyautogui
    from function import click_pos_2, click_pos_reg, text_check_get, in_number_check, int_put_
    from jadong_zeno import jadong_start
    from action_zeno import gold_check_open, out_check, now_hunting, get_items, clean_screen, character_change, confirm_all
    from server import server_get_version, server_get_zeno
    from potion_zeno import juljun_potion_check, juljun_maul_potion
    from realtime import collection, boonhae, chango_in, all_realtime
    from settings import chago_setting, chago_drag
    cla = "three"
    v_.now_cla = cla

    # chago_drag(160, 690, 160, 170, cla) 

    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\zenonia_start_ready.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(0, 0, 960, 1030, v_.now_cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("매크로를 내려야 실행됨...10초")
    else:
        print("매크로 제목 안 보여")
    #
    #(50, 370, 320, 730, cla, img, 0.85)
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\chango\\guisok.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(50, 370, 270, 360), confidence=0.8):
    #     # for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 945 + plus, 985),
    #     #                                      confidence=0.7):
    #     last_x = i.left
    #     last_y = i.top
    #     print("last_x", last_x)
    #     print("last_y", last_y)




