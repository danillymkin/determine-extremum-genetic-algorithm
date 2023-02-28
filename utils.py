def float_to_bin_array(x):
    x_bin = bin(int(round((x + 5) * 1000)))[2:].zfill(20)
    return [int(x) for x in list(x_bin)]


def bin_array_to_float(bin_arr):
    x_bin = ''.join([str(x) for x in bin_arr])

    integer_part = x_bin[:10]
    fractional_part = x_bin[10:]

    int_val = int(integer_part, 2) - 5
    frac_val = int(fractional_part, 2) / 1024

    result = int_val + frac_val
    return result
