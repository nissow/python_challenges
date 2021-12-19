from challenges import atbash_cipher, will_collide


def atbash_cipher_test():
    assert atbash_cipher('apple') == "zkkov"
    assert atbash_cipher('Hello world!') == "Svool dliow!"
    assert atbash_cipher('Christmas is the 25th of December') == "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
    print("all tests passed")



def will_collide_test():
    assert will_collide((3, 2), "y = 2x + 6")
    assert will_collide((1, 2), "y = -4x + 6")
    assert will_collide((0, 0), "y = 2x - 5")
