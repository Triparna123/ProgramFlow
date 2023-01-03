chosen_option = "-"
while chosen_option != "0":  # while True:
    if chosen_option not in "12345":
        print("Please choose a option from below : ")
        options = ["1. Learn Python",
                   "2. Learn Java",
                   "3. Go swimming",
                   "4. Have dinner",
                   "5. Go to bed",
                   "0. exit"]
        print(options)
    # if chosen_option == "0":
    #     break
    # elif chosen_option in "12345":
    else:
        print("You have choose {} ".format(chosen_option))

    # if chosen_option in "12345":
    #     print("You have choose {} ".format(chosen_option))
    # else:
    #     print("Please choose a option from below : ")
    #     options = ["1. Learn Python",
    #                "2. Learn Java",
    #                "3. Go swimming",
    #                "4. Have dinner",
    #                "5. Go to bed",
    #                "0. exit"]
    #     print(options)
    # chosen_option = input()
    chosen_option = input()
