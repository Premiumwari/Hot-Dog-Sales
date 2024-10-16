###########################
#   Project Name: Hot Dogs
#   Author Name: Payathik Manoranjan
#   Description: Keep track of the hot dogs sold and display it whenever asked. This is to find the most popular hot dog.
#   Date: 2024 October 3
total_dogs_sold = 0 
traditional_dog_sales = 0
veggie_dog_sales = 0
curry_dog_sales = 0

#input & process
while True:
    try:
        selection = int(input("Select an option:\n1. Traditional\n2. Veggie\n3. Curry\n4. Tally Sales & Exit\n"))
    except ValueError:
        continue
    if selection == 1:
        while True:
            try:
                traditional_dogs= int(input("Enter amount of traditional dogs sold:  "))
                if traditional_dogs<0:
                    continue
                else:
                    traditional_dog_sales += traditional_dogs
                break
            except ValueError:
                continue
    elif selection == 2:
        while True:
            try:
                veggie_dog = int(input("Enter amount of veggie dogs sold: "))
                if veggie_dog < 0:
                    continue
                else: 
                    veggie_dog_sales += veggie_dog
                break
            except ValueError:
                continue
    elif selection == 3:
        while True:
            try:
                curry_dog = int(input("Enter amount of curry dogs sold: "))
                if curry_dog < 0:
                    continue
                else: 
                    curry_dog_sales += curry_dog
                break  
            except ValueError:
                continue
            #output
    elif selection == 4:
        total_dogs_sold = traditional_dog_sales + veggie_dog_sales + curry_dog_sales
        if traditional_dog_sales or veggie_dog_sales or curry_dog_sales > 0:
            trad_percent = (traditional_dog_sales / total_dogs_sold) * 100
            veg_percent = (veggie_dog_sales / total_dogs_sold) * 100
            curry_percent = (curry_dog_sales / total_dogs_sold) * 100
        else:
            trad_percent = 0
            veg_percent = 0
            curry_dog_sales = 0
        print ("Total Hot Dogs Sold: "  + str(total_dogs_sold))
        print ("Total Traditional Hot Dogs Sold: " + str(traditional_dog_sales) + "(" + str(trad_percent) + "%)")
        print ("Total Veggie Hot Dogs Sold: " + str(veggie_dog_sales) + "(" + str(veg_percent) + "%)")
        print ("Total Curry  Hot Dogs Sold: " + str(curry_dog_sales) + "(" + str(curry_percent) + "%)")
        break
