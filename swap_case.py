def swap_case(s):
    return "".join([i.upper() if ord(i) in range(97, 123) else i.lower() for i in s])
        

