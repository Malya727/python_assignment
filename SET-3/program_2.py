def write_into_file():
    fp = open("Demonetization.txt" , "w")
    data = "As the clock struck 8 pm on November 8, 2016, India came to a standstill and Prime Minister Narendra Modi announced one of the most ground breaking changes in the Indian economyThe Indian Prime Minister announced his plans of banning Rs 500 and Rs 1000 notes with several motives in mind and thus began India’s struggle with demonetization. A year after the country was wiped out of old currency, the effects of Narendra Modi’sdemonetization can still be felt in the economy. Demonetization has be .."
    fp.write(data)
    fp.close()
    print("Inserted Successfully into File")

def read_from_file():
    fp = open("Demonetization.txt" , "r")
    st = fp.read()
    print(st)
    fp.close()


while True:
    ch = int(input("Enter Choice :\n1.Write Into File\n2.Read From File\n3.Exit\n"))
    if ch == 1:
        write_into_file()
    elif ch == 2:
        read_from_file()
    else:
        print("You have chosen to exit the operation. Thanks.")
        exit(0)