num_list = [1, 2, 3, 4, 5]
year = (365, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

for i in range(len(year)):
    if(i == 0):
        print(f"今有{year[i]}天")
    else:
        print(f"{i}月有{year[i]}天")
