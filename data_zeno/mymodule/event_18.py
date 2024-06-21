import time

# import os
import sys


sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def event_stop(cla):
    import numpy as np
    import cv2
    import os
    from function import click_pos_reg, click_pos_2, imgs_set_
    from action_zeno import menu_open
    try:
        print("event_stop")

        loop = True
        loop_count = 0
        while loop is True:
            loop_count += 1
            if loop_count > 3:
                loop = False

            loop_check = False
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\event_18\\not_again_view.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 600, 300, 750, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("not_again_view", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                loop_check = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\event_18\\today_one.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(220, 650, 480, 750, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("today_one", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    loop_check = True
                else:
                    # 서버 끊김
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\event_18\\server_not_connected.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(220, 700, 300, 900, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("server_not_connected", imgs_)

                        dir_path = "C:\\my_games\\load\\zenonia"
                        file_path = dir_path + "\\start.txt"
                        file_path2 = dir_path + "\\cla.txt"
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            data = 'no'
                            file.write(str(data))
                            time.sleep(0.2)
                        with open(file_path2, "w", encoding='utf-8-sig') as file:
                            data = v_.now_cla
                            file.write(str(data))
                            time.sleep(0.2)
                        os.execl(sys.executable, sys.executable, *sys.argv)

            if loop_check == False:
                loop = False

            time.sleep(0.5)

    except Exception as e:
        print(e)




