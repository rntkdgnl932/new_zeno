import time

import requests
import json
# import os
import sys


sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def potion_check(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, in_number_check, change_number, imgs_set_, text_check_potion
        from action_zeno import maul_potion, out_check, clean_screen

        print("potion_check")

        is_out = out_check(cla)
        if is_out == True:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:

                result_potion = False
                potion_count_ = text_check_potion(567, 990, 604, 1003, cla)
                print("4potion_count_", potion_count_)
                if potion_count_ > 0:
                    result_potion = True
                else:
                    potion_count_ = text_check_potion(573, 990, 604, 1003, cla)
                    print("4potion_count_", potion_count_)
                    if potion_count_ > 0:
                        result_potion = True
                    else:
                        potion_count_ = text_check_potion(577, 990, 604, 1003, cla)
                        print("3potion_count_", potion_count_)
                        if potion_count_ > 0:
                            result_potion = True
                        else:
                            v_.potion_count += 1
                            if v_.potion_count > 7:
                                v_.potion_count = 0
                                maul_potion(cla)
                if result_potion == True:
                    print("v_.potion_count", v_.potion_count)
                    if potion_count_ < 90:
                        v_.potion_count += 1
                        if v_.potion_count > 7:
                            v_.potion_count = 0
                            maul_potion(cla)
                    else:
                        v_.potion_count = 0
                    if cla == "one" or cla == "three":
                        v_.mypotion_1 = potion_count_
                    if cla == "two" or cla == "four":
                        v_.mypotion_2 = potion_count_
            else:
                print("없다.")
                maul_potion(cla)
        else:
            clean_screen(cla)





    except Exception as e:
        print(e)
        return 0

def potion_check_tuto(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, in_number_check, change_number, imgs_set_
        from action_zeno import maul_potion, out_check, clean_screen

        print("potion_check")

        is_out = out_check(cla)
        if is_out == True:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                potion_ready = text_check_get(580, 985, 605, 1003, cla)
                print("potion", potion_ready)
                v_.potion_count = 0
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("없다.", v_.potion_count)

                    v_.potion_count += 1
                    if v_.potion_count > 7:
                        v_.potion_count = 0
                        maul_potion(cla)
                else:
                    print("있다.")
        else:
            clean_screen(cla)





    except Exception as e:
        print(e)
        return 0

