def digit_sum(n):
    string=str(n)
    if len(string)==1:
        return string
    else:
        return int(string[0])+int(digit_sum(string[1:]))

def digital_root(n):
    new_value=str(n)

    if len(new_value)==1:
        return new_value
    else:
        a=digit_sum(new_value)
        return int(digital_root(a))
