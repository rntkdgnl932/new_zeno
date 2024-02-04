import random
import time
import sys
import cv2
import numpy as np

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def jadong_start(cla, where):
    from action_zeno import dead_die
    from potion_zeno import juljun_potion_check, juljun_maul_potion
    from function import imgs_set_
    try:
        print("jadong_start")
        dead_die(cla)
        # jadong_juljun_attack_gold_check(cla, where)
        # 절전 자동 모드 아니라면 진입하기
        result_arrived = jadong_arrive_check(cla, where)
        if result_arrived == True:
            result_potion = juljun_potion_check(cla)
            if result_potion == False:
                juljun_maul_potion(cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun_item_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 220, 170, 270, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:
                    juljun_maul_potion(cla)

        else:
            for i in range(10):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\dead_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    jadong_juljun_attack_dead(cla, where)
                    time.sleep(0.5)
                    break
                time.sleep(0.1)

            dead_die(cla)
            map_in(cla, where)
        time.sleep(3)
    except Exception as e:
        print(e)
        return 0

def map_in(cla, where):
    try:
        from action_zeno import clean_screen, confirm_all, now_hunting
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("map_in")

        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                drag_pos(360, 460, 900, 460, cla)

            else:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\map.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 20, 100, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    time.sleep(0.2)

                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\is_dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 550, 250, 620, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("is_dungeon", imgs_)

                        quihwan_ = False
                        quihwan_count = 0
                        while quihwan_ is False:
                            quihwan_count += 1
                            if quihwan_count > 10:
                                quihwan_ = True
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\maul_quihwan.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 940, 410, 1010, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                quihwan_ = True
                                time.sleep(2)
                                spot_arrive(cla, where)
                            else:
                                click_pos_2(930, 50, cla)
                            time.sleep(1)


                    else:
                        print("던전 아니다.")

                        in_map_ = True

                        # 여기에 갈 장소 넣기
                        # 오른쪽에 리스트 열기
                        map_list_open(cla, where)
                        # 열린 리스트 클릭하기기
                        map_list_click(cla, where)
                        # 전리품 클릭
                        map_junlipoom_open(cla, where)
                        # 전리품 주는 몬스터 클릭 => 업뎃 후 몬스터 랜덤클릭
                        map_junlipoom_click(cla, where)
                        # 지도에 표시된 포탈 클릭
                        map_spot_click(cla, where)
                        # 확인 클릭
                        confirm_all(cla)
                        # 도착 확인
                        spot_arrive(cla, where)
                        # 사냥 중인지 확인

                        # 1

                        # 2
                        juljun_arrive(cla, where)
                        # 절전 모드 확인 후 전투중인지 확인하고 다시 공격 버튼 누르기



                else:
                    clean_screen(cla)
                    time.sleep(0.2)
                    click_pos_2(110, 130, cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def map_list_open(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_
        print("map_list_open")
        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\maul.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 120, 870, 1020, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_map_ = True
            else:
                click_pos_2(840, 100, cla)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def map_list_click(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("map_list_click")

        click_reg = map_pic_name(cla, where)

        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True
            # red_hwangya_1

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\map_list\\" + click_reg + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 70, 960, 120, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\maul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 120, 870, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\map_list\\" + click_reg + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(740, 120, 960, 1020, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                else:
                    in_map_ = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\map_list\\" + click_reg + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 120, 960, 1020, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:

                    if click_reg == 'alak_3':
                        drag_pos(860, 100, 860, 500, cla)
                        time.sleep(0.3)
                        click_pos_2(860, 500, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\maul.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 120, 870, 1020, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(860, 500, cla)
                            time.sleep(0.5)

                    else:
                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\maul.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 120, 870, 1020, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(x_reg, y_reg, cla)
                            time.sleep(0.5)

                    time.sleep(1)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\maul.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(740, 120, 870, 1020, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        drag_pos(850, 200, 850, 700, cla)
                    else:
                        click_pos_2(840, 100, cla)
                        time.sleep(0.5)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def map_junlipoom_open(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_
        print("map_junlipoom_open")
        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\junlipoom.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 120, 80, 170, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_map_ = True
            else:
                click_pos_2(50, 100, cla)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

# def map_junlipoom_click(cla, where):
#     try:
#         from action_zeno import clean_screen
#         from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
#         print("map_junlipoom_click")
#
#
#         click_reg = map_pic_name(cla, where)
#
#         in_map_ = False
#         in_map_count = 0
#         while in_map_ is False:
#             in_map_count += 1
#             if in_map_count > 10:
#                 in_map_ = True
#
#             full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\map_spot.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(310, 170, 950, 840, cla, img, 0.85)
#             if imgs_ is not None and imgs_ != False:
#                 in_map_ = True
#             else:
#
#                 full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\spot_click_1.PNG"
#                 img_array = np.fromfile(full_path, np.uint8)
#                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                 imgs_ = imgs_set_(430, 340, 520, 390, cla, img, 0.85)
#                 if imgs_ is not None and imgs_ != False:
#                     if click_reg == 'goolm_1':
#                         click_pos_2(455, 555, cla)
#                     else:
#                         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\spot_click_2.PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         imgs_ = imgs_set_(560, 380, 655, 725, cla, img, 0.85)
#                         if imgs_ is not None and imgs_ != False:
#                             click_pos_reg(imgs_.x, imgs_.y, cla)
#
#                 else:
#
#                     if click_reg == 'red_hwangya_1':
#                         click_pos_2(110, 570, cla)
#                     elif click_reg == 'goolm_1':
#                         for i in range(10):
#                             full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\junlipoom\\" + click_reg + ".PNG"
#                             img_array = np.fromfile(full_path, np.uint8)
#                             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                             imgs_ = imgs_set_(0, 160, 300, 1020, cla, img, 0.85)
#                             if imgs_ is not None and imgs_ != False:
#                                 click_pos_reg(imgs_.x, imgs_.y, cla)
#                                 break
#                             else:
#                                 drag_pos(140, 540, 140, 140, cla)
#                             time.sleep(0.5)
#                     else:
#
#                         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\junlipoom\\" + click_reg + ".PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         imgs_ = imgs_set_(0, 160, 300, 1020, cla, img, 0.85)
#                         if imgs_ is not None and imgs_ != False:
#                             click_pos_reg(imgs_.x, imgs_.y, cla)
#             time.sleep(0.5)
#     except Exception as e:
#         print(e)
#         return 0

def map_junlipoom_click(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("map_junlipoom_click")


        click_reg = map_pic_name(cla, where)

        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\map_spot.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(310, 170, 950, 840, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_map_ = True
            else:
                click_pos_2(150, 105, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\monster_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 120, 80, 180, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)

                y_ran = random.randint(1, 12)
                y_plus = 200 + (65 * y_ran)

                click_pos_2(120, y_plus, cla)

            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def map_spot_click(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_
        print("map_spot_click")
        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 610, 650, 650, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_map_ = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\map_spot.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(310, 170, 950, 840, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\teleport2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(310, 170, 950, 840, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("teleport2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(0.2)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def spot_arrive(cla, where):
    try:
        from action_zeno import clean_screen, out_check, confirm_all
        from function import click_pos_2, click_pos_reg, imgs_set_
        # 여기 where는 2023. 7. 22. 현재는 큰 의미 없음.
        print("spot_arrive", where)
        time.sleep(5)
        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 30:
                in_map_ = True
            result = out_check(cla)
            if result == True:
                in_map_ = True
            else:
                print("사냥터 가는중")
                confirm_all(cla)
            time.sleep(2)
    except Exception as e:
        print(e)
        return 0

def juljun_arrive(cla, where):
    try:
        from action_zeno import clean_screen, out_check, now_hunting
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("juljun_arrive")
        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("in_map_count", in_map_count)

                result_attack = jadong_juljun_attack_check(cla, where)

                print("result_attack", result_attack)
                if result_attack == "attack":
                    in_map_ = True
                else:
                    for i in range(3):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            drag_pos(360, 460, 900, 460, cla)

                        else:
                            break
                    if result_attack == "rest":
                        print("공격모드로 바꾸기")
                        click_pos_2(905, 790, cla)
                        time.sleep(0.3)
                        click_pos_2(30, 930, cla)
                    elif result_attack == "dead":
                        print("죽었으니 살리기")
                        jadong_juljun_attack_dead(cla, where)
            else:
                result = out_check(cla)
                if result == True:
                    # 던전일 경우 날아가자
                    if '_' in where:
                        jadong_spl_ = where.split("_")
                        if jadong_spl_[0] != "사냥":
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\random_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 940, 460, 1010, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(2)
                                # 사냥터로 가는 중
                                spot_arrive(cla, where)
                    result_hunting1 = now_hunting(cla)
                    if result_hunting1 == True:
                        result_hunting2 = now_hunting(cla)
                        if result_hunting2 == True:
                            print("사냥중")
                            click_pos_2(30, 930, cla)
                        else:
                            click_pos_2(905, 790, cla)
                            time.sleep(0.3)
                            click_pos_2(30, 930, cla)
                    else:
                        click_pos_2(905, 790, cla)
                        time.sleep(0.3)
                        click_pos_2(30, 930, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)

                else:
                    clean_screen(cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0


def map_pic_name(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_
        print("map_pic_name")

        click_reg = 'none'

        if '_' in where:
            jadong_spl_ = where.split("_")

        if jadong_spl_[2] == "쉐이드숲":
            click_reg = 'shade_forest'
        elif jadong_spl_[2] == "로렐라이강":
            if jadong_spl_[3] == "15벨트":
                click_reg = 'lolel_river_1'
            elif jadong_spl_[3] == "14장갑":
                click_reg = 'lolel_river_2'
            elif jadong_spl_[3] == "17갑옷나무600":
                click_reg = 'lolel_river_3'
        elif jadong_spl_[2] == "구름고원":
            if jadong_spl_[3] == "27인간정수":
                click_reg = 'goolm_1'
        elif jadong_spl_[2] == "아라크1층":
            click_reg = 'alak_1'
        elif jadong_spl_[2] == "아라크3층":
            click_reg = 'alak_3'

        elif jadong_spl_[2] == "엘라움계곡":
            if jadong_spl_[3] == "30목걸이장갑천":
                click_reg = 'elaum_1'
            elif jadong_spl_[3] == "31벨트":
                click_reg = 'elaum_2'
            elif jadong_spl_[3] == "33반귀투천":
                click_reg = 'elaum_3'
        elif jadong_spl_[2] == "붉은황야":
            if jadong_spl_[3] == "35활목천아인종":
                click_reg = 'red_hwangya_1'
        elif jadong_spl_[2] == "카나크협곡":
            click_reg = 'canak_1'
        elif jadong_spl_[2] == "로쿠광산":
            click_reg = 'locoo_1'
        elif jadong_spl_[2] == "베네둠1층":
            click_reg = 'benedoom_1'
        elif jadong_spl_[2] == "고대유적지":
            click_reg = 'godae_1'

        return click_reg
    except Exception as e:
        print(e)
        return 0

def jadong_arrive_check(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion_zeno import juljun_potion_check, juljun_maul_potion
        print("jadong_arrive_check")

        potion_check = False
        arrive = False

        result_arrive = jadong_juljun_attack_check(cla, where)
        if result_arrive == "attack":

            gold_1 = jadong_juljun_attack_gold_check(cla, where)
            # time.sleep(15)
            # 여기 15초동안 포션체크 하자
            for i in range(15):
                result_potion = juljun_potion_check(cla)
                if result_potion == False:
                    potion_check = True
                    juljun_maul_potion(cla)
                    break
                time.sleep(1)

            if potion_check == False:
                gold_2 = jadong_juljun_attack_gold_check(cla, where)

                if gold_1 != gold_2:
                    arrive = True
                else:
                    for i in range(3):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            drag_pos(360, 460, 900, 460, cla)
                            break
                        time.sleep(1)

        else:
            for i in range(3):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(360, 460, 900, 460, cla)
                else:
                    break
            if result_arrive == "rest":
                print("공격모드로 바꾸기")
                click_pos_2(905, 790, cla)
                time.sleep(0.3)
                click_pos_2(30, 930, cla)
            elif result_arrive == "dead":
                print("죽었으니 살리기")
                jadong_juljun_attack_dead(cla, where)
        time.sleep(0.5)


        return arrive
    except Exception as e:
        print(e)
        return 0

def jadong_juljun_attack_check(cla, where):
    try:
        from action_zeno import clean_screen, out_check
        from function import click_pos_2, click_pos_reg, imgs_set_, text_check_get
        from dungeon_zeno import dungeon_ready
        print("jadong_juljun_attack_check")

        go_ = "none"
        dun_ = False
        if '_' in where:
            jadong_spl_ = where.split("_")

        # 왼쪽 위 장소 맞는지 파악하고 맞다면 아래 파악 ... 던전은 추후 추가하기...

        # 먼저 절전모드인지 체크하고 절전모드 상태로 돌려놓고 확인하자

        check_ready = False
        check_ready_count = 0
        while check_ready is False:
            check_ready_count += 1
            if check_ready_count > 7:
                check_ready = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:

                check_ready = True

                if jadong_spl_[0] == "사냥":
                    result_pic = map_pic_name(cla, where)
                    # red_hwangya_1
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\juljun_title\\" + result_pic + ".PNG"
                    # elif jadong_spl_[0] == "일반" or jadong_spl_[0] == "특수" or jadong_spl_[0] == "파티":
                    #
                    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\dungeon_title\\" #
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 90, 250, 150, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            # gold_1 = jadong_juljun_attack_gold_check(cla, where)
                            in_map_ = False
                            in_map_count = 0
                            while in_map_ is False:
                                in_map_count += 1
                                if in_map_count > 50:
                                    in_map_ = True

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\attack_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    go_ = "attack"
                                    in_map_ = True
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\rest_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    go_ = "rest"
                                    in_map_ = True
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\dead_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    go_ = "dead"
                                    in_map_ = True
                                time.sleep(0.1)
                        else:
                            print("절전공격모드 아님")
                else:
                    if jadong_spl_[0] == "일반" or jadong_spl_[0] == "특수":
                        # jadong_spl_[1] == "업보, 지옥, 죄악, 저주, 마족, 아르카스"
                        # title_ = text_check_get(45, 90, 140, 160, cla)
                        # print("title_", title_)
                        # title_ = text_check_get(45, 90, 140, 130, cla)
                        # print("title_", title_)
                        # print("jadong_spl_[1]", jadong_spl_[1])
                        #
                        # equal = 0
                        # for i in range(len(title_)):
                        #     for z in range(len(jadong_spl_[1])):
                        #         if title_[i] == jadong_spl_[1][z]:
                        #             equal += 1
                        #             print("equal", title_[i], jadong_spl_[1][z])
                        #             if equal > 1:
                        #                 dun_ = True
                        #                 break

                        if jadong_spl_[1] == "업보":
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\upbo_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 90, 250, 150, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                dun_ = True
                                print("upbo_title", imgs_)
                            else:
                                print("not upbo_title")
                        elif jadong_spl_[1] == "지옥":
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\juljun_hell_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 90, 250, 150, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                dun_ = True
                                print("devil_title", imgs_)
                            else:
                                print("not devil_title")

                        # elif jadong_spl_[1] == "죄악":
                        #
                        # elif jadong_spl_[1] == "저주":
                        #
                        elif jadong_spl_[1] == "마족":
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\devil_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 90, 250, 150, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                dun_ = True
                                print("devil_title", imgs_)
                            else:
                                print("not devil_title")

                        elif jadong_spl_[1] == "아르카스":
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\arcas_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 90, 250, 150, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                dun_ = True
                                print("arcas_title", imgs_)
                            else:
                                print("not arcas_title")

                        elif jadong_spl_[1] == "격전":
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\gyugjun_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 90, 250, 150, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                dun_ = True
                                print("gyugjun_title", imgs_)
                            else:
                                print("not gyugjun_title")

                        time.sleep(1)

                        if dun_ == True:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                # gold_1 = jadong_juljun_attack_gold_check(cla, where)
                                in_map_ = False
                                in_map_count = 0
                                while in_map_ is False:
                                    in_map_count += 1
                                    if in_map_count > 50:
                                        in_map_ = True

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\attack_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        go_ = "attack"
                                        in_map_ = True
                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\rest_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        go_ = "rest"
                                        in_map_ = True
                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\dead_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        go_ = "dead"
                                        in_map_ = True
                                    time.sleep(0.1)
                            else:
                                print("절전공격모드 아님")
                        else:
                            print("던전 아님")


                    elif jadong_spl_[0] == "파티":
                        print("이건 준비중...")

                    else:
                        print("원하는 장소가 아니다.")
            else:
                print("절전모드가 아니니 확인하기 위해 절전모드로 진입하자")
                for i in range(10):
                    result_out = out_check(cla)
                    if result_out == True:
                        click_pos_2(30, 930, cla)
                        break
                    else:
                        clean_screen(cla)
                    time.sleep(1)
            time.sleep(1)
        print("go_ ???? ", go_)
        return go_
    except Exception as e:
        print(e)
        return 0

def jadong_juljun_attack_gold_check(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_,text_check_get, in_number_check, int_put_
        print("jadong_juljun_attack_gold_check")
        many_gold = 0
        gold_ = text_check_get(40, 165, 120, 190, cla)
        print("gold", gold_)
        is_number = in_number_check(cla, gold_)
        if is_number == True:
            result_num = int_put_(gold_)
            many_gold = result_num
        else:
            print("숫자가 아니다.")
        return many_gold
    except Exception as e:
        print(e)
        return 0

def jadong_juljun_attack_dead(cla, where):
    try:
        from action_zeno import clean_screen, dead_die, out_check
        from function import drag_pos
        from function import click_pos_2, click_pos_reg, imgs_set_,text_check_get, in_number_check, int_put_

        print("jadong_juljun_attack_dead")


        # 절전모드 부터 해제

        dead_juljun = False
        dead_juljun_count = 0
        while dead_juljun is False:
            dead_juljun_count += 1
            if dead_juljun_count > 7:
                dead_juljun = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                drag_pos(360, 460, 800, 460, cla)
                for i in range(10):
                    result_out = out_check(cla)
                    if result_out == True:
                        break
            else:
                dead_juljun = True
                dead_die(cla)
            time.sleep(1)



    except Exception as e:
        print(e)
        return 0
