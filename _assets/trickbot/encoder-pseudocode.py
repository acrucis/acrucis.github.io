import sys

def encode_cb64(msg, msg_size):
    current_char = 0
    n_chars = msg_size
    char_array = list(msg)

    while (n_chars != 0):
        n_chars = (n_chars - 1 >> 2) + 1
        current_char = char_array[0]
        ivar6 = 0
        ivar7 = 0
        uvar4 = 0

        if current_char != '=':
            ivar6 = 6
        
        # c < A > z
        if ((ord(current_char) < 65) or (90 < ord(current_char))):
            # & c < a > z
            if ((ord(current_char) < 97) or (122 < ord(current_char))):
                # c < 0 > 9
                if ((ord(current_char) < 48) or (56 < ord(current_char))):
                    # c == +
                    if (ord(current_char == 43)):
                        uvar4 = 0x3e
                
                    else:
                        # c == /
                        if (ord(current_char) == 47):
                            uvar4 = 0x3f
                        
                        else:
                            uvar4 = 0
                            ivar6 = ivar6 - 2

                else:
                    uvar4 = ord(current_char) + 4    
                
            else:
                uvar4 = ord(current_char) - 0x47
        
        else:
            uvar4 = ord(current_char) - 0x41

        current_char = char_array[0]

        # c == '='
        if (ord(current_char) != 61):
            uvar4 = uvar4 << 6
            ivar6 = ivar6 + 6

        # c < A > z
        if ((ord(current_char) < 65) or (90 < ord(current_char))):
            # & c < a > z
            if ((ord(current_char) < 97) or (122 < ord(current_char))):
                # c < 0 > 9
                if ((ord(current_char) < 48) or (56 < ord(current_char))):
                    # c == +
                    if (ord(current_char == 43)):
                        uvar4 = 0x3e
                
                    else:
                        #c == /
                        if (ord(current_char) == 47):
                            uvar4 = 0x3f
                        
                        else:
                            uvar4 = 0
                            ivar6 = ivar6 - 2
                
                else:
                    uvar4 = uvar4 | ord(current_char) + 4
                
            else:
                uvar4 = uvar4 | ord(current_char) - 0x47

        else:
            uvar4 = uvar4 | ord(current_char) - 0x41

        current_char = char_array[1]

         # c == '='
        if (ord(current_char) != 61):
            uvar4 = uvar4 << 6
            ivar6 = ivar6 + 6

        # c < A > z
        if ((ord(current_char) < 65) or (90 < ord(current_char))):
            # & c < a > z
            if ((ord(current_char) < 97) or (122 < ord(current_char))):
                # c < 0 > 9
                if ((ord(current_char) < 48) or (56 < ord(current_char))):
                    # c == +
                    if (ord(current_char == 43)):
                        uvar4 = 0x3e

                    else:
                        #c == /
                        if (ord(current_char) == 47):
                            uvar4 = 0x3f
                        
                        else:
                            uvar4 = 0
                            ivar6 = ivar6 - 2

                else:
                    uvar4 = uvar4 | ord(current_char) + 4
                
            else:
                uvar4 = uvar4 | ord(current_char) - 0x47

        else:
            uvar4 = uvar4 | ord(current_char) - 0x41

        current_char = char_array[2]

         # c == '='
        if (ord(current_char) != 61):
            uvar4 = uvar4 << 6
            ivar6 = ivar6 + 6

        # c < A > z
        if ((ord(current_char) < 65) or (90 < ord(current_char))):
            # & c < a > z
            if ((ord(current_char) < 97) or (122 < ord(current_char))):
                # c < 0 > 9
                if ((ord(current_char) < 48) or (56 < ord(current_char))):
                    # c == +
                    if (ord(current_char == 43)):
                        uvar4 = 0x3e

                    else:
                        #c == /
                        if (ord(current_char) == 47):
                            uvar4 = 0x3f
                        
                        else:
                            uvar4 = 0
                            ivar6 = ivar6 - 2

                else:
                    uvar4 = uvar4 | ord(current_char) + 4
                
            else:
                uvar4 = uvar4 | ord(current_char) - 0x47

        else:
            uvar4 = uvar4 | ord(current_char) - 0x41

        while (ivar6 != 0):
            ivar6 = ivar6 + -8

            undefined_ptr = str(uvar4 >> (ivar6 & 0x1f))
            ivar7 = ivar7 + 1

        char_array = char_array + 4
        n_chars = n_chars - 1
        undefined_ptr = 0
        return

if __name__=='__main__':
    message = "the silver cat feeds when blue meets yellow in the west"
    encode_cb64(message, sys.getsizeof(message) * 4)