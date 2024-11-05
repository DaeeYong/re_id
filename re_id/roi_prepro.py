import json
import copy

####variables####
roi_pp_path = '/Users/ivory/Documents/1/roi/pp151/' #전처리 전 roi 폴더
pre_roi_path = '/Users/ivory/Documents/1/pre_roi/pp151/' #전처리 후 roi 폴더

ppxx_list = [
    'pp71','pp79','pp80',
    'pp81','pp82_OFF','pp82_ON','pp85',
    'pp88','pp90','pp91','pp93','pp94','pp99',
    'pp100','pp102_ON','pp104_OFF','pp104_ON',
    'pp105','pp113','pp114','pp117','pp121',
    'pp128','pp134','pp138','pp139','pp140',
    'pp141','pp148','pp150','pp151','pp154'
]

#ppxx 에 따라서 변경 가능
'''
task_list = ['gait1_front',
'gait1_rear',
'gait2_front',
'gait2_rear',
'obstacle_high_front',
'obstacle_high_rear',
'obstacle_low_front',
'obstacle_low_rear',
'tug_front',
'tug_low',
'walk_fast_front',
'walk_fast_rear',
'walk_preferred_front',
'walk_preferred_rear',
'walk_slow_front',
'walk_slow_rear']

'''
task_list = [
    'pp151_omc_gait1_front_roi',
    'pp151_omc_gait2_front_roi',
    'pp151_omc_obstacle_high_front_roi',
    'pp151_omc_obstacle_low_front_roi',
    'pp151_omc_tug_front_roi',
    'pp151_omc_walk_fast_front_roi',
    'pp151_omc_walk_fast_rear_roi',
    'pp151_omc_walk_preferred_front_roi',
    'pp151_omc_walk_preferred_rear_roi',
    'pp151_omc_walk_slow_front_roi',
    'pp151_omc_walk_slow_rear_roi',
    'pp151_omc_walk_turn_front_roi',
    'pp151_omc_walk_turn_rear_roi'
]
#################

for task in task_list:
    roi_json = roi_pp_path + task + '.json'
    with open(roi_json, 'r') as file:
        roi_data = json.load(file)

    idx_list = list(roi_data.keys())

    #기존의 idx를 0,1로 변경
    for idx, each_idx in enumerate(idx_list):
        roi_data[idx] = roi_data.pop(each_idx)
    
    #예외처리: roi에 idx가 1개밖에 없는 경우 임의로 숫자를 넣어줌
    if len(idx_list) == 1:
        roi_data[1] = copy.deepcopy(roi_data[0])
    
    #가정2. frame 번호가 앞에서 특정 번호까지 비는 경우
    ##0번 idx
    copy_data = copy.deepcopy(roi_data[0][0])
    first_idx = copy_data[0] #first frame number
    for i in range(0, first_idx):
        roi_data[0].insert(i, [i, copy_data[1], copy_data[2], copy_data[3], copy_data[4]])
        
    ##1번 idx
    copy_data = copy.deepcopy(roi_data[1][0])
    first_idx = copy_data[0] #first frame number
    for i in range(0, first_idx):
        roi_data[1].insert(i, [i, copy_data[1], copy_data[2], copy_data[3], copy_data[4]])
        

    json_file_path = pre_roi_path + '/' + task + '.json'
    with open(json_file_path, "w") as file:
        json.dump(roi_data, file, indent=4)
    