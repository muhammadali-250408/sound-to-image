import ast

test = ['371', '460', '0o152', '441', '126', '206', '0o357', '269', '103', '100', '0o293', '432', '339', '0o203', '242', '3', '226', '0o917', '387', '199', '544', '0o718', '532', '163', '0o26', '348', '224', '74', '618', '459', '438', '468', '0o414']
def amp_to_pixel(amp_arr):
    for i in range(len(amp_arr)):

        if amp_arr[i][0] == "-":
            if len(amp_arr[i]) >= 4:
                if amp_arr[i][3] == "0" and len(amp_arr[i]) != 3:
                    amp_arr[i] = f"[0, {amp_arr[i][1:4]},{amp_arr[i][4:]}]"
                else:
                    amp_arr[i] = f"[0, {amp_arr[i][1:3]},{amp_arr[i][3:]}]"

            if len(amp_arr[i]) == 4:
                amp_arr[i] = f"[0, {amp_arr[i][1:2]},{amp_arr[i][2:]}]"

            elif len(amp_arr[i]) == 3:
                amp_arr[i] = f"[0, {amp_arr[i][1]},{amp_arr[i][2]}]"
            else:
                amp_arr[i] = f"[0, {amp_arr[i][1]}, 0]"


        else:
            if len(amp_arr[i]) > 3:
                if amp_arr[i][2] == "0":
                    amp_arr[i] = f"[100, {amp_arr[i][:3]},{amp_arr[i][3:]}]"
                else:

                    amp_arr[i] = f"[100, {amp_arr[i][:2]},{amp_arr[i][2:]}]"

            elif len(amp_arr[i]) == 3:
                amp_arr[i] = f"[100, {amp_arr[i][:2]},{amp_arr[i][2:]}]"

            elif len(amp_arr[i]) == 2:
                amp_arr[i] = f"[100, {amp_arr[i][:1]},{amp_arr[i][1:]}]"
            else:
                amp_arr[i] = f"[100, {amp_arr[i]}, 0]"


    # CLEANING THE ARRAY
    print(amp_arr)
    amp_arr_clean = [ast.literal_eval(item) for item in amp_arr]

    return amp_arr_clean
