from openpyxl import Workbook
import json
#Variables #
##Const

op_xlsx_path = '/Users/ivory/Documents/1/openpose_data/excel/pp151/' # 저장할 openpose 엑셀 경로
op_joint_path = '/Users/ivory/Documents/1/openpose_data/2d_joint/pp151/' #json 경로
'''task_list = [
    'gait1_front',
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
    'walk_slow_rear'
]

'''

task_list = [
    'pp151_omc_gait1_front',
    'pp151_omc_gait2_front',
    'pp151_omc_obstacle_high_front',
    'pp151_omc_obstacle_low_front',
    'pp151_omc_tug_front',
    'pp151_omc_walk_fast_front',
    'pp151_omc_walk_fast_rear',
    'pp151_omc_walk_preferred_front',
    'pp151_omc_walk_preferred_rear',
    'pp151_omc_walk_slow_front',
    'pp151_omc_walk_slow_rear',
    'pp151_omc_walk_turn_front',
    'pp151_omc_walk_turn_rear'
]
#logic
for TASK_IDX, _ in enumerate(task_list):
    op_json = op_joint_path + task_list[TASK_IDX] + '.json'
    op_xlsx = op_xlsx_path + task_list[TASK_IDX] + '.xlsx'
    
    with open(op_json, 'r') as file:
        op_json_dict = json.load(file)

    wb = Workbook()
    for people_idx in op_json_dict:
        print(people_idx)
        sheet = wb.create_sheet(title=f'OpIdx{people_idx}')
        wb.active = wb[f'OpIdx{people_idx}']
        ws = wb.active
        
        for row in op_json_dict[f'{people_idx}']:
            ws.append(row)

    wb.save(op_xlsx)