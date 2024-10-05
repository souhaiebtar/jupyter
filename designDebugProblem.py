
def convert_fahr2cels(temp_fahr):
    return (temp_fahr - 32) / 1.8
current_temp_fahr = 122
print(f"{current_temp_fahr} fahr correspond to { convert_fahr2cels(current_temp_fahr)} cels")