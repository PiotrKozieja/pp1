def occurs(number, array):
    e = 0
    for i in array:
        if number == i:
            e = e+1
    if e != 0:
        return(f"Number {number} appears in array")
    else:
        return(f"Number {number} doesnt appear in array")
print(occurs(14, [15, 38, 7, 23, 14]))