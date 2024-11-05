import sys
import json
sys.path.append('/Users/ivory/Desktop/WorkSpace/gaitome/src/')
from dragon import dragonV

# variables
##Const
openpose_path = '/Users/ivory/Documents/1/openpose_pp11/'
op_joint_path = '/Users/ivory/Documents/1/openpose_data/2d_joint/'

task_list = [
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
## Control
TASK_IDX = 3
##
openpose_json_folder_path = openpose_path + task_list[TASK_IDX]
json_list = dragonV.get_jsons_list(openpose_json_folder_path)

op_dict = {}
for cur_frame_number, each_json in enumerate(json_list):
    with open(openpose_json_folder_path + '/' + each_json, 'r') as file:
        cur_json = json.load(file)
    
    #하나의 json file에 존재하는 사람 수
    people_list = cur_json['people']
    people_len = len(people_list)
    
    for people_idx, cur_people in enumerate(people_list):
        joint_2d = cur_people['pose_keypoints_2d']
        joint_2d.insert(0, cur_frame_number)
        
        if people_idx in op_dict:
            op_dict[people_idx].append(joint_2d)
        else:
            op_dict[people_idx] = []
            op_dict[people_idx].append(joint_2d)

with open(op_joint_path + '/' + task_list[TASK_IDX] + '.json', 'w', encoding='utf-8') as file:
    json.dump(op_dict, file, ensure_ascii=False, indent=4)