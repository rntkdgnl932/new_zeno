# pyqt5 부분
rowcount = 0
colcount = 0
rehi_ = 'none'
thisRow = 0
thisCol = 0
table_datas = ""
onCharacter = 0
onDunjeon = "none"
onHunt = "none"
onMaul = "none"

isgloballoop = False

# 기존 오토모드 관련###############################################
one_cla_id = "none"
one_cla_pw = "none"
two_cla_id = "none"
two_cla_pw = "none"
# 1번
mypotion_1 = 9999
myId_1 = 0
# 2번
mypotion_2 = 9999
myId_2 = 0
# 3번
mypotion_3 = 9999
myId_3 = 0
# 4번
mypotion_4 = 9999
myId_4 = 0
# 현재실행중인 클라우드
now_cla = 'none'
global_howcla = 'none'

# 제노니아 관련
# 버젼
# import os

dir_path = "C:\\my_games\\zenonia\\data_zeno"
file_path = dir_path + "\\mymodule\\version.txt"
file_path2 = "C:\\my_games\\mouse\\port.txt"

with open(file_path, "r", encoding='utf-8-sig') as file:
    version_ = file.read()
    print("version???", version_)

with open(file_path2, "r", encoding='utf-8-sig') as file:
    read_port = file.read().splitlines()
    COM_ = read_port[0]
    speed_ = int(read_port[1])
    print("COM???", COM_)
    print("speed_???", speed_)

this_game = "제노니아"
game_folder = "zenonia"
data_folder = "data_zeno"

# 자동모드 관련
potion_count = 0
dead_count = 0

# 던전 진행중 여부
now_dungeon_ing = False
skill_checked_ = False
now_ing_schedule = "none"
# 강제로 돈벌기
forcee_not_sub = False
force_sub_quest = False
onForceGold = 5000000
onForceGoldSpot = "none"
onForceGoldSpot_go = "none"
onCollection = False



# 일일퀘스트
sub_quest_count = 0

# 가방 열어 골드 파악하는거 서브퀘스트일때 and 300초마다
bag_open_count = 0
bag_full_open_count = 0

# 마우스 관련
mouse_speed = 20
mouse_pm = 3

# 아두이노
now_arduino = "none"