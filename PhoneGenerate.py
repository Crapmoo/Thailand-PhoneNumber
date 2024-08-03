from tqdm import tqdm
import os

PhoneData = [
    {
        "GenerateDescName" : "Generating 02-xxx-xxxx numbers",
        "GenerateFileName" : "02-xxx-xxxx.txt",
        "PhoneStart" : 20000000,
        "PhoneStop" : 29999999,
    },{
        "GenerateDescName" : "Generating 06x-xxx-xxxx numbers",
        "GenerateFileName" : "06x-xxx-xxxx.txt",
        "PhoneStart" : 600000000,
        "PhoneStop" : 699999999,
    },{
        "GenerateDescName" : "Generating 08x-xxx-xxxx numbers",
        "GenerateFileName" : "08x-xxx-xxxx.txt",
        "PhoneStart" : 800000000,
        "PhoneStop" : 899999999,
    },{
        "GenerateDescName" : "Generating 09x-xxx-xxxx numbers",
        "GenerateFileName" : "09x-xxx-xxxx.txt",
        "PhoneStart" : 900000000,
        "PhoneStop" : 999999999,
    }
    ]

menu_options = """
1 | 00000000 - 99999999
2 | 02-xxx-xxxx
3 | 06x-xxx-xxxx
4 | 08x-xxx-xxxx
5 | 09x-xxx-xxxx
6 | ALL
Choose = """

def GeneratePhoneNumber(Index):
    Filename = PhoneData[Index]["GenerateFileName"]
    DescName = PhoneData[Index]["GenerateDescName"]
    Start = PhoneData[Index]["PhoneStart"]
    Stop = PhoneData[Index]["PhoneStop"]
    
    with open(Filename, "w") as file:
        for i in tqdm(range(Start,Stop+1), desc=DescName, unit="number"):
            number = str(i)
            file.write(f"0{number}")
            
def GenerateEightDigit():
    total_numbers = 100000000
    with open("8-Dig.txt", "w") as file:
        for i in tqdm(range(total_numbers), desc="Generating 8-Dig numbers", unit="number"):
            number = str(i).zfill(8)
            file.write(number + "\n")
            
def GenerateAllPhoneNumber():
    GenerateEightDigit()
    for i in range(len(PhoneData)):
        GeneratePhoneNumber(i)
        
if __name__ == "__main__":
    os.system('cls')
    try:
        GenerateInput = int(input(menu_options))
        match GenerateInput:
            case 1:
                GenerateEightDigit()
            case 2:
                GeneratePhoneNumber(0)
            case 3:
                GeneratePhoneNumber(1)
            case 4:
                GeneratePhoneNumber(2)
            case 5:
                GeneratePhoneNumber(3)
            case 6:
                GenerateAllPhoneNumber()
            case _:
                print("Error Please Select Correct Choice")
    except Exception as e :
        print(f"Error\n{e}")
