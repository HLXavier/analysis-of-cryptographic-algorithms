from utils import * 

# If a function is to satisfy the strict avalanche criterion, 
# then each of its output bits should change with a probability 
# of one half whenever a single input bit x is complemented to x'.
    

def strict_avalanche_criterion(bin1, bin2):
    assert len(bin1) == len(bin2)
    diff = xor(bin1, bin2)
    return 100 * diff / len(bin1)


def avalanche_effect(encrypt, key, encryption_rounds, executions=100):
    avarege = 0

    for _ in range(executions):
        plain_text = random_bytes(16)

        new_key = shift_bit(key)

        cipher1 = encrypt(plain_text, key, encryption_rounds)
        cipher2 = encrypt(plain_text, new_key, encryption_rounds)

        bin_cipher1 = str_to_bin(hex_to_str(cipher1))
        bin_cipher2 = str_to_bin(hex_to_str(cipher2))

        avarege += strict_avalanche_criterion(bin_cipher1, bin_cipher2)

    return avarege / executions
