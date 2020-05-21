mf_find = "HDFC Children Gift Fund-Savings"
with open("Mutual Fund Schemes Data.txt", "r")as mf:
    columns_dict = {}
    columns = mf.readline(0).split(";")
    print(columns)
    for i in range(0,len(columns)):
        columns_dict[columns[i]] = "Blank"
    for lines in (mf):
        if(mf_find in lines):
            print("Found scheme")
            a = lines.split(";")
            print(a)

            break
        else:
            continue