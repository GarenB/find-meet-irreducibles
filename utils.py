mapping_str_to_bits = {
    chr(ord('A') + i): 1 << i for i in range(26)
}
mapping_bits_to_str = {v: k for k, v in mapping_str_to_bits.items()}

def str_to_bits(s):
    if not isinstance(s, str):
        return None
    bits = 0
    for c in s:
        bits |= mapping_str_to_bits[c]
    return bits

def bits_to_str(bits):
    result = ''
    for bit, char in mapping_bits_to_str.items():
        if bits & bit:
            result += char
    return result if result else '0'