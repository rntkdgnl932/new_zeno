
import sys
import time

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def all_realtime(cla):
    try:
        print("all_realtime")
        collection(cla)
        boonhae(cla)
        chango_in(cla)

    except Exception as e:
        print(e)
        return 0


def collection(cla):
    import numpy as np
    import cv2
    from action_zeno import menu_open
    from function import click_pos_reg, click_pos_2, imgs_set_
    try:
        print("collection")

        col_ = False
        col_count = 0
        while col_ is False:
            col_count += 1
            if col_count > 7:
                col_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\collection_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("collection_title", imgs_)

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\collection_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(5, 170, 40, 270, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("collection_click", imgs_)
                    click_pos_reg(imgs_.x + 15, imgs_.y + 20, cla)
                    time.sleep(0.3)

                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\collection_click2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 170, 570, 970, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("collection_click", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 20, cla)
                            time.sleep(0.3)
                            click_pos_2(900, 1000, cla)
                            time.sleep(0.3)
                            for c in range(10):
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 620, 620, 670, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                time.sleep(0.2)
                        else:
                            break
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 640, 470, 700, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                else:
                    col_ = True

            else:
                menu_open(cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\collection_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 110, 850, 150, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("collection_checked", imgs_)
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                else:
                    col_ = True
            time.sleep(1)

        for i in range(5):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\cancle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 640, 470, 700, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\collection\\collection_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 50, cla)
                break
            time.sleep(0.1)

    except Exception as e:
        print(e)
        return 0


def boonhae(cla):
    import numpy as np
    import cv2
    from action_zeno import clean_screen, bag_open
    from function import click_pos_reg, click_pos_2, imgs_set_
    try:
        print("boonhae")
        clean_screen(cla)


        # 장비 분해
        j_boon_ = False
        j_boon_count = 0
        while j_boon_ is False:
            j_boon_count += 1
            if j_boon_count > 5:
                j_boon_ = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\boonhae_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 740, 850, 780, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:

                j_boon_ = True

                # 1 장비
                # 2 스킬북
                # 3 석판

                for i in range(1):

                    x_plus = i * 90
                    click_pos_2(690 + x_plus, 350, cla)
                    time.sleep(0.5)

                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\no_have_item.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(710, 530, 890, 590, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        pass
                    else:

                        click_pos_2(680, 395, cla)
                        time.sleep(0.5)
                        click_pos_2(770, 395, cla)
                        time.sleep(0.5)

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\boonhae_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 740, 850, 780, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)


                    time.sleep(0.5)

            else:
                bag_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\boonhae_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(740, 740, 850, 780, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\bag_boonhae_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(840, 720, 910, 790, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(0.3)

            time.sleep(0.5)

        # 스킬북 분해전 한번 더 확인
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\boonhae_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 740, 920, 780, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # # 스킬북 분해
        # s_boon_ = False
        # s_boon_count = 0
        # while s_boon_ is False:
        #     s_boon_count += 1
        #     if s_boon_count > 5:
        #         s_boon_ = True
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\skillbook_boonhae.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(780, 320, 900, 370, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         time.sleep(1)
        #
        #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\no_have_item.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(710, 530, 890, 590, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             s_boon_ = True
        #         else:
        #             click_pos_2(680, 400, cla)
        #             time.sleep(0.5)
        #             click_pos_2(770, 400, cla)
        #             time.sleep(0.5)
        #
        #             for i in range(10):
        #                 full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\boonhae_confirm.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(740, 740, 850, 780, cla, img, 0.85)
        #                 if imgs_ is not None and imgs_ != False:
        #                     click_pos_reg(imgs_.x, imgs_.y, cla)
        #                     break
        #                 time.sleep(0.1)
        #             s_boon_ = True

        for i in range(4):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\x.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 310, 960, 390, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0


def chango_in(cla):
    import numpy as np
    import cv2
    from action_zeno import clean_screen, in_maul_check, go_maul, zeno_moving
    from function import click_pos_reg, imgs_set_
    try:
        print("chango_in")
        in_ = in_maul_check(cla)
        if in_ == False:
            clean_screen(cla)
            in_ = in_maul_check(cla)
            if in_ == False:
                go_maul(cla)

        chango_go_ = False
        chango_go_count = 0
        while chango_go_ is False:
            chango_go_count += 1
            if chango_go_count > 7:
                chango_go_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\chango_in\\bogwan.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(820, 740, 940, 790, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                for i in range(2):
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 740, 620, 785, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
                chango_go_ = True
            else:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\chango_in\\chango.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 940, 870, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    zeno_moving(cla)
            time.sleep(1)

        for i in range(4):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\x.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 310, 960, 390, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.3)

    except Exception as e:
        print(e)
        return 0

