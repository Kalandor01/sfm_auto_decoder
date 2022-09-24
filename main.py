from os import sep
from sys import argv
from save_file_manager import decode_save

def imput(ask="Num: "):
    """Input but only accepts whole numbers."""
    while True:
        try: return int(input(ask))
        except ValueError: print("Not number!")

args = argv
if len(args) < 2:
    input("Open a \".sav\"(or similarly encoded) file with this exe.")
else:
    file_path = args[1]
file_ext = file_path.split(".")[-1]
file_path_stripped = "".join(file_path.rsplit("." + file_ext, 1))
file_name = file_path_stripped.split(sep)[-1]
save_num = imput("What is the seed?: ")
try:
    file_data = decode_save(save_num, file_path_stripped, file_ext)
except (UnicodeDecodeError, ValueError):
    input("Couldn't decode file. Probably wrong seed.")
else:
    print(file_data)
    if input(f'\n\nDo you want to save the results as "{file_name}.decoded.json"?(Y/N): ').upper() == "Y":
        f = open(f'{file_path_stripped}.decoded.json', "w")
        for line in file_data:
            f.write(line + "\n")
        f.close()
        input("SAVED!")