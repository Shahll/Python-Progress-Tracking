with open("/home/shall/Documents/code/hardware/stundets.csv") as file:
    for line in file:
        name, county = line.rstrip().split(",")
        print(f"{name} is in {county}")