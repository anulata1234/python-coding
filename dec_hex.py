def dec_hex(d):
    if d<16:
        return ( "inavlid number")
    else:
        hex_num = ''
        map_num = {10 : 'a',11:'b', 12:'c',13:'d',14:'e',15:'f'}
        quotient = 1
    while quotient:
        remainder = d%16
        quotient = d//16
        d = quotient
        if remainder <= 9:
            hex_num = hex_num +str(remainder)
        else:
            hex_num = hex_num+map_num[remainder]

    return hex_num[::-1]


print(dec_hex(4567890))
