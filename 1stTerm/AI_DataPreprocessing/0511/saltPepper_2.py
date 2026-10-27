def chop_nxn(in_data,input_size):
    for i in range(len(in_data)):
        for j in range(len(in_data)):
            if (i+input_size<=len(in_data[i])) & (j+input_size <= len(in_data[j])):
                chopped = in_data[i:i + input_size, j:j+input_size]
