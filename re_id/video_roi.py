import cv2
import json

####Variables####
#Const
pre_roi_path = '/Users/ivory/Documents/1/pre_roi/'
pp11_video_path = '/Users/ivory/Documents/1/pp151/'

ppxx_list = ['pp151']
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

#controll variables
TASK_IDX = 0
ROI_IDX = '1'
video_path = pp11_video_path + task_list[TASK_IDX] + '.mp4'
roi_path = pre_roi_path + ppxx_list[0] + '/' + task_list[TASK_IDX] + '.json'
#####################

####function part###
def play_video(video_path:str, video_name:str = 'video', play_mul:float = 1):
    """
    비디오를 재생하는 함수
    args:
        video_path (str): video path to play
        video_name (str): GUI name of Video
        play_num (float): Speed Multiple
                            e.g.) 1 -> x1, 0.5 -> x0.5
    return:
        
    """
    #Const variables
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
        
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        #algorithm space#
        ##variabels
        
        cur_frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES)) - 1
        text = f'Frame: {cur_frame_num}'

        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) , 2)
        #############
        
        #play video#
        cv2.imshow(video_name, frame)
        if cv2.waitKey(int(20 / play_mul)) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
def play_video_with_roi(video_path:str, roi_data_list, roi_idx:str, video_name:str = 'video', play_mul:float = 1):
    """
    하나의 ROI를 비디오에 그려서 재생하는 함수
    args:
        video_path (str): video path to play
        video_name (str): GUI name of Video
        play_num (float): Speed Multiple
                            e.g.) 1 -> x1, 0.5 -> x0.5
    return:
        
    """
    #Const variables
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    roi_pointer = 0
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
        
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        #algorithm space#
        ##variabels
        cur_frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES)) - 1
        roi_frame_num = roi_data_list[roi_pointer][0]
        roi_x1 = roi_data_list[roi_pointer][1]
        roi_y1 = roi_data_list[roi_pointer][2]
        roi_x2 = roi_data_list[roi_pointer][3]
        roi_y2 = roi_data_list[roi_pointer][4]
        
        ##logic
        if (cur_frame_num == roi_frame_num):
            roi_pointer += 1
            cv2.rectangle(frame, (roi_x1, roi_y1), (roi_x2, roi_y2), (255, 0, 0), thickness=3)
            roi_idx_text = f'roi_idx: {roi_idx}'
            roi_idx_text_position = (roi_x1 - 10, roi_y1 - 10)
            cv2.putText(
                frame, roi_idx_text, roi_idx_text_position, 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0) , 3)
        #global text part
        text = f'Frame: {cur_frame_num}'
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) , 3)
        #############
        
        #play video#
        cv2.imshow(video_name, frame)
        if cv2.waitKey(int(20 / play_mul)) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
####################

###code part###

#play_video(video_path)
with open(roi_path, 'r') as file:
    roi_data_dic = json.load(file)

roi_data_list = roi_data_dic[ROI_IDX]
play_video_with_roi(video_path,roi_data_list, ROI_IDX, play_mul=0.5)
