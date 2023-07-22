import sys
import time

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def chago_setting(cla):
    import cv2
    import pyautogui
    import numpy as np
    from function import imgs_set_, click_pos_reg
    try:
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        if cla == 'four':
            plus = 960 + 960 + 960


        print("chago_setting")
        chago_drag(160, 690, 160, 170, cla)
        time.sleep(0.2)
        chango_bogwan_ = False
        chango_bogwan_count = 0
        while chango_bogwan_ is False:
            chango_bogwan_count += 1
            if chango_bogwan_count > 50:
                chango_bogwan_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\chango\\peari_soul.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 370, 320, 730, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                chango_bogwan_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\chango\\guisok_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            for i in pyautogui.locateAllOnScreen(img, region=(50 + plus, 370, 270, 360), confidence=0.8):
                # for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 945 + plus, 985),
                #                                      confidence=0.7):
                last_x1 = i.left
                last_y1 = i.top
                click_pos_reg(last_x1, last_y1, cla)
                time.sleep(0.2)

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\chango\\guisok_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            for i in pyautogui.locateAllOnScreen(img, region=(50 + plus, 370, 270, 360), confidence=0.8):
                # for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 945 + plus, 985),
                #                                      confidence=0.7):
                last_x2 = i.left
                last_y2 = i.top
                click_pos_reg(last_x2, last_y2, cla)
                time.sleep(0.2)

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\chango\\guisok_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            for i in pyautogui.locateAllOnScreen(img, region=(50 + plus, 370, 270, 360), confidence=0.8):
                # for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 945 + plus, 985),
                #                                      confidence=0.7):
                last_x2 = i.left
                last_y2 = i.top
                click_pos_reg(last_x2, last_y2, cla)
                time.sleep(0.2)

            # 드래그
            time.sleep(0.4)
            chago_drag(160, 690, 160, 170, cla)
            time.sleep(0.4)




    except Exception as e:
        print(e)
        return 0

def chago_drag(pos_1, pos_2, pos_3, pos_4, cla):
    import cv2
    import numpy as np
    from function import mouse_move_cpp, drag_pos_Press, drag_pos_Release
    try:
        print("chago_drag")
        mouse_move_cpp(pos_1, pos_2, cla)

        # 0.2초
        time.sleep(0.2)
        # 마우스 누르기
        drag_pos_Press()
        # 0.2초
        time.sleep(0.4)
        # 마우스 이동
        mouse_move_cpp(pos_3, pos_4, cla)
        # 0.2초
        time.sleep(0.4)
        # 마우스 떼기
        drag_pos_Release()
        # 0.2초
        time.sleep(0.2)
    except Exception as e:
        print(e)
        return 0



