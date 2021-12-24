from tkinter import *
import random
import datetime

root = Tk()
root.geometry("1500x700")
root.title("Grosary System version 1.6.8.9 ")
current_time = datetime.datetime.now()


def home():
    main_frame = Frame(root)
    main_frame.place(x=0, y=0)
    title_frame = Frame(main_frame)
    title_frame.grid(row=1, column=0)
    cust_frame = Frame(main_frame, bg="green", borderwidth=10, relief=GROOVE)
    cust_frame.grid(row=2, column=0, pady=5)

    app_title = Label(
        title_frame,
        text="Grosary Billing System",
        font="Algerian 20 bold ",
        bg="green",
        fg="white",
        borderwidth=10,
        relief=GROOVE,
        padx=543,
        pady=10,
    )
    app_title.pack()

    # customer entry part

    cust_title = Label(
        cust_frame,
        text="Customer Information :",
        font="Fira_Code 10 bold ",
        bg="green",
        fg="white",
        borderwidth=2,
        relief=GROOVE,
    )
    cust_title.grid(row=0, column=0)

    cust_name_lb = Label(
        cust_frame,
        text="Customer Name : ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
    )
    cust_name_lb.grid(row=2, column=0, pady=10)

    cust_name = StringVar()
    cust_name_entry = Entry(
        cust_frame, borderwidth=10, relief=GROOVE, textvariable=cust_name
    )
    cust_name_entry.grid(row=2, column=2, padx=30)

    cust_phone_lb = Label(
        cust_frame,
        text="Customer Phone Number  : ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
    )
    cust_phone_lb.grid(row=2, column=3)

    cust_phone = StringVar()
    cust_phone_entry = Entry(cust_frame, borderwidth=10, relief=GROOVE)
    cust_phone_entry.grid(row=2, column=4, padx=30)

    cust_bill_lb = Label(
        cust_frame,
        text="Bill ID   : ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
    )
    cust_bill_lb.grid(row=2, column=5)

    cust_bill = Text(cust_frame, height=1, width=10, borderwidth=10, relief=GROOVE)
    cust_bill.grid(row=2, column=6, padx=30)
    # createing the biill id
    nunbers = "123456789"
    passid = "".join(random.sample(nunbers, 4))
    cust_bill.insert(INSERT, passid)

    # All the information of the user and items
    # frames in use
    all_info_frame = Frame(
        main_frame, bg="green", borderwidth=10, relief=GROOVE, padx=5
    )
    all_info_frame.grid(row=3)

    # Food box

    food_frame = Frame(
        all_info_frame, bg="green", borderwidth=10, relief=GROOVE, pady=25, padx=10
    )
    food_frame.grid(row=1, column=0)

    food_title = Label(
        food_frame,
        text="Food",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        borderwidth=2,
        relief=GROOVE,
    )
    food_title.grid(row=0, column=0)

    Bread_want_lb = Label(
        food_frame, text="Bread : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    Bread_want_lb.grid(row=2, column=0, pady=10)

    Bread_want = StringVar()
    Bread_want_entry = Entry(
        food_frame, borderwidth=10, relief=GROOVE, textvariable=Bread_want
    )
    Bread_want_entry.grid(row=2, column=1, padx=30)

    Candy_want_lb = Label(
        food_frame, text="Candy  : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    Candy_want_lb.grid(row=3, column=0, pady=10)

    Candy_want = StringVar()
    Candy_want_entry = Entry(
        food_frame, borderwidth=10, relief=GROOVE, textvariable=Candy_want
    )
    Candy_want_entry.grid(row=3, column=1, padx=30)

    hot_dog_want_lb = Label(
        food_frame, text="Hot Dog : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    hot_dog_want_lb.grid(row=4, column=0, pady=10)

    hot_dog_want = StringVar()
    hot_dog_want_entry = Entry(
        food_frame, borderwidth=10, relief=GROOVE, textvariable=hot_dog_want
    )
    hot_dog_want_entry.grid(row=4, column=1, padx=30)

    burger_want_lb = Label(
        food_frame, text="Burger: ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    burger_want_lb.grid(row=5, column=0, pady=10)

    burger_want = StringVar()
    burger_want_entry = Entry(
        food_frame, borderwidth=10, relief=GROOVE, textvariable=burger_want
    )
    burger_want_entry.grid(row=5, column=1, padx=30)

    sand_wich_want_lb = Label(
        food_frame,
        text="Sandwich : ",
        font="Fira_Code 20 bold ",
        bg="green",
        fg="white",
    )
    sand_wich_want_lb.grid(row=6, column=0, pady=10)

    sand_wich_want = StringVar()
    sand_wich_want_entry = Entry(
        food_frame, borderwidth=10, relief=GROOVE, textvariable=sand_wich_want
    )
    sand_wich_want_entry.grid(row=6, column=1, padx=30)

    # grosary box
    grosary_frame = Frame(
        all_info_frame, bg="green", borderwidth=10, relief=GROOVE, pady=25, padx=10
    )
    grosary_frame.grid(row=1, column=1)

    food_title = Label(
        grosary_frame,
        text="Grosary",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        borderwidth=2,
        relief=GROOVE,
    )
    food_title.grid(row=0, column=0)

    rice_want_lb = Label(
        grosary_frame, text="Rice : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    rice_want_lb.grid(row=2, column=0, pady=10)

    rice_want = StringVar()
    rice_want_entry = Entry(
        grosary_frame, borderwidth=10, relief=GROOVE, textvariable=rice_want
    )
    rice_want_entry.grid(row=2, column=1, padx=30)

    food_oil_want_lb = Label(
        grosary_frame,
        text="Food Oil  : ",
        font="Fira_Code 20 bold ",
        bg="green",
        fg="white",
    )
    food_oil_want_lb.grid(row=3, column=0, pady=10)

    food_oil_want = StringVar()
    food_oil_want_entry = Entry(
        grosary_frame, borderwidth=10, relief=GROOVE, textvariable=food_oil_want
    )
    food_oil_want_entry.grid(row=3, column=1, padx=30)

    salt_want_lb = Label(
        grosary_frame, text="Salt : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    salt_want_lb.grid(row=4, column=0, pady=10)

    salt_want = StringVar()
    salt_want_entry = Entry(
        grosary_frame, borderwidth=10, relief=GROOVE, textvariable=salt_want
    )
    salt_want_entry.grid(row=4, column=1, padx=30)

    wheat_want_lb = Label(
        grosary_frame,
        text="Wheat : ",
        font="Fira_Code 20 bold ",
        bg="green",
        fg="white",
    )
    wheat_want_lb.grid(row=5, column=0, pady=10)

    wheat_want = StringVar()
    wheat_want_entry = Entry(
        grosary_frame, borderwidth=10, relief=GROOVE, textvariable=wheat_want
    )
    wheat_want_entry.grid(row=5, column=1, padx=30)

    suger_want_lb = Label(
        grosary_frame,
        text="Suger : ",
        font="Fira_Code 20 bold ",
        bg="green",
        fg="white",
    )
    suger_want_lb.grid(row=6, column=0, pady=10)

    suger_want = StringVar()
    suger_want_entry = Entry(
        grosary_frame, borderwidth=10, relief=GROOVE, textvariable=suger_want
    )
    suger_want_entry.grid(row=6, column=1, padx=30)

    # Other box
    other_frame = Frame(
        all_info_frame, bg="green", borderwidth=10, relief=GROOVE, pady=25, padx=10
    )
    other_frame.grid(row=1, column=2)

    food_title = Label(
        other_frame,
        text="Other",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        borderwidth=2,
        relief=GROOVE,
    )
    food_title.grid(row=0, column=0)
    # coke_want
    coke_want_lb = Label(
        other_frame, text="Coke : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    coke_want_lb.grid(row=1, column=0, pady=10)

    coke_want = StringVar()
    coke_want_entry = Entry(
        other_frame, borderwidth=10, relief=GROOVE, textvariable=coke_want
    )
    coke_want_entry.grid(row=1, column=1, padx=30)

    # biscuit_want
    biscuit_want_lb = Label(
        other_frame,
        text="Biscuit : ",
        font="Fira_Code 20 bold ",
        bg="green",
        fg="white",
    )
    biscuit_want_lb.grid(row=3, column=0, pady=10)

    biscuit_want = StringVar()
    biscuit_want_entry = Entry(
        other_frame, borderwidth=10, relief=GROOVE, textvariable=biscuit_want
    )
    biscuit_want_entry.grid(row=3, column=1, padx=30)

    # waffer_want
    waffer_want_lb = Label(
        other_frame, text="Waffer : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    waffer_want_lb.grid(row=4, column=0, pady=10)

    waffer_want = StringVar()
    waffer_want_entry = Entry(
        other_frame, borderwidth=10, relief=GROOVE, textvariable=waffer_want
    )
    waffer_want_entry.grid(row=4, column=1, padx=30)

    # juice_want
    juice_want_lb = Label(
        other_frame, text="Juice : ", font="Fira_Code 20 bold ", bg="green", fg="white"
    )
    juice_want_lb.grid(row=5, column=0, pady=10)

    juice_want = StringVar()
    juice_want_entry = Entry(
        other_frame, borderwidth=10, relief=GROOVE, textvariable=juice_want
    )
    juice_want_entry.grid(row=5, column=1, padx=30)

    # tea_powder_want
    tea_powder_want_lb = Label(
        other_frame,
        text="Tea Powder : ",
        font="Fira_Code 20 bold ",
        bg="green",
        fg="white",
    )
    tea_powder_want_lb.grid(row=6, column=0, pady=10)

    tea_powder_want = StringVar()
    tea_powder_want_entry = Entry(
        other_frame, borderwidth=10, relief=GROOVE, textvariable=tea_powder_want
    )
    tea_powder_want_entry.grid(row=6, column=1, padx=30)

    # bill area
    # bll memu
    bill_menu_frame = Frame(
        main_frame, bg="green", borderwidth=10, relief=GROOVE, padx=5
    )
    bill_menu_frame.grid(row=4)

    # billl area frame
    bill_area_frame = Frame(
        all_info_frame,
        bg="green",
        borderwidth=10,
        relief=GROOVE,
    )
    bill_area_frame.grid(row=1, column=3, pady=18)

    text_box = Text(bill_area_frame, height=0, width=8)
    text_box.pack(ipadx=100, ipady=200)

    def bill_func():
        text = f"              BILL\n=================================\n {current_time}\n=================================\n Customer Name : {cust_name.get()}\n Bill ID : {passid}\n=================================\nItem             Net  price \n=================================\n"
        text_box.insert(INSERT, text)

        if int(Bread_want.get()) > 0:
            text_box.insert(INSERT, "Bread")
            text_box.insert(
                INSERT,
                f"             {int(Bread_want.get())}    {int(Bread_want.get()) * 20}",
            )
        else:
            pass

        if int(Candy_want.get()) > 0:
            text_box.insert(INSERT, "\nCandy")
            text_box.insert(
                INSERT,
                f"             {int(Candy_want.get())}    {int(Candy_want.get()) * 5}",
            )
        else:
            pass
        if int(hot_dog_want.get()) > 0:
            text_box.insert(INSERT, "\nHot Dog")
            text_box.insert(
                INSERT,
                f"           {int(hot_dog_want.get())}    {int(hot_dog_want.get()) * 20}",
            )
        else:
            pass
        if int(burger_want.get()) > 0:
            text_box.insert(INSERT, "\nBurger")
            text_box.insert(
                INSERT,
                f"            {int(burger_want.get())}    {int(burger_want.get()) * 40}",
            )

        else:
            pass
        if int(sand_wich_want.get()) > 0:
            text_box.insert(INSERT, "\nSandwich")
            text_box.insert(
                INSERT,
                f"          {int(sand_wich_want.get())}    {int(sand_wich_want.get()) * 15}",
            )
        else:
            pass
        if int(rice_want.get()) > 0:
            text_box.insert(INSERT, "\nRice")
            text_box.insert(
                INSERT,
                f"              {int(rice_want.get())}    {int(rice_want.get()) * 250}",
            )
        else:
            pass
        if int(food_oil_want.get()) > 0:
            text_box.insert(INSERT, "\nFood Oil")
            text_box.insert(
                INSERT,
                f"          {int(sand_wich_want.get())}    {int(food_oil_want.get()) * 25}",
            )
        else:
            pass
        if int(salt_want.get()) > 0:
            text_box.insert(INSERT, "\nSalt want")
            text_box.insert(
                INSERT,
                f"         {int(salt_want.get())}    {int(salt_want.get()) * 35}",
            )
        else:
            pass
        if int(wheat_want.get()) > 0:
            text_box.insert(INSERT, "\nWheat")
            text_box.insert(
                INSERT,
                f"             {int(wheat_want.get())}    {int(wheat_want.get()) * 350}",
            )
        else:
            pass
        if int(suger_want.get()) > 0:
            text_box.insert(INSERT, "\nSuger")
            text_box.insert(
                INSERT,
                f"             {int(suger_want.get())}    {int(suger_want.get()) * 50}",
            )
        else:
            pass
        if int(coke_want.get()) > 0:
            text_box.insert(INSERT, "\nCoke")
            text_box.insert(
                INSERT,
                f"              {int(coke_want.get())}    {int(coke_want.get()) * 25}",
            )
        else:
            pass
        if int(biscuit_want.get()) > 0:
            text_box.insert(INSERT, "\nBiscuit")
            text_box.insert(
                INSERT,
                f"           {int(biscuit_want.get())}    {int(biscuit_want.get()) * 15}",
            )
        else:
            pass
        if int(waffer_want.get()) > 0:
            text_box.insert(INSERT, "\nWaffer")
            text_box.insert(
                INSERT,
                f"            {int(waffer_want.get())}    {int(waffer_want.get()) * 15}",
            )
        else:
            pass
        if int(juice_want.get()) > 0:
            text_box.insert(INSERT, "\nJuice")
            text_box.insert(
                INSERT,
                f"             {int(juice_want.get())}    {int(juice_want.get()) * 20}",
            )
        else:
            pass

        # priceses of the item
        bread_price = int(Bread_want.get()) * 20
        Candy_price = int(Candy_want.get()) * 5
        hot_dog_price = int(hot_dog_want.get()) * 20
        burger_price = int(burger_want.get()) * 40
        sand_wich_price = int(sand_wich_want.get()) * 15
        rice_want_price = int(rice_want.get()) * 250
        food_oil_price = int(food_oil_want.get()) * 25
        salt_price = int(salt_want.get()) * 35
        wheat_price = int(wheat_want.get()) * 350
        suger_price = int(suger_want.get()) * 50
        coke_price = int(coke_want.get()) * 25
        biscuit_price = int(biscuit_want.get()) * 15
        waffer_price = int(waffer_want.get()) * 15
        juice_price = int(juice_want.get()) * 20
        tea_powder_price = int(tea_powder_want.get()) * 10

        total = (
            bread_price
            + Candy_price
            + hot_dog_price
            + burger_price
            + rice_want_price
            + food_oil_price
            + salt_price
            + wheat_price
            + suger_price
            + coke_price
            + biscuit_price
            + waffer_price
            + juice_price
            + tea_powder_price
        )
        total_food = (
            int(Candy_want.get())
            + int(Bread_want.get())
            + int(hot_dog_want.get())
            + int(burger_want.get())
            + int(sand_wich_want.get())
        )
        tf.insert(INSERT, total_food)

        total_grosary = (
            int(rice_want.get())
            + int(food_oil_want.get())
            + int(salt_want.get())
            + int(wheat_want.get())
            + int(suger_want.get())
        )
        tg.insert(INSERT, total_grosary)

        total_other = (
            int(coke_want.get())
            + int(biscuit_want.get())
            + int(waffer_want.get())
            + int(juice_want.get())
            + int(tea_powder_want.get())
        )
        to.insert(INSERT, total_other)

        total_items = total_food + total_grosary + total_other

        tax = total_items * 12

        if int(tea_powder_want.get()) > 0:
            text_box.insert(INSERT, "\nTea Powder")
            text_box.insert(
                INSERT,
                f"        {int(tea_powder_want.get())}    {int(tea_powder_want.get()) * 10}",
            )
        text_box.insert(INSERT, f"\n=================================\n")
        text_box.insert(INSERT, f"Total Tax         {total_items}    {tax}\n")
        text_box.insert(INSERT, f"Total             {total_items}    {total + tax}")

    tf_lb = Label(
        bill_menu_frame,
        text="Total Food :  ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        padx=30,
    )
    tf_lb.grid(row=1, column=1, pady=10)

    tf = Text(bill_menu_frame, height=1, width=10)
    tf.grid(row=1, column=2)

    tg_lb = Label(
        bill_menu_frame,
        text="Total Grosary :  ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        padx=30,
    )
    tg_lb.grid(row=2, column=1, pady=10)

    tg = Text(bill_menu_frame, height=1, width=10)
    tg.grid(row=2, column=2)

    to_lb = Label(
        bill_menu_frame,
        text="Total Other :  ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        padx=30,
    )
    to_lb.grid(row=1, column=3, pady=10)

    to = Text(bill_menu_frame, height=1, width=10)
    to.grid(row=1, column=4)

    tt_lb = Label(
        bill_menu_frame,
        text="Total Tax :  ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        padx=30,
    )
    tt_lb.grid(row=2, column=3, pady=10)

    tt = Text(bill_menu_frame, height=1, width=10)
    tt.grid(row=2, column=4)

    def total_func():
        total_food = (
            int(Candy_want.get())
            + int(Bread_want.get())
            + int(hot_dog_want.get())
            + int(burger_want.get())
            + int(sand_wich_want.get())
        )
        tf.insert(INSERT, total_food)

        total_grosary = (
            int(rice_want.get())
            + int(food_oil_want.get())
            + int(salt_want.get())
            + int(wheat_want.get())
            + int(suger_want.get())
        )
        tg.insert(INSERT, total_grosary)

        total_other = (
            int(coke_want.get())
            + int(biscuit_want.get())
            + int(waffer_want.get())
            + int(juice_want.get())
            + int(tea_powder_want.get())
        )
        to.insert(INSERT, total_other)

        total_items = total_food + total_grosary + total_other

        tax = total_items * 16
        tt.insert(INSERT, tax)

    submint_btn = Button(
        bill_menu_frame,
        text=" Ganrate BILL ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        borderwidth=10,
        relief=GROOVE,
        command=bill_func,
        padx=30,
    )
    submint_btn.grid(row=2, column=6, padx=30)

    clear_btn = Button(
        bill_menu_frame,
        text=" Clear ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        borderwidth=10,
        relief=GROOVE,
        command=home,
        padx=30,
    )
    clear_btn.grid(row=2, column=8, padx=30)

    total_btn = Button(
        bill_menu_frame,
        text="Total",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        borderwidth=10,
        relief=GROOVE,
        command=total_func,
        padx=30,
    )
    total_btn.grid(row=2, column=7, padx=30)

    exit_btn = Button(
        bill_menu_frame,
        text=" Exit ",
        font="Fira_Code 15 bold ",
        bg="green",
        fg="white",
        borderwidth=10,
        relief=GROOVE,
        command=root.destroy,
        padx=30,
    )
    exit_btn.grid(row=2, column=9, padx=30)


home()

root.mainloop()
