# Isaias Hernandez
# Extra Credit Attempted

def metric_f2c(f_temp): # Metric units function
    met_temp = (int(f_temp) - 32) * (5/9)
    return met_temp


def imperial_c2f(c_temp): # Imperial Function
    imptemp = (int(c_temp) * 5 / 9) + 32
    return imptemp


def metric_f2m(f_distance): # Meters function
    met_distance = int(f_distance) / 3.281
    return met_distance


def imperial_m2f(m_distance): # Feet Function
    imp_distance = int(m_distance) * 3.281
    return imp_distance


def print_backwards(data): # extra credit
    txt = data[::-1] # tells the compiler to write the data backwards from the array
    return txt


print(" WELCOME TO UNIT CONVERT MACHINE 2020: ")
print(" 0. Exit Program\n 1. Convert F to C\n 2. Convert C to F")
print(" 3. Convert Ft to M\n 4. Converts M to Ft \n 5. Prints Input Data in Reverse ")

# Main menu
while True:

    cin = input("\n SELECT YOUR CHOICE: ")

    if cin == "0":
        break

    elif cin == "1":
        print(metric_f2c(input(" ENTER A TEMP IN F: ")), "C")

    elif cin == "2":
        print(imperial_c2f(input(" enter a temp in C: ")), "F")

    elif cin == "3":
        print(metric_f2m(input(" enter distance in Feet: ")), "M")

    elif cin == "4":
        print(imperial_m2f(input(" enter distance in Meters")), "Ft")

    elif cin == "5":
        print(print_backwards(input(" Enter a set of data: ")))

    else:
        print("ERROR: DATA CURRUPT TRY AGAIN.")
