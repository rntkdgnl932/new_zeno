import time

# import os
import sys


sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def auction_ready(cla):
    import numpy as np
    import cv2
    import os
    from action_zeno import menu_open
    from function import click_pos_2, click_pos_reg, imgs_set_
    from property_zeno import my_property_upload
    try:
        print("auction_ready")

        auction_ = False
        auction_count = 0
        while auction_ is False:
            auction_count += 1
            if auction_count > 7:
                auction_ = True

            print("auction_count", auction_count)
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                time.sleep(0.2)

                # 정산하기

                # 서버 정산
                click_pos_2(870, 50, cla)
                time.sleep(0.5)

                auction_settle(cla)

                # 월드 정산
                click_pos_2(777, 50, cla)
                time.sleep(0.5)

                auction_settle(cla)

                # 재화 파악하기
                my_property_upload(cla)

                # 월드거래소 판매하기

                auction_swich(cla, "world")

                # 서버거래소 판매하기
                click_pos_2(870, 50, cla)
                time.sleep(0.5)
                auction_swich(cla, "server")


                auction_ = True
            else:
                menu_open(cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\menu_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 950, 530, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
            time.sleep(0.5)
        for i in range(5):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 50, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)

def auction_settle(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, click_pos_reg, imgs_set_
    try:
        print("auction_settle")

        for i in range(5):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_point.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(555, 65, 620, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\calculate.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(530, 70, 600, 120, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\all_calculate.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 940, 960, 1030, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)

def auction_swich(cla, data):
    import numpy as np
    import cv2
    from function import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for
    try:
        print("auction_swich")

        # 판매하기
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\sell_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 70, 440, 120, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

            # 들어왔는지 확인
            for i in range(10):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\list_in.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(660, 130, 700, 170, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.1)

            # 판매전 회수하기
            for i in range(10):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\recall.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 240, 650, 950, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\recall.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 160, 650, 950, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                    else:
                        break
                time.sleep(0.5)
            # 리스트 불러와서 판매하기
            dir_path = "C:\\my_games\\zenonia"
            if data == "world":
                file_path1 = dir_path + "\\data_zeno\\imgs\\auction\\list_world.txt"
            else:
                # server
                file_path1 = dir_path + "\\data_zeno\\imgs\\auction\\list_server.txt"
            with open(file_path1, "r", encoding='utf-8-sig') as file:
                auction_list = file.read().splitlines()

            for i in range(len(auction_list)):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\list\\" + auction_list[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 160, 950, 600, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:

                    if "blessing" in auction_list[i]:
                        result = imgs_set_for(650, 160, 950, 600, cla, img, 0.85)
                        print("result", result)
                        print("len(result)", len(result))
                        if len(result) > 0:
                            print("result[len(result) - 1]", result[len(result) - 1])
                            print("result[len(result) - 1][0]", result[len(result) - 1][0])
                            print("result[len(result) - 1][1]", result[len(result) - 1][1])
                            sell_x = result[len(result) - 1][0]
                            sell_y = result[len(result) - 1][1]
                        else:
                            sell_x = imgs_.x
                            sell_y = imgs_.y
                    else:
                        sell_x = imgs_.x
                        sell_y = imgs_.y

                    click_pos_reg(sell_x, sell_y, cla)
                    time.sleep(0.3)
                    for k in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(510, 690, 585, 745, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)

                    # 현재 최저 거래단가 구하기

                    # 클릭하자
                    click_pos_2(570, 465, cla)
                    time.sleep(0.1)
                    click_pos_2(570, 465, cla)
                    time.sleep(0.1)

                    result_low = auction_start(cla)
                    result_many = auction_start2(cla)

                    how_much_ready = float(result_low) * float(result_many)
                    how_much_ = int(how_much_ready)


                    sell_start = False
                    if data == "world":
                        if how_much_ >= 100:
                            sell_start = True
                    else:
                        if how_much_ >= 10:
                            sell_start = True

                    if sell_start == True:

                        # 클릭하자
                        click_pos_2(570, 590, cla)
                        time.sleep(0.1)
                        click_pos_2(570, 590, cla)
                        time.sleep(0.1)

                        string_how_much = str(how_much_)

                        for s in range(len(string_how_much)):
                            if string_how_much[s] == "0":
                                click_pos_2(745, 665, cla)
                            if string_how_much[s] == "1":
                                click_pos_2(670, 470, cla)
                            if string_how_much[s] == "2":
                                click_pos_2(745, 470, cla)
                            if string_how_much[s] == "3":
                                click_pos_2(820, 470, cla)
                            if string_how_much[s] == "4":
                                click_pos_2(670, 535, cla)
                            if string_how_much[s] == "5":
                                click_pos_2(745, 535, cla)
                            if string_how_much[s] == "6":
                                click_pos_2(820, 535, cla)
                            if string_how_much[s] == "7":
                                click_pos_2(670, 600, cla)
                            if string_how_much[s] == "8":
                                click_pos_2(745, 600, cla)
                            if string_how_much[s] == "9":
                                click_pos_2(820, 600, cla)
                            time.sleep(0.3)

                        for k in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(510, 690, 585, 745, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                            time.sleep(0.5)
                    else:
                        for k in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(510, 690, 585, 745, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(410, 725, cla)
                            else:
                                break
                            time.sleep(0.5)
                for k in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(510, 690, 585, 745, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.5)

                for c in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\canclee.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 690, 470, 745, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.5)

    except Exception as e:
        print(e)

def auction_start(cla):
    from function import imgs_set_num
    import numpy as np
    import cv2
    try:

        if cla == "one":
            x_plus = 0
        elif cla == "two":
            x_plus = 960
        elif cla == "three":
            x_plus = 960 * 2
        elif cla == "four":
            x_plus = 960 * 3

        # 결과값
        sell_ready_now_low = ""
        x1_reg_point = 0
        x1_reg_1000 = 0

        y_1 = 475
        y_2 = 500

        x1_plus = False

        # 첫번째 소수점 및 쉼표 파악
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(256, y_1, 300, y_2, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("현재 최저 금액 : point", imgs_)
            x1_plus = True
            x1_reg_point = imgs_.x
        else:
            print("현재 최저 금액 : not point")

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\1000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(256, y_1, 275, y_2, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("현재 최저 금액 : , ", imgs_)
            x1_plus = True
            x1_reg_1000 = imgs_.x
        else:
            print("현재 최저 금액 : not 1000")


        # 값 구하기
        for k in range(4):
            if k == 0:
                # 첫째자리
                x_1 = 255
                x_2 = 270
            if k == 1:
                # 둘째자리
                x_1 = 265
                x_2 = 280
            if k == 2:
                # 셋째자리
                x_1 = 275
                x_2 = 290
            if k == 3:
                # 넷째자리
                x_1 = 285
                x_2 = 300



            # sell_ready_now_low

            if x1_plus == True:
                if k != 0:
                    if x1_reg_point != 0 or x1_reg_1000 != 0:
                        # 270, 278, 286
                        if 266 + x_plus < x1_reg_point < 274 + x_plus or 266 + x_plus < x1_reg_1000 < 274 + x_plus:
                            if k > 0:
                                x_1 = x_1 + 4
                                x_2 = x_2 + 4
                        if 274 + x_plus < x1_reg_point < 282 + x_plus or 274 + x_plus < x1_reg_1000 < 282 + x_plus:
                            if k > 1:
                                x_1 = x_1 + 4
                                x_2 = x_2 + 4
                        if 282 + x_plus < x1_reg_point < 290 + x_plus or 282 + x_plus < x1_reg_1000 < 290 + x_plus:
                            if k > 2:
                                x_1 = x_1 + 4
                                x_2 = x_2 + 4

            # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\vacant.PNG"
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.95)
            # if imgs_ is not None and imgs_ != False:
            #     print("숫자 없다", x_1, y_1, x_2, y_2)
            #
            # else:


                # sell_ready_now_low = text_check_get(x_1, y_1, x_2, y_2, cla)

            for i in range(10):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    # data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
                    # print(data, imgs_)

                    left_x1 = 266
                    right_x1 = 274

                    if k != 0:
                        # 270, 278, 286
                        if k == 1:
                            if x1_reg_point != 0 and (266 + x_plus < x1_reg_point < 274 + x_plus):
                                sell_ready_now_low += "."
                        if k == 2:
                            if x1_reg_point != 0 and (274 + x_plus < x1_reg_point < 282 + x_plus):
                                sell_ready_now_low += "."
                        if k == 3:
                            if x1_reg_point != 0 and (282 + x_plus < x1_reg_point < 290 + x_plus):
                                sell_ready_now_low += "."
                        sell_ready_now_low += str(i)
                    else:
                        sell_ready_now_low += str(i)

                    break


            print("3 되면 끝 : ", k)

        print("현재최저단가", sell_ready_now_low)
        return sell_ready_now_low
    except Exception as e:
        print(e)
        return 0

def auction_start2(cla):
    from function import imgs_set_num
    import numpy as np
    import cv2
    try:

        # 결과값
        sell_ready_now_low = ""

        y_1 = 385
        y_2 = 430


        x1_plus = False

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\many\\1000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(700, y_1, 800, y_2, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("1000 여부 : , ", imgs_)
            x1_plus = True
        else:
            print("1000 여부 : not 1000")

        if x1_plus == True:

            # 값 구하기
            for k in range(4):
                if k == 0:
                    # 첫째자리
                    x_1 = 715
                    x_2 = 735
                if k == 1:
                    # 둘째자리
                    x_1 = 732
                    x_2 = 752
                if k == 2:
                    # 셋째자리
                    x_1 = 745
                    x_2 = 765
                if k == 3:
                    # 넷째자리
                    x_1 = 755
                    x_2 = 775



                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\many\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        # data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)

                        sell_ready_now_low += str(i)

                        break


                print("3 되면 끝 : ", k)
        else:

            sell_ready_now_low_3 = ""
            sell_ready_now_low_2 = ""
            sell_ready_now_low_1 = ""

            for k in range(3):
                if k == 0:
                    # 첫째자리
                    x_1 = 725
                    x_2 = 744
                if k == 1:
                    # 둘째자리
                    x_1 = 735
                    x_2 = 758
                if k == 2:
                    # 셋째자리
                    x_1 = 745
                    x_2 = 768



                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\many\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        # data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)

                        sell_ready_now_low_3 += str(i)

                        break

                print("2 되면 끝 : ", k)

            for k in range(2):
                if k == 0:
                    # 첫째자리
                    x_1 = 730
                    x_2 = 751
                if k == 1:
                    # 둘째자리
                    x_1 = 740
                    x_2 = 764


                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\many\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        # data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)

                        sell_ready_now_low_2 += str(i)

                        break

                print("1 되면 끝 : ", k)

            for k in range(1):
                if k == 0:
                    # 첫째자리
                    x_1 = 735
                    x_2 = 764


                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\many\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        # data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)

                        sell_ready_now_low_1 += str(i)

                        break

                print("0 되면 끝 : ", k)
            print("333", sell_ready_now_low_3)
            print("222", sell_ready_now_low_2)
            print("111", sell_ready_now_low_1)
            result_many_ready = [int(sell_ready_now_low_3), int(sell_ready_now_low_2), int(sell_ready_now_low_1)]
            sell_ready_now_low = max(result_many_ready)

        print("판매수량", sell_ready_now_low)
        return sell_ready_now_low
    except Exception as e:
        print(e)
        return 0

def auction_start_ex(cla):
    from function import imgs_set_num
    import numpy as np
    import cv2
    try:

        # 결과값
        sell_ready_now_low = ""
        sell_ready_last = ""
        x1_reg_point = 0
        x1_reg_1000 = 0
        x2_reg_point = 0
        x2_reg_1000 = 0


        x1_plus = False

        x2_plus = False

        # 첫번째 소수점 및 쉼표 파악
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(256, 490, 300, 505, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("현재 최저 금액 : point", imgs_)
            # 첫번째 소수점 x = 379, 378
            # 두번째 소수점 x = 387, 386
            # 세번째 소수점 x = 395
            x1_plus = True
            x1_reg_point = imgs_.x
        else:
            print("현재 최저 금액 : not point")

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\1000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(256, 490, 275, 505, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("현재 최저 금액 : , ", imgs_)
            x1_plus = True
            x1_reg_1000 = imgs_.x
        else:
            print("현재 최저 금액 : not 1000")

        # 두번째 소수점 및 쉼표 파악
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(256, 505, 300, 527, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("마지막 거래 금액 : point", imgs_)
            x2_plus = True
            x2_reg_point = imgs_.x
        else:
            print("마지막 거래 금액 : not point")

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\1000.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_num(256, 505, 275, 527, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("마지막 거래 금액 : , ", imgs_)
            x2_plus = True
            x2_reg_1000 = imgs_.x
        else:
            print("마지막 거래 금액 : not 1000")


        # 값 구하기
        for k in range(4):
            if k == 0:
                # 첫째자리
                x_1 = 255
                x_2 = 269
                x_3 = 255
                x_4 = 269
            if k == 1:
                # 둘째자리
                x_1 = 265
                x_2 = 279
                x_3 = 265
                x_4 = 279
            if k == 2:
                # 셋째자리
                x_1 = 274
                x_2 = 288
                x_3 = 274
                x_4 = 288
            if k == 3:
                # 넷째자리
                x_1 = 283
                x_2 = 297
                x_3 = 283
                x_4 = 297

            y_1 = 480
            y_2 = 500
            y_3 = 500
            y_4 = 520

            # sell_ready_now_low

            if x1_plus == True:
                if k != 0:
                    if x1_reg_point != 0 or x1_reg_1000 != 0:
                        # 270, 278, 286
                        if 266 < x1_reg_point < 274 or 266 < x1_reg_1000 < 274:
                            if k > 0:
                                x_1 = x_1 + 5
                                x_2 = x_2 + 5
                        if 274 < x1_reg_point < 282 or 274 < x1_reg_1000 < 282:
                            if k > 1:
                                x_1 = x_1 + 5
                                x_2 = x_2 + 5
                        if 282 < x1_reg_point < 290 or 282 < x1_reg_1000 < 290:
                            if k > 2:
                                x_1 = x_1 + 5
                                x_2 = x_2 + 5

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\vacant.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("숫자 없다")

            else:


                # sell_ready_now_low = text_check_get(x_1, y_1, x_2, y_2, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        # data = "현재 최저 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)


                        if k != 0:
                            # 270, 278, 286
                            if k == 1:
                                if x1_reg_point != 0 and (266 < x1_reg_point < 274):
                                    sell_ready_now_low += "."
                            if k == 2:
                                if x1_reg_point != 0 and (274 < x1_reg_point < 282):
                                    sell_ready_now_low += "."
                            if k == 3:
                                if x1_reg_point != 0 and (282 < x1_reg_point < 290):
                                    sell_ready_now_low += "."
                            sell_ready_now_low += str(i)
                        else:
                            sell_ready_now_low += str(i)

                        break

            # sell_ready_last

            if x2_plus == True:
                if k != 0:
                    if x2_reg_point != 0 or x2_reg_1000 != 0:
                        if 266 < x2_reg_point < 274 or 266 < x2_reg_1000 < 274:
                            if k > 0:
                                x_3 = x_3 + 5
                                x_4 = x_4 + 5
                        if 274 < x2_reg_point < 282 or 274 < x2_reg_1000 < 282:
                            if k > 1:
                                x_3 = x_3 + 5
                                x_4 = x_4 + 5
                        if 282 < x2_reg_point < 290 or 282 < x2_reg_1000 < 290:
                            if k > 2:
                                x_3 = x_3 + 5
                                x_4 = x_4 + 5


            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\vacant.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_num(x_3, y_3, x_4, y_4, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("숫자 없다")

            else:


                # sell_ready_last = text_check_get(x_3, y_3, x_4, y_4, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_num(x_3, y_3, x_4, y_4, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        # data = "마지막 거래 금액 : 숫자 " + str(i) + " 보여"
                        # print(data, imgs_)

                        if k != 0:
                            # 첫번째 소수점 x = 379, 378
                            # 두번째 소수점 x = 387, 386
                            # 세번째 소수점 x = 395, 394
                            if k == 1:
                                if x2_reg_point != 0 and (266 < x2_reg_point < 274):
                                    sell_ready_last += "."
                            if k == 2:
                                if x2_reg_point != 0 and (274 < x2_reg_point < 282):
                                    sell_ready_last += "."
                            if k == 3:
                                if x2_reg_point != 0 and (282 < x2_reg_point < 290):
                                    sell_ready_last += "."
                            sell_ready_last += str(i)
                        else:
                            sell_ready_last += str(i)

                        break

            print("3 되면 끝 : ", k)



        return sell_ready_now_low, sell_ready_last
    except Exception as e:
        print(e)
        return 0
