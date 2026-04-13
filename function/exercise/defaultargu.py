# Default argument = A default value for certain parameter
# default function is used when the argument is omitted
# to make your function more flexible, default, keyword, arbitary

def net_price(listprice, discount, tax):
    return listprice * (1 - discount) * (1 + tax)
    
print(net_price(200, 0, 0.02))