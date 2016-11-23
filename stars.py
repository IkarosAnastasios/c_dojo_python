x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
for num in x:
    if str(num).isdigit()==True:
        print '*'*num
    else:
        print num[:1]*len(num)
