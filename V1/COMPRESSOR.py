from AMPLITUDE_FETCHER import get_amplitude

amp_arr = get_amplitude("069.wav")

# COMPRESSING THE AMPLITUDES
compr_amp_arr = []
def COMPRESSED_ARR_FETCH():
    # COMPRESSING THE AMPLITUDES
    for i in range(len(amp_arr)):
        if amp_arr[i] =='0':
            compr_amp_arr.append("0")
        else:
            compr_amp_arr.append(str(int(amp_arr[i]) // 10))
            print(compr_amp_arr[i][0])

    # REMOVING MINUS FROM THE AMPLITUDES
    #for i in range(len(compr_amp_arr)):
        #if compr_amp_arr[i][0] == "-": # FINDING ALL THE INDEXS WITH - IN THE FIRST PLACE
            #compr_amp_arr[i] = compr_amp_arr[i].replace("-", "0o") # REPLACING ALL THE - WITH 0

    return compr_amp_arr


print(f'{compr_amp_arr}')

