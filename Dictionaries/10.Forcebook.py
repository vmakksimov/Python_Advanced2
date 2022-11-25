def add_user(forces_dict, side_to_join, user_to_add):
    for side, user in forces_dict.items():
        if user_to_add in user:
            return forces_dict
    if side_to_join not in forces_dict:
        forces_dict[side_to_join] = []
        forces_dict[side_to_join].append(user_to_add)
    else:
        if user_to_add not in forces_dict[side_to_join]:
            forces_dict[side_to_join].append(user_to_add)
    return forces_dict


def transfer_user(forces_dict, side_to_transfer, user_to_transfer):
    for side, user in forces_dict.items():
        if user_to_transfer in user:
            forces_dict[side].remove(user_to_transfer)
            return add_user(forces_dict, side_to_transfer, user_to_transfer)
    return add_user(forces_dict, side_to_transfer, user_to_transfer)

command = input()
sides = {}
new_sides = {}
while not command == 'Lumpawaroo':
    data = command.split(' | ')
    if len(data) > 1:
        force_side, force_user = command.split(' | ')
        sides = add_user(sides, force_side, force_user)
    else:
        force_user, force_side = command.split(' -> ')
        sides = transfer_user(sides, force_side, force_user)
        print(f'{force_user} joins the {force_side} side!')

    command = input()

sorted_by_name = sorted(sides.items(), key=lambda x: (-len(x[1]), x[0]))
for key, value in sorted_by_name:
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        for v in sorted(value):
            print(f'! {"".join(v)}')
