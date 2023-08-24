def reverse_hex_and_decode(hex_string):

    hex_string = hex_string.replace(" ", "").replace("\n", "")


    reversed_hex = "".join(hex_string[i:i+2][::-1] for i in range(0, len(hex_string), 2))


    decoded_string = bytearray.fromhex(reversed_hex).decode()

    return reversed_hex, decoded_string


hex_string = "76f60247f60253e2136313e2135373e2739302778656275602573796e6760207f627470283030303e2024786560253e2136313e2135373e2739302861637021602368696c646023616c6c656460237b696c6c657070216e646024786560237b696c6c6570702861637021602368696c646023616c6c6564602368616c6c656e67656e2d0a037f60247865602368616c6c656e67656029637021602762716e646368696c64602f6660253e2136313e2135373e27393e2024696460297f65702375656024786963702f3d0a0"

reversed_hex, decoded_string = reverse_hex_and_decode(hex_string)
print("Reversed Hex:", reversed_hex)
print("Decoded String:", decoded_string)
