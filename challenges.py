def atbash_cipher(txt: str) -> str:
    '''
        ref :  https://edabit.com/challenge/MGALfBAXhXqqdFyqo
    '''
    if txt:
        rs = ''
        for item in txt:
            if str.isupper(item):
                count = ord(item) - ord('A')  # swap the ith item with the ith item from the end !
                rs = rs + chr(ord('Z') - count)
            elif str.islower(item):
                count = ord(item) - ord('a')
                rs = rs + chr(ord('z') - count)
            else:
                rs = rs + item
        return rs
    return ''


def will_collide(position: tuple, trajectory: str) -> bool:
    '''
        ref : https://edabit.com/challenge/9YfCbQpRPqRLzPCcg
    '''
    x, y = position

    a,b = trajectory.split("=")[1].split('x')
    a=int(a.strip())

    b=float(b.strip().replace(" ",''))
    # f(x) = y means that the function f passes through the point (x,y)
    return y == a*x + b




