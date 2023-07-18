import time
import sys
import cv2
import numpy as np

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def jadong_start(cla, where):
    from action_zeno import juljun_potion_check, juljun_maul_potion, dead_die
    from function import click_pos_2
    try:
        print("jadong_start")
        # jadong_juljun_attack_gold_check(cla, where)
        # 절전 자동 모드 아니라면 진입하기
        result_arrived = jadong_arrive_check(cla, where)
        if result_arrived == True:
            result_potion = juljun_potion_check(cla)
            if result_potion == False:
                juljun_maul_potion(cla)


        else:
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
                drag_pos(360, 460, 600, 460, cla)

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
                        # 전리품 주는 몬스터 클릭
                        map_junlipoom_click(cla, where)
                        # 지도에 표시된 포탈 클릭
                        map_spot_click(cla, where)
                        # 확인 클릭
                        confirm_all(cla)
                        # 도착 확인
                        spot_arrive(cla, where)
                        # 사냥 중인지 확인
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
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\map_list\\" + click_reg + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 120, 960, 1020, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                in_map_ = True
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
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\maul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 120, 870, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(850, 200, 850, 700, cla)
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
                click_pos_2(150, 100, cla)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

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

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\spot_click_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 340, 520, 390, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\spot_click_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(560, 380, 655, 725, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    in_map_ = True

            else:

                if click_reg == 'red_hwangya_1':
                    click_pos_2(110, 570, cla)
                else:

                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\junlipoom\\" + click_reg + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 160, 300, 1020, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
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
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\map_spot.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(310, 170, 950, 840, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_map_ = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def spot_arrive(cla, where):
    try:
        from action_zeno import clean_screen, out_check
        from function import click_pos_2, click_pos_reg, imgs_set_
        print("spot_arrive")
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
            time.sleep(2)
    except Exception as e:
        print(e)
        return 0

def juljun_arrive(cla, where):
    try:
        from action_zeno import clean_screen, out_check
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("map_list_open")
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
                result_attack = jadong_juljun_attack_check(cla, where)
                if result_attack == True:
                    in_map_ = True
                else:
                    for i in range(3):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            drag_pos(360, 460, 600, 460, cla)
                        else:
                            break

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

                    click_pos_2(905, 790, cla)
                    time.sleep(0.3)
                    click_pos_2(30, 930, cla)
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
            elif jadong_spl_[3] == "17갑옷":
                click_reg = 'lolel_river_3'
        elif jadong_spl_[2] == "아라크1층":
            click_reg = 'alak_1'
        elif jadong_spl_[2] == "아라크3층":
            click_reg = 'alak_3'
        elif jadong_spl_[2] == "엘라움계곡":
            if jadong_spl_[3] == "30목걸이장갑":
                click_reg = 'elaum_1'
            elif jadong_spl_[3] == "31벨트":
                click_reg = 'elaum_2'
            elif jadong_spl_[3] == "33반귀투":
                click_reg = 'elaum_3'
        elif jadong_spl_[2] == "붉은황야":
            click_reg = 'red_hwangya_1'
        elif jadong_spl_[2] == "카나크협곡":
            click_reg = 'canak_1'
        elif jadong_spl_[2] == "로쿠광산":
            click_reg = 'locoo_1'
        return click_reg
    except Exception as e:
        print(e)
        return 0

def jadong_arrive_check(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("jadong_arrive_check")

        arrive = False

        result_arrive = jadong_juljun_attack_check(cla, where)
        if result_arrive == True:

            gold_1 = jadong_juljun_attack_gold_check(cla, where)
            time.sleep(15)
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
                        drag_pos(360, 460, 600, 460, cla)
                        break
                    time.sleep(1)

        else:
            for i in range(3):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(360, 460, 600, 460, cla)
                else:
                    break
        time.sleep(0.5)


        return arrive
    except Exception as e:
        print(e)
        return 0

def jadong_juljun_attack_check(cla, where):
    try:
        from action_zeno import clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_, text_check_get
        print("jadong_juljun_attack_check")

        go_ = False
        dun_ = False

        # 왼쪽 위 장소 맞는지 파악하고 맞다면 아래 파악 ... 던전은 추후 추가하기...

        if '_' in where:
            jadong_spl_ = where.split("_")
        if jadong_spl_[0] == "사냥":
            result_pic = map_pic_name(cla, where)
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
                            go_ = True
                            in_map_ = True
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\rest_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            in_map_ = True
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\dead_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            in_map_ = True
                        time.sleep(0.1)
                else:
                    print("절전공격모드 아님")
        else:
            if jadong_spl_[0] == "일반" or jadong_spl_[0] == "특수":
                # jadong_spl_[1] == "업보, 지옥, 죄악, 저주, 마족, 아르카스"
                title_ = text_check_get(45, 90, 140, 160, cla)
                # print("title_", title_)
                # print("jadong_spl_[1]", jadong_spl_[1])

                equal = 0
                for i in range(len(title_)):
                    for z in range(len(jadong_spl_[1])):
                        if title_[i] == jadong_spl_[1][z]:
                            equal += 1
                            # print("equal", title_[i], jadong_spl_[1][z])
                            if equal > 1:
                                dun_ = True
                                break


                    # if jadong_spl_[1] == "업보":
                    #
                    # elif jadong_spl_[1] == "지옥":
                    #
                    # elif jadong_spl_[1] == "죄악":
                    #
                    # elif jadong_spl_[1] == "저주":
                    #
                    # elif jadong_spl_[1] == "마족":
                    #
                    # elif jadong_spl_[1] == "아르카스":
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
                                go_ = True
                                in_map_ = True
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\rest_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                in_map_ = True
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\dead_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                in_map_ = True
                            time.sleep(0.1)
                    else:
                        print("절전공격모드 아님")

            elif jadong_spl_[0] == "파티":
                print("이건 준비중...")

            else:
                print("원하는 장소가 아니다.")
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