legs = {1:['j_c1_rf','j_thigh_rf','j_tibia_rf'],
        2:['j_c1_rm','j_thigh_rm','j_tibia_rm'],
        3:['j_c1_rr','j_thigh_rr','j_tibia_rr'],
        4:['j_c1_lf','j_thigh_lf','j_tibia_lf'],
        5:['j_c1_lm','j_thigh_lm','j_tibia_lm'],
        6:['j_c1_lr','j_thigh_lr','j_tibia_lr']}
present_positions = [[0,0,0],
                     [0,0,0],
                     [0,0,0],
                     [0,0,0],
                     [0,0,0],
                     [0,0,0]]

new_values = {'j_c1_lm': 0.1, 'j_thigh_lm': 0.2, 'j_tibia_lm': 0.3}

def merge_legs_positions_dict():
    count = 0
    merged_positions = {}
    for leg_group in legs.values():
        k = 0
        for joint_name in leg_group:
            temp = present_positions[count]
            merged_positions[joint_name] = temp[k]
            k += 1
        count += 1
    return merged_positions

def update_present_positions():
    for index, leg_group in legs.items():
        for joint_name in leg_group:
            if joint_name in new_values:
                k = leg_group.index(joint_name)
                present_positions[index - 1][k] = new_values[joint_name]

update_present_positions()

print(present_positions)

