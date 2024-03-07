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
        from action_zeno import out_check, clean_screen

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
        from action_zeno import out_check, clean_screen

        print("potion_check")

        is_out = out_check(cla)
        if is_out == True:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                potion_ready = text_check_get(580, 985, 605, 1003, cla)
                print("potion", potion_ready)
                v_.potion_count = 0
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\not_have_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("없다.", v_.potion_count)

                    v_.potion_count += 1
                    if v_.potion_count > 7:
                        v_.potion_count = 0
                        maul_potion(cla)
                else:
                    print("비어있다.")
        else:
            clean_screen(cla)
    except Exception as e:
        print(e)
        return 0

def juljun_potion_check(cla):
    import cv2
    import numpy as np
    from function import imgs_set_
    try:
        print("juljun_potion_check")
        is_potion = False
        for i in range(4):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\juljun_potion_" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            if i == 0:
                imgs_ = imgs_set_(360, 950, 430, 990, cla, img, 0.95)
            else:
                imgs_ = imgs_set_(360, 950, 430, 990, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                is_potion = True
                # print(i)
        # print("is_potion", is_potion)
        if is_potion == False:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\juljun_potion_zero.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 950, 430, 990, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("false 물약 없다 즉시 집에 가자")
            else:
                is_potion = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\juljun_potion_0.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 950, 430, 990, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("false 물약 있는거라고 표시된다")
                is_potion = True
        return is_potion
    except Exception as e:
        print("error", e)
        return 0


def juljun_maul_potion(cla):
    import cv2
    import numpy as np
    from function import imgs_set_, drag_pos, click_pos_2
    from action_zeno import out_check, clean_screen
    try:
        print("juljun_maul_potion")
        in_ = False
        in_count = 0
        while in_ is False:
            in_count += 1
            if in_count > 20:
                in_ = True
            result_out = out_check(cla)
            if result_out == True:
                in_ = True
                maul_potion(cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_maul_potion : juljun_1")
                    # drag_pos(360, 460, 600, 460, cla)
                    click_pos_2(560, 980, cla)
                    time.sleep(0.2)
                    click_pos_2(560, 980, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        drag_pos(360, 460, 600, 460, cla)
                else:
                    print("juljun_maul_potion : clean_screen")
                    clean_screen(cla)
                    click_pos_2(375, 975, cla)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0

def maul_potion(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_reg, click_pos_2, drag_pos
        from action_zeno import in_maul_check, clean_screen, go_maul
        from realtime import all_realtime
        from guild_zenonia import guild_check

        print("maul_potion")

        # 바깥 화면으로 먼저 빠져나오기



        in_ = in_maul_check(cla)
        if in_ == False:
            clean_screen(cla)
            in_ = in_maul_check(cla)
            if in_ == False:
                go_maul(cla)

        # 마을 도착하면 가방 등 정리하기

        guild_check(cla)
        time.sleep(0.5)

        all_realtime(cla)

        in_jabhwa = False

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            in_jabhwa = True


        in_jabhwa_count = 0
        while in_jabhwa is False:
            in_jabhwa_count += 1
            if in_jabhwa_count > 10:
                in_jabhwa = True

            # 잡화 진입

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                in_jabhwa2 = False
                in_jabhwa2_count = 0
                while in_jabhwa2 is False:
                    in_jabhwa2_count += 1
                    if in_jabhwa2_count > 20:
                        in_jabhwa2 = True

                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        in_jabhwa = True
                        in_jabhwa2 = True
                    time.sleep(0.5)

            time.sleep(0.5)

        if in_jabhwa == True:
            in_jabhwa2 = False
            in_jabhwa2_count = 0
            while in_jabhwa2 is False:
                in_jabhwa2_count += 1
                if in_jabhwa2_count > 20:
                    in_jabhwa2 = True

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    in_jabhwa2 = True

                    if in_jabhwa2_count < 3:
                        click_pos_2(775, 350, cla)
                        time.sleep(0.5)
                    print("잡화 상점 도착")

                    # # 귀환주문서 부터
                    # print("마을귀환서 구매")
                    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\maul_guihwan_bag.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    # if imgs_ is not None and imgs_ != False:
                    #     print("c")
                    # else:
                    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\maul_guihwan_sangjum.PNG"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                    #     if imgs_ is not None and imgs_ != False:
                    #         click_pos_reg(imgs_.x, imgs_.y, cla)
                    #         time.sleep(0.5)
                    #
                    #         in_jabhwa3 = False
                    #         in_jabhwa3_count = 0
                    #         while in_jabhwa3 is False:
                    #             in_jabhwa3_count += 1
                    #             if in_jabhwa3_count > 10:
                    #                 in_jabhwa3 = True
                    #
                    #             full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                    #             img_array = np.fromfile(full_path, np.uint8)
                    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #             imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                    #             if imgs_ is not None and imgs_ != False:
                    #                 click_pos_2(420, 450, cla)
                    #                 time.sleep(0.3)
                    #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                 time.sleep(0.3)
                    #
                    #                 full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    #                 img_array = np.fromfile(full_path, np.uint8)
                    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #                 imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    #                 if imgs_ is not None and imgs_ != False:
                    #                     in_jabhwa3 = True
                    #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                     time.sleep(0.3)
                    # # 랜덤이동서
                    # print("랜덤이동서 구매")
                    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\random_move_bag.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    # if imgs_ is not None and imgs_ != False:
                    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\random_move_sangjum.PNG"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                    #     if imgs_ is not None and imgs_ != False:
                    #         click_pos_reg(imgs_.x, imgs_.y, cla)
                    #         time.sleep(0.5)
                    #
                    #         in_jabhwa3 = False
                    #         in_jabhwa3_count = 0
                    #         while in_jabhwa3 is False:
                    #             in_jabhwa3_count += 1
                    #             if in_jabhwa3_count > 10:
                    #                 in_jabhwa3 = True
                    #
                    #             full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                    #             img_array = np.fromfile(full_path, np.uint8)
                    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #             imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                    #             if imgs_ is not None and imgs_ != False:
                    #                 click_pos_2(470, 450, cla)
                    #                 time.sleep(0.3)
                    #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                 time.sleep(0.3)
                    #
                    #                 full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    #                 img_array = np.fromfile(full_path, np.uint8)
                    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #                 imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    #                 if imgs_ is not None and imgs_ != False:
                    #                     in_jabhwa3 = True
                    #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                     time.sleep(0.3)
                    # else:
                    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\random_move_sangjum.PNG"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                    #     if imgs_ is not None and imgs_ != False:
                    #         click_pos_reg(imgs_.x, imgs_.y, cla)
                    #         time.sleep(0.5)
                    #
                    #         in_jabhwa3 = False
                    #         in_jabhwa3_count = 0
                    #         while in_jabhwa3 is False:
                    #             in_jabhwa3_count += 1
                    #             if in_jabhwa3_count > 10:
                    #                 in_jabhwa3 = True
                    #
                    #             full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                    #             img_array = np.fromfile(full_path, np.uint8)
                    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #             imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                    #             if imgs_ is not None and imgs_ != False:
                    #                 for i in range(1):
                    #                     click_pos_2(530, 460, cla)
                    #                     time.sleep(0.3)
                    #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                 time.sleep(0.3)
                    #
                    #                 full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    #                 img_array = np.fromfile(full_path, np.uint8)
                    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #                 imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    #                 if imgs_ is not None and imgs_ != False:
                    #                     in_jabhwa3 = True
                    #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                     time.sleep(0.3)
                    # # 천마석
                    # print("천마석")
                    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\chunma_bag.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    # if imgs_ is not None and imgs_ != False:
                    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\chunma_sangjum.PNG"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                    #     if imgs_ is not None and imgs_ != False:
                    #         click_pos_reg(imgs_.x, imgs_.y, cla)
                    #         time.sleep(0.5)
                    #
                    #         in_jabhwa3 = False
                    #         in_jabhwa3_count = 0
                    #         while in_jabhwa3 is False:
                    #             in_jabhwa3_count += 1
                    #             if in_jabhwa3_count > 10:
                    #                 in_jabhwa3 = True
                    #
                    #             full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                    #             img_array = np.fromfile(full_path, np.uint8)
                    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #             imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                    #             if imgs_ is not None and imgs_ != False:
                    #                 for i in range(5):
                    #                     click_pos_2(420, 500, cla)
                    #                     time.sleep(0.1)
                    #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                 time.sleep(0.3)
                    #
                    #                 full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    #                 img_array = np.fromfile(full_path, np.uint8)
                    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #                 imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    #                 if imgs_ is not None and imgs_ != False:
                    #                     in_jabhwa3 = True
                    #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                     time.sleep(0.3)
                    # else:
                    #
                    #     drag_pos(140, 670, 140, 170, cla)
                    #
                    #     time.sleep(0.5)
                    #
                    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\chunma_sangjum.PNG"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                    #     if imgs_ is not None and imgs_ != False:
                    #         click_pos_reg(imgs_.x, imgs_.y, cla)
                    #         time.sleep(0.5)
                    #
                    #         in_jabhwa3 = False
                    #         in_jabhwa3_count = 0
                    #         while in_jabhwa3 is False:
                    #             in_jabhwa3_count += 1
                    #             if in_jabhwa3_count > 10:
                    #                 in_jabhwa3 = True
                    #
                    #             full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                    #             img_array = np.fromfile(full_path, np.uint8)
                    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #             imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                    #             if imgs_ is not None and imgs_ != False:
                    #                 click_pos_2(530, 530, cla)
                    #                 time.sleep(0.3)
                    #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                 time.sleep(0.3)
                    #
                    #                 full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    #                 img_array = np.fromfile(full_path, np.uint8)
                    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #                 imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    #                 if imgs_ is not None and imgs_ != False:
                    #                     in_jabhwa3 = True
                    #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #                     time.sleep(0.3)

                    # 위는 자동구매로 대체하기
                    click_pos_2(80, 760, cla)

                    # 물약
                    print("물약 사기")

                    potion_ready = False
                    potion_ready_count = 0
                    while potion_ready is False:
                        potion_ready_count += 1
                        if potion_ready_count > 10:
                            potion_ready = True

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\potion_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            in_jabhwa3 = False
                            in_jabhwa3_count = 0
                            while in_jabhwa3 is False:
                                in_jabhwa3_count += 1
                                if in_jabhwa3_count > 10:
                                    in_jabhwa3 = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    potion_ready = True
                                    click_pos_2(590, 530, cla)
                                    time.sleep(0.3)

                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        in_jabhwa3 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.3)

                                time.sleep(0.3)
                        else:
                            click_pos_2(90, 350, cla)
                            time.sleep(0.5)
                    time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                time.sleep(1)
        # 마지막 닫기
        for i in range(4):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
            else:
                break
            time.sleep(0.1)




    except Exception as e:
        print(e)
        return


def maul_dead_potion(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_reg, click_pos_2, drag_pos
        from action_zeno import in_maul_check, clean_screen, go_maul
        from realtime import all_realtime

        print("maul_dead_potion")

        # 바깥 화면으로 먼저 빠져나오기



        in_ = in_maul_check(cla)
        if in_ == False:
            clean_screen(cla)
            in_ = in_maul_check(cla)
            if in_ == False:
                go_maul(cla)

        # 마을 도착하면 가방 등 정리하기
        all_realtime(cla)

        in_jabhwa = False

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            in_jabhwa = True


        in_jabhwa_count = 0
        while in_jabhwa is False:
            in_jabhwa_count += 1
            if in_jabhwa_count > 10:
                in_jabhwa = True

            # 잡화 진입

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                in_jabhwa2 = False
                in_jabhwa2_count = 0
                while in_jabhwa2 is False:
                    in_jabhwa2_count += 1
                    if in_jabhwa2_count > 20:
                        in_jabhwa2 = True

                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        in_jabhwa = True
                        in_jabhwa2 = True
                    time.sleep(0.5)

            time.sleep(0.5)

        if in_jabhwa == True:
            in_jabhwa2 = False
            in_jabhwa2_count = 0
            while in_jabhwa2 is False:
                in_jabhwa2_count += 1
                if in_jabhwa2_count > 20:
                    in_jabhwa2 = True

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    in_jabhwa2 = True

                    if in_jabhwa2_count < 3:
                        click_pos_2(775, 350, cla)
                        time.sleep(0.5)
                    print("잡화 상점 도착")

                    # 귀환주문서 부터
                    print("마을귀환서 구매")
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\maul_guihwan_bag.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("c")
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\maul_guihwan_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            in_jabhwa3 = False
                            in_jabhwa3_count = 0
                            while in_jabhwa3 is False:
                                in_jabhwa3_count += 1
                                if in_jabhwa3_count > 10:
                                    in_jabhwa3 = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(420, 450, cla)
                                    time.sleep(0.3)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        in_jabhwa3 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.3)
                    # 랜덤이동서
                    print("랜덤이동서 구매")
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\random_move_bag.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\random_move_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            in_jabhwa3 = False
                            in_jabhwa3_count = 0
                            while in_jabhwa3 is False:
                                in_jabhwa3_count += 1
                                if in_jabhwa3_count > 10:
                                    in_jabhwa3 = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(420, 450, cla)
                                    time.sleep(0.3)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        in_jabhwa3 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.3)
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\random_move_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            in_jabhwa3 = False
                            in_jabhwa3_count = 0
                            while in_jabhwa3 is False:
                                in_jabhwa3_count += 1
                                if in_jabhwa3_count > 10:
                                    in_jabhwa3 = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    for i in range(1):
                                        click_pos_2(530, 460, cla)
                                        time.sleep(0.3)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        in_jabhwa3 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.3)
                    # 천마석
                    print("천마석")
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\chunma_bag.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\chunma_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            in_jabhwa3 = False
                            in_jabhwa3_count = 0
                            while in_jabhwa3 is False:
                                in_jabhwa3_count += 1
                                if in_jabhwa3_count > 10:
                                    in_jabhwa3 = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(530, 605, cla)
                                    time.sleep(0.3)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        in_jabhwa3 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.3)
                    else:

                        drag_pos(140, 670, 140, 170, cla)

                        time.sleep(0.5)

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\chunma_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            in_jabhwa3 = False
                            in_jabhwa3_count = 0
                            while in_jabhwa3 is False:
                                in_jabhwa3_count += 1
                                if in_jabhwa3_count > 10:
                                    in_jabhwa3 = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(530, 650, cla)
                                    time.sleep(0.3)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        in_jabhwa3 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.3)
                    # 물약
                    print("물약 사기")

                    potion_ready = False
                    potion_ready_count = 0
                    while potion_ready is False:
                        potion_ready_count += 1
                        if potion_ready_count > 10:
                            potion_ready = True

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\potion_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 350, 100, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            in_jabhwa3 = False
                            in_jabhwa3_count = 0
                            while in_jabhwa3 is False:
                                in_jabhwa3_count += 1
                                if in_jabhwa3_count > 10:
                                    in_jabhwa3 = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    potion_ready = True
                                    click_pos_2(590, 530, cla)
                                    time.sleep(0.3)

                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        in_jabhwa3 = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.3)

                                time.sleep(0.3)
                        else:
                            click_pos_2(90, 350, cla)
                            time.sleep(0.5)
                    time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                time.sleep(1)
        # 마지막 닫기
        for i in range(4):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
            else:
                break
            time.sleep(0.1)




    except Exception as e:
        print(e)
        return







