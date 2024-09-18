from integer_len import integer_len

def bin_dec(num:int)->int:
    sum , x = 0 , 1 
    while num > 0:
        sum += (num % 10) * x
        x *= 2
        num //= 10
    return sum

def dec_bin(num:int) -> int:
    x , sum = 1 , 0
    while num > 0:
        sum += (num % 2) * x
        num = num // 2
        x *= 10
    return sum

def bin_hex(num:int)-> str:
    hexa_dict={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    result:str = '' 
    while num > 0 :
        dec = bin_dec(num % 10000)
        if dec > 9:
            result = hexa_dict[dec] + result
        else:
            result = str(dec) + result
        num //= 10000
    return "0x" + result

def hex_bin(x:str)-> int :
    dec_dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    result = ''
    while x != '0x':
        if x[-1] in dec_dict:
            binary = dec_bin(dec_dict[x[-1]])
        else:
            binary = dec_bin(int(x[-1]))
        
        result = ("0" * (4 - integer_len(binary))) + str(binary) + result
        x = x[:-1]
    return int(result)
        
def hex_dec(x:str)->int :
    return bin_dec(hex_bin(x)) 

def dec_hex(num:int)->str:
    return bin_hex(dec_bin(num))

def dec_octal(num:int)->int:
    x , sum = 1 , 0
    while num > 0:
        sum += (num % 8) * x
        num //= 8
        x *=10
    return sum

def octal_dec(num:int)->int:
    x ,sum = 1 , 0
    while num > 0:
        sum += (num % 10) * x
        num //=10
        x *= 8
    return sum

def bin_octal(num:int)->int:
    return dec_octal(bin_dec(num))

def octal_bin(num:int)->int:
    return dec_bin(octal_dec(num))

def hex_octal(num:int)->int:
    return dec_octal(hex_dec(num))

def octal_hex(num:int)->str:
    return dec_hex(octal_dec(num))    

def main() -> None:
    print(octal_hex(2024))

if __name__=='__main__':
    main()
