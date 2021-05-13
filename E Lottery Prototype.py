from collections import defaultdict
from random import randint as rand
from random import choice as pick
import pyautogui
import time

# User Dictionaries

# For Checking Put = {0: ["a", 123456, 500.00]}
users_dict = {}  # users_dict = {1: [user name, password, money]}
# For Checking Put = {0: ["abby", "a", 9556736262, 19, True, 123456]}
values_dict = {}  # values_dict = {1: [full name, user name, number, age, legal, pin_num]}
admin_dict = {1: ["MJ", 101102], 2: ["Caro", 201202], 3: ["Thel", 301302]}  # Constant Values For Admin Login

# Lotto Winning, Entries, Winners Dictionaries
entries_dict = defaultdict(lambda: defaultdict(list))  # For Appending Entries To List Inside Dictionary
winning_dict = {}  # Winning Combinations Go Here
won_draw = {}  # All User IDs Who Won Goes Here

# Constant Values
user_id = 0
admin_id = 0
key_val = 0
client_attempts = 3
admin_attempts = 5


# ALGORITHMS
def generate_pin():  # Automatically generates a pin code for the newly registered players,
    length_pin = 6
    start_range = 10 ** (length_pin - 1)
    end_range = (10 ** length_pin) - 1
    pin_num = rand(start_range, end_range)
    return pin_num


def generate_num_pool(range_start, range_end):  # Generate the number of pool of choices in different lotto games
    return [x for x in range(range_start, range_end + 1)]


def jackpot_unique(range_start, range_end, num_comb):  # Generate winning numbers for without repetition
    num_pool = [x for x in range(range_start, range_end + 1)]
    return [num_pool.pop(rand(0, len(num_pool) - 1)) for i in range(num_comb)]


def jackpot_repeating(range_start, range_end, num_comb):  # Generate winning numbers for with repetition
    num_pool = [x for x in range(range_start, range_end + 1)]
    return [rand(0, len(num_pool) - 1) for i in range(num_comb)]


def jackpot_raffle(entries_dict, game_type):  # Picks the winner on a raffle basis
    random_key = pick(list(entries_dict.keys()))
    if game_type == "grand":
        random_list = pick(entries_dict[random_key]["grand"])
    elif game_type == "mega":
        random_list = pick(entries_dict[random_key]["mega"])
    elif game_type == "four":
        random_list = pick(entries_dict[random_key]["four"])
    elif game_type == "three":
        random_list = pick(entries_dict[random_key]["three"])
    elif game_type == "two":
        random_list = pick(entries_dict[random_key]["two"])

    return random_list


# Creates A New Dictionary With Prize As The KEY and Winners As The VALUE List
def verify_grand(grand_jackpot):
    grand_winner_exact = []
    grand_exact_count = 0
    grand_winner_shuffled = []
    grand_shuffled_count = 0
    for k1, v1 in entries_dict.items():
        for k2, v2 in v1.items():
            if k2 == "grand":
                for v3 in v2:
                    if grand_jackpot == v3:
                        prize_money = 30000000.00
                        grand_winner_exact.append(k1)
                        won_draw[prize_money] = grand_winner_exact
                        grand_exact_count += 1
                    elif all(i in grand_jackpot for i in v3):
                        prize_money = 200000.00
                        grand_winner_shuffled.append(k1)
                        won_draw[prize_money] = grand_winner_shuffled
                        grand_shuffled_count += 1
                    else:
                        continue
    return won_draw, grand_exact_count, grand_shuffled_count


def verify_mega(mega_jackpot):
    mega_winner_exact = []
    mega_exact_count = 0
    mega_winner_shuffled = []
    mega_shuffled_count = 0
    for k1, v1 in entries_dict.items():
        for k2, v2 in v1.items():
            if k2 == "mega":
                for v3 in v2:
                    if mega_jackpot == v3:
                        prize_money = 9000000.00
                        mega_winner_exact.append(k1)
                        won_draw[prize_money] = mega_winner_exact
                        mega_exact_count += 1
                    elif all(i in mega_jackpot for i in v3):
                        prize_money = 50000.00
                        mega_winner_shuffled.append(k1)
                        won_draw[prize_money] = mega_winner_shuffled
                        mega_shuffled_count += 1
                    else:
                        continue
    return won_draw, mega_exact_count, mega_shuffled_count


def verify_four(four_jackpot):
    four_winner_exact = []
    four_exact_count = 0
    four_winner_shuffled = []
    four_shuffled_count = 0
    for k1, v1 in entries_dict.items():
        for k2, v2 in v1.items():
            if k2 == "four":
                for v3 in v2:
                    if four_jackpot == v3:
                        prize_money = 10000.00
                        four_winner_exact.append(k1)
                        won_draw[prize_money] = four_winner_exact
                        four_exact_count += 1
                    elif all(i in four_jackpot for i in v3):
                        prize_money = 800.00
                        four_winner_shuffled.append(k1)
                        won_draw[prize_money] = four_winner_shuffled
                        four_shuffled_count += 1
                    else:
                        continue
    return won_draw, four_exact_count, four_shuffled_count


def verify_three(three_jackpot):
    three_winner_exact = []
    three_exact_count = 0
    three_winner_shuffled = []
    three_shuffled_count = 0
    for k1, v1 in entries_dict.items():
        for k2, v2 in v1.items():
            if k2 == "three":
                for v3 in v2:
                    if three_jackpot == v3:
                        prize_money = 5000.00
                        three_winner_exact.append(k1)
                        won_draw[prize_money] = three_winner_exact
                        three_exact_count += 1
                    elif all(i in three_jackpot for i in v3):
                        prize_money = 1500.00
                        three_winner_shuffled.append(k1)
                        won_draw[prize_money] = three_winner_shuffled
                        three_shuffled_count += 1
                    else:
                        continue
    return won_draw, three_exact_count, three_shuffled_count


def verify_two(two_jackpot):
    two_winner_exact = []
    two_exact_count = 0
    two_winner_shuffled = []
    two_shuffled_count = 0
    for k1, v1 in entries_dict.items():
        for k2, v2 in v1.items():
            if k2 == "two":
                for v3 in v2:
                    if two_jackpot == v3:
                        prize_money = 4000.00
                        two_winner_exact.append(k1)
                        won_draw[prize_money] = two_winner_exact
                        two_exact_count += 1
                    elif all(i in two_jackpot for i in v3):
                        prize_money = 2000.00
                        two_winner_shuffled.append(k1)
                        won_draw[prize_money] = two_winner_shuffled
                        two_shuffled_count += 1
                    else:
                        continue
    return won_draw, two_exact_count, two_shuffled_count
# Creates A New Dictionary With Prize As The KEY and Winners As The VALUE List


def give_prize(winners_dict, exact_winners, shuffled_winners, first_prize, conso_prize):  # Give the prize money direct from the user player account
    for user, money in users_dict.items():
        for prize, list_winners in winners_dict.items():
            if user in list_winners:
                if prize == first_prize:
                    if shuffled_winners > 0:
                        lotto_prize = prize - conso_prize
                    else:
                        lotto_prize = first_prize
                    money[2] = money[2] + lotto_prize / exact_winners
                elif prize == conso_prize:
                    lotto_prize = conso_prize
                    money[2] = money[2] + lotto_prize / shuffled_winners
# ALGORITHMS


# PRINT FUNCTIONS
def attempts_counter(attempts_num):  # Display How Many Attempts Are Left
    print()
    print("      Login Attempts Left:", attempts_num, "    ")


def mobile_body(part):  # UI Display of the program.
    def print_header():
        print("╔═══════════════════════════════╗")
        print("║12:00 NN       ●         ▄▄ 50%║")
        print("╠═══════════════════════════════╣")
        print("║                               ║")
        print("║                               ║")

    def print_footer():
        print("║                               ║")
        print("║                ®JHUNCHUMAEARLO║")
        print("╠═══════════════════════════════╣")
        print("║       ≡       ◯       ←       ║")
        print("╚═══════════════════════════════╝")

    def print_title():
        print("║ ║     ╔═══╗ ══╦══ ══╦══ ╔═══╗ ║")
        print("║ ║     ║   ║   ║     ║   ║   ║ ║")
        print("║ ║     ║   ║   ║     ║   ║   ║ ║")
        print("║ ║     ║   ║   ║     ║   ║   ║ ║")
        print("║ ╚════ ╚═══╝   ║     ║   ╚═══╝ ║")
        print("║                               ║")

    if part == "Header":
        print_header()
    elif part == "Footer":
        print_footer()
    elif part == "Title":
        print_title()


def error_messages(error_type):  # Print statements for the error validation of the program.
    def out_of_scope():
        print()
        print("ERROR 101: INPUT NUMBER IN CHOICE")  # Checked and Formatted
        print()

    def value_error():
        print()
        print(" ERROR 102: INPUT INTEGER/S ONLY")  # Checked and Formatted
        print()

    def text_only():
        print()
        print("ERROR 103: PLEASE ENTER TEXT ONLY")
        print()

    def length_req():
        print()
        print(" ERROR 104 : LENGTH REQ. NOT MET")
        print()

    def yes_no():
        print()
        print(" ERROR 105: ENTER YES / NO ONLY")  # Checked and Formatted
        print()

    def verify_password():
        print()
        print(" ERROR 106: PASSWORD SHOULD BE A")  # Checked and Formatted
        print("     6-DIGIT NUM COMBINATION")
        print()

    def login_error():
        print()
        print("ERROR 107: WRONG USER CREDENTIALS")  # Checked and Formatted
        print()

    def attempts_error():
        print()
        print("ERROR 108: NO MORE ATTEMPTS LEFT")  # Checked and Formatted
        print()

    def money_error():
        print()
        print("ERROR 109: INPUT FLOAT NUM/S ONLY")  # Checked and Formatted
        print()

    def null_dict():
        print()
        print("     ERROR 110: NULL ENTRIES")  # Checked and Formatted
        print("         TRY RANDOM DRAW")
        print()

    def insufficient_funds():
        print()
        print(" ERROR 111: Insufficient Fund/s")
        print()

    def signing_out_message():
        print()
        print("          Signing Out...        ")
        time.sleep(4)

    if error_type == "not_in_range":
        out_of_scope()
    elif error_type == "unmatched_type":
        value_error()
    elif error_type == "mixed_num":
        text_only()
    elif error_type == "len_short":
        length_req()
    elif error_type == "neither_yes_no":
        yes_no()
    elif error_type == "password_format":
        verify_password()
    elif error_type == "wrong_login":
        login_error()
    elif error_type == "no_more_attempts":
        attempts_error()
    elif error_type == "float_val":
        money_error()
    elif error_type == "empty_dict":
        null_dict()
    elif error_type == "no_funds":
        insufficient_funds()
    elif error_type == "end_session":
        signing_out_message()
# PRINT FUNCTIONS


# INPUT FUNCTIONS
def choose_numbers(is_repeating, game_type, user_id):  # Choose Corresponding Number Of Lucky Numbers
    flag_value = True
    flag_value_two = True

    def pick_number():
        return int(input("        Lucky Number # "))

    if is_repeating:
        while flag_value:
            try:
                start_num = 0
                end_num = 9
                if game_type == "four":
                    current_entry = []
                    print("      Pick 4 Lucky Number/s      ")
                    print("      (Number/s Can Repeat)      ")
                    print()
                    four_lotto_pool = generate_num_pool(start_num, end_num)
                    count = 0
                    while count != 4:
                        num_pick = pick_number()
                        if num_pick in four_lotto_pool:
                            current_entry.append(num_pick)
                            count += 1
                        else:
                            print("Choose Numbers 0-9 W/o Repeating")
                            continue
                    entries_dict[user_id][game_type].append(current_entry)
                elif game_type == "three":
                    current_entry = []
                    print("      Pick 3 Lucky Number/s      ")
                    print("      (Number/s Can Repeat)      ")
                    print()
                    three_lotto_pool = generate_num_pool(start_num, end_num)
                    count = 0
                    while count != 3:
                        num_pick = pick_number()
                        if num_pick in three_lotto_pool:
                            current_entry.append(num_pick)
                            count += 1
                        else:
                            print("Choose Numbers 0-9 W/o Repeating")
                            continue
                    entries_dict[user_id][game_type].append(current_entry)
                flag_value = False
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue
    else:
        while flag_value:
            try:
                if game_type == "grand":
                    current_entry = []
                    print("      Pick 6 Lucky Number/s      ")
                    print("    (Number/s Can Not Repeat)    ")
                    print()
                    start_num = 6
                    end_num = 55
                    grand_lotto_pool = generate_num_pool(start_num, end_num)
                    count = 0
                    while count != 6:
                        num_pick = pick_number()
                        if num_pick in grand_lotto_pool:
                            current_entry.append(num_pick)
                            grand_lotto_pool.remove(num_pick)
                            count += 1
                        else:
                            print("Choose Numbers 6-55 W/o Repeating")
                            continue
                    entries_dict[user_id][game_type].append(current_entry)
                    # print(entries_dict[user_id][game_type])
                elif game_type == "mega":
                    current_entry = []
                    print("      Pick 6 Lucky Number/s      ")
                    print("    (Number/s Can Not Repeat)    ")
                    print()
                    start_num = 6
                    end_num = 45
                    mega_lotto_pool = generate_num_pool(start_num, end_num)
                    count = 0
                    while count != 6:
                        num_pick = pick_number()
                        if num_pick in mega_lotto_pool:
                            current_entry.append(num_pick)
                            mega_lotto_pool.remove(num_pick)
                            count += 1
                        else:
                            print("Choose Numbers 6-45 W/o Repeating")
                            continue
                    entries_dict[user_id][game_type].append(current_entry)
                    # print(entries_dict[user_id][game_type])
                elif game_type == "two":
                    current_entry = []
                    print("      Pick 2 Lucky Number/s      ")
                    print("    (Number/s Can Not Repeat)    ")
                    print()
                    start_num = 1
                    end_num = 31
                    two_lotto_pool = generate_num_pool(start_num, end_num)
                    count = 0
                    while count != 2:
                        num_pick = pick_number()
                        if num_pick in two_lotto_pool:
                            current_entry.append(num_pick)
                            two_lotto_pool.remove(num_pick)
                            count += 1
                        else:
                            print("Choose Numbers 1-31 W/o Repeating")
                            continue
                    entries_dict[user_id][game_type].append(current_entry)
                    #print(entries_dict[user_id][game_type])
                #print("All entries", entries_dict[user_id])
                flag_value = False
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue

    while flag_value_two:
        print()
        ticket_buy = input("     Buy Again? (Yes / No): ")
        if ticket_buy.title() == "Yes":
            flag_value_two = False
            print("Processing...")
            hub_portals_third(1)
        elif ticket_buy.title() == "No":
            flag_value_two = False
            print()
            print("   Going Back To Main Page....   ")
            time.sleep(4)
            client_hub(user_id)
        else:
            error_value = "neither_yes_no"
            error_messages(error_value)
            continue


def cash_in():  # Cash In Money Function
    money_to_load = 0
    flag_value = True
    print("           ENTER AMOUNT          ")
    print()
    print("Initial Money = ", users_dict[user_id][2])
    print()
    while flag_value:
        try:
            money_to_load = float(input("      Cash In PHP: "))
            if 500.00 <= money_to_load <= 50000.00:
                users_dict[user_id][2] = users_dict[user_id][2] + money_to_load
                flag_value = False
            elif money_to_load == 1:
                client_hub(user_id)
            else:
                error_value = "not_in_range"
                error_messages(error_value)
                continue
        except ValueError:
            error_value = "float_val"
            error_messages(error_value)
            continue
    print()
    print("Updated Money =", users_dict[user_id][2])
    print()
    print("    Money Successfully Loaded    ")
    print("   Going Back To Main Page....   ")
    time.sleep(4)
    return money_to_load


def login_input(location_val):  # Login Function For Client / Admin
    flag_value = True
    verified_admin_pass = False
    verified_user_pass = False
    global client_attempts
    global admin_attempts

    def login_as_client():
        flag_password = True
        client_pass = 000000
        client_username = input("Guest Username: ")
        while flag_password:
            try:
                client_pass = int(input("Guest Password: "))
                if len(str(client_pass)) != 6:
                    login_error = "password_format"
                    error_messages(login_error)
                    continue
                flag_password = False
            except ValueError:
                login_error = "password_format"
                error_messages(login_error)
                continue

        return client_username, client_pass

    def login_as_admin():
        flag_password = True
        admin_password = 000000
        admin_username = input("Admin Username: ")
        while flag_password:
            try:
                admin_password = int(input("Admin Password: "))
                if len(str(admin_password)) != 6:
                    login_error = "password_format"
                    error_messages(login_error)
                    continue
                flag_password = False
            except ValueError:
                login_error = "password_format"
                error_messages(login_error)
                continue

        return admin_username, admin_password

    if location_val == "Client":
        global user_id
        while flag_value:
            a, b = login_as_client()
            for x in users_dict.keys():
                if a and b in users_dict[x]:
                    verified_user_pass = True
                    user_id = x
            if verified_user_pass is not True:
                client_attempts -= 1
                attempts_counter(client_attempts)
                if client_attempts == 0:
                    error_value = "no_more_attempts"
                    error_messages(error_value)
                    print("Going To Login / Register Page...")
                    flag_value = False
                    time.sleep(4)
                    hub_portals_first(1)
                    break
                error_value = "wrong_login"
                error_messages(error_value)
            else:
                flag_value = False
                client_hub(user_id)

    elif location_val == "Admin":
        global admin_id
        while flag_value:
            c, d = login_as_admin()
            for y in admin_dict.keys():
                if c and d in admin_dict[y]:
                    verified_admin_pass = True
                    admin_id = y
            if verified_admin_pass is not True:
                admin_attempts -= 1
                attempts_counter(admin_attempts)
                if admin_attempts == 0:
                    error_value = "no_more_attempts"
                    error_messages(error_value)
                    print("Going To Login / Register Page...")
                    flag_value = False
                    time.sleep(4)
                    hub_portals_first(1)
                    break
                error_value = "wrong_login"
                error_messages(error_value)
            else:
                flag_value = False
                admin_hub()


def registration_input():  # Registration Function For Clients
    flag_name = True
    flag_number = True
    flag_age = True
    flag_username = True
    flag_pin_one = True
    flag_pin_two = True
    name = ""
    number = 0
    user_name = ""
    int_pin = 0
    age = 0
    print("\t\tRegister Detail/s")

    while flag_name:
        name = input("Full Name: ").title()
        if name.replace(" ", "").isalpha() is not True:
            error_value = "mixed_num"
            error_messages(error_value)
            continue
        else:
            flag_name = False

    while flag_username:
        user_name = input("User Name: ")
        if user_name in [k for x in users_dict.values() for k in x]:
            print()
            print("Try Again: Username Already Taken")
            print()
            continue
        else:
            flag_username = False

    while flag_number:
        try:
            number = int(input("Contact Number: (+63)").replace(" ", ""))
            if len(str(number)) == 10:
                flag_number = False
            else:
                error_value = "len_short"
                error_messages(error_value)
                continue
        except ValueError:
            error_value = "unmatched_type"
            error_messages(error_value)
            continue

    while flag_age:
        try:
            age = int(input("Age: "))
            flag_age = False
        except ValueError:
            error_value = "unmatched_type"
            error_messages(error_value)
            continue

    while flag_pin_one:
        pin_num = generate_pin()
        print("Suggested Pin:", pin_num)
        print()
        while flag_pin_two:
            decide_pin = input("Change pin? (Yes / No): ")
            if decide_pin.title() == "Yes":
                pin_num = input("Input 6 Digit Pin Number: ")
                if pin_num.isdigit() and len(pin_num) == 6:
                    flag_pin_two = False
                    flag_pin_one = False
                elif pin_num.isdigit() is not True:
                    error_value = "unmatched_type"
                    error_messages(error_value)
                    continue
                elif len(pin_num) != 6:
                    error_value = "len_short"
                    error_messages(error_value)
                    continue
            elif decide_pin.title() == "No":
                flag_pin_two = False
                flag_pin_one = False
            else:
                error_value = "neither_yes_no"
                error_messages(error_value)
                continue
        int_pin = int(pin_num)
    global key_val
    if age >= 18:
        age_legality = True
        print()
        print("     Successfully Registered")
        key_val += 1
    else:
        age_legality = False
        print()
        print("   Invalid Session : Minor Age")
    print()
    return name, number, age, age_legality, user_name, int_pin, key_val


def call_input(input_choices, location_val):  # Calls Respective Input Depending On The Number Of Choices
    flag_value = True

    def one_input():
        return int(input("\t\t    Input (1): "))

    def three_inputs():
        return int(input("\t\t Input (1/2/3): "))

    def four_inputs():
        return int(input("\t\tInput (1/2/3/4): "))

    def five_inputs():
        return int(input("\t   Input (1/2/3/4/5): "))

    def six_inputs():
        return int(input("\t Input (1/2/3/4/5/6): "))

    while flag_value:
        try:
            if input_choices == 1:
                input_val = one_input()
                if input_val == 1:
                    if location_val == "members_developers":
                        main_home()
                        flag_value = False
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            elif input_choices == 3:
                input_val = three_inputs()
                if 1 <= input_val <= 3:
                    if location_val == "main_home":
                        hub_portals_first(input_val)
                        flag_value = False
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            elif input_choices == 4:
                input_val = four_inputs()
                if 1 <= input_val <= 4:
                    if location_val == "login_register":
                        hub_portals_second(input_val)
                        flag_value = False
                    if location_val == "client_page":
                        hub_portals_third(input_val)
                        flag_value = False
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            elif input_choices == 5:
                input_val = five_inputs()
                if 1 <= input_val <= 5:
                    if location_val == "admin_page":
                        hub_portals_five(input_val)
                        flag_value = False
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            elif input_choices == 6:
                input_val = six_inputs()
                if 1 <= input_val <= 6:
                    if location_val == "ticket_hub":
                        hub_portals_four(input_val, user_id)
                        flag_value = False
                    if location_val == "category_generate":
                        hub_portals_six(input_val)
                        flag_value = False
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            else:
                error_value = "not_in_range"
                error_messages(error_value)
                continue
        except ValueError:
            error_value = "unmatched_type"
            error_messages(error_value)
            continue
# INPUT FUNCTIONS


# PROGRAM BODY
def main_home():
    pyautogui.hotkey('ctrl', 'l')
    input_choices = 3
    location_val = "main_home"
    mobile_body("Header")
    mobile_body("Title")
    print("║      E-LOTTERY PROTOTYPE      ║")
    print("║ CASE STUDY PROJECT OF ICT 101 ║")
    print("║                               ║")
    print("║      [1 - ACCESS PROGRAM]     ║")
    print("║   [2 - MEET THE DEVELOPERS]   ║")
    print("║    [3 - CLOSE THE PROGRAM]    ║")
    mobile_body("Footer")
    call_input(input_choices, location_val)


def hub_portals_first(hub_num):
    def login_register():
        pyautogui.hotkey('ctrl', 'l')
        input_choices = 4
        location_val = "login_register"
        mobile_body("Header")
        mobile_body("Title")
        print("║        LOGIN / REGISTER       ║")
        print("║                               ║")
        print("║      [1 - LOGIN AS GUEST]     ║")
        print("║      [2 - LOGIN AS ADMIN]     ║")
        print("║        [3 - REGISTER ]        ║")
        print("║         [4 - GO BACK]         ║")
        mobile_body("Footer")
        call_input(input_choices, location_val)

    def members_developers():
        pyautogui.hotkey('ctrl', 'l')
        input_choices = 1
        location_val = "members_developers"
        mobile_body("Header")
        mobile_body("Title")
        print("║        GROUP2 MEMBERS:        ║")
        print("║   GALANG, CHARLES ALLDRYN M.  ║")
        print("║ PANGILINAN, JHUNIELLE LOUIE M.║")
        print("║    VICTORIA, JOSHUA ARLO D.   ║")
        print("║    FLORES, RAMIELLE MAE G.    ║")
        print("║         [1 - GO BACK]         ║")
        mobile_body("Footer")
        call_input(input_choices, location_val)

    def close_program():
        pyautogui.hotkey('ctrl', 'l')
        mobile_body("Header")
        mobile_body("Title")
        print("║      ELOTTERTY PROTOTYPE      ║")
        print("║ CASE STUDY PROJECT OF ICT 101 ║")
        print("║                               ║")
        print("║           GOOD DAY!           ║")
        print("║     THANK YOU FOR PLAYING!    ║")
        print("║          CLOSING....          ║")
        mobile_body("Footer")

    if hub_num == 1:
        login_register()
    elif hub_num == 2:
        members_developers()
    elif hub_num == 3:
        close_program()


def hub_portals_second(hub_num):
    def access_client():
        pyautogui.hotkey('ctrl', 'l')
        location_value = "Client"
        mobile_body("Header")
        mobile_body("Title")
        print("║          LOGIN GUEST          ║")
        print("║  INPUT THE FOLLOWING DETAILS  ║")
        print("║                               ║")
        print("║   Guest Username :            ║")
        print("║   Guest Password :            ║")
        print("║      Login Attempt/s = 3      ║")
        mobile_body("Footer")
        login_input(location_value)

    def access_admin():
        pyautogui.hotkey('ctrl', 'l')
        location_value = "Admin"
        mobile_body("Header")
        mobile_body("Title")
        print("║      LOGIN ADMINISTRATOR      ║")
        print("║  INPUT THE FOLLOWING DETAILS  ║")
        print("║                               ║")
        print("║   Admin Username :            ║")
        print("║   Admin Password :            ║")
        print("║      Login Attempt/s = 3      ║")
        mobile_body("Attempts")
        mobile_body("Footer")
        login_input(location_value)

    def registration_page():
        pyautogui.hotkey('ctrl', 'l')
        current_user = []
        value_check = []
        initial_balance = 0
        mobile_body("Header")
        mobile_body("Title")
        print("║        LOGIN / REGISTER       ║")
        print("║  INPUT THE FOLLOWING DETAILS  ║")
        print("║                               ║")
        print("║   Full Name:    Password:     ║")
        print("║   User Name:    Contact #:    ║")
        print("║   Age:                        ║")
        mobile_body("Footer")
        name, number, age, age_legality, user_name, pin_num, key_num = registration_input()
        if age_legality:

            # Appends All Details For Checking
            value_check.append(name)
            value_check.append(user_name)
            value_check.append(number)
            value_check.append(age)
            value_check.append(age_legality)
            value_check.append(pin_num)

            # Appends Required Details For Login
            current_user.append(user_name)
            current_user.append(pin_num)
            current_user.append(initial_balance)
            users_dict[key_num] = current_user
            values_dict[key_num] = value_check
        else:
            print("    You are still a underage!")
            print("    Credentials are not saved")
            print()
        print("Going To Login / Register Page...")
        time.sleep(4)  # 4 Seconds
        hub_portals_first(1)

    def go_back():
        main_home()

    if hub_num == 1:
        access_client()
    elif hub_num == 2:
        access_admin()
    elif hub_num == 3:
        registration_page()
    elif hub_num == 4:
        go_back()


def client_hub(user_id):
    pyautogui.hotkey('ctrl', 'l')
    input_choices = 4
    location_val = "client_page"
    mobile_body("Header")
    mobile_body("Title")
    print("║           PLAY LOTTO          ║")
    print("║                               ║")
    print("║       [1 - Buy A Ticket]      ║")
    print("║  [2 - Check Winning Numbers]  ║")
    print("║      [3 - Load E - Money]     ║")
    print("║         [4 - Sign Out]        ║")
    mobile_body("Footer")
    print("Hello User ID #", user_id)
    print("Credit Balance:", users_dict[user_id][2])
    print()
    call_input(input_choices, location_val)


def hub_portals_third(hub_num):
    def buy_ticket():
        pyautogui.hotkey('ctrl', 'l')
        input_choices = 6
        location_val = "ticket_hub"
        mobile_body("Header")
        mobile_body("Title")
        print("║[1 - Grand Lotto    (6 / 55)  ]║")
        print("║[2 - Mega Lotto     (6 / 45)  ]║")
        print("║[3 - 4 Digit     (4 One Digit)]║")
        print("║[4 - Swertes     (3 One Digit)]║")
        print("║[5 - EZ2 Lotto   (2 Num Combi)]║")
        print("║         [6 - Go Back]         ║")
        mobile_body("Footer")
        call_input(input_choices, location_val)

    def load_money():
        pyautogui.hotkey('ctrl', 'l')
        mobile_body("Header")
        mobile_body("Title")
        print("║       ENTER AMOUNT IN PHP     ║")
        print("║                               ║")
        print("║        PHP:___________        ║")
        print("║     Minimum of PHP 500.00     ║")
        print("║    Maximum of PHP 50000.00    ║")
        print("║         [1 - GO BACK]         ║")
        mobile_body("Footer")
        cash_in()
        client_hub(user_id)

    def display_winning_num():
        flag_value = True
        pyautogui.hotkey('ctrl', 'l')
        print("Display Winning Number/s")
        print()
        print("Winning Number/s")
        for game_type, combinations in winning_dict.items():
            print(game_type, ":", combinations)
        print()
        while flag_value:
            try:
                exit_code = int(input("Input 0 To Exit: "))
                if exit_code != 0:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
                else:
                    flag_value = False
                    client_hub(user_id)
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue

    def sign_out():
        error_value = "end_session"
        error_messages(error_value)
        hub_portals_first(1)

    if hub_num == 1:
        buy_ticket()
    elif hub_num == 2:
        display_winning_num()
    elif hub_num == 3:
        load_money()
    elif hub_num == 4:
        sign_out()


def hub_portals_four(hub_num, user_id):
    def grand_lotto():
        pyautogui.hotkey('ctrl', 'l')
        mobile_body("Header")
        mobile_body("Title")
        repeating_val = False
        game_type = "grand"
        print("║      Grand Lotto  (6/55)      ║")
        print("║  6 7 8 9 10 11 12 13 14 15 16 ║")
        print("║ 17 18 19 20 21 22 23 24 25 26 ║")
        print("║ 27 28 29 30 31 32 33 34 35 36 ║")
        print("║ 37 38 39 40 41 42 43 44 45 46 ║")
        print("║   47 48 49 50 51 52 53 54 55  ║")
        mobile_body("Footer")
        # print("Hello User ID#", user_id)
        if users_dict[user_id][2] >= 20:
            print()
            print("Money Before:", users_dict[user_id][2])
            users_dict[user_id][2] = users_dict[user_id][2] - 20
            print("Money After:", users_dict[user_id][2])
            print()
            choose_numbers(repeating_val, game_type, user_id)

        else:
            error_type = "no_funds"
            error_messages(error_type)
            print("   Going Back To Client Hub...")
            time.sleep(4)
            client_hub(user_id)

    def mega_lotto():
        pyautogui.hotkey('ctrl', 'l')
        mobile_body("Header")
        mobile_body("Title")
        repeating_val = False
        game_type = "mega"
        print("║      Mega Lotto   (6/45)      ║")
        print("║  6 7 8 9 10 11 12 13 14 15 16 ║")
        print("║ 17 18 19 20 21 22 23 24 25 26 ║")
        print("║ 27 28 29 30 31 32 33 34 35 36 ║")
        print("║   37 38 39 40 41 42 43 44 45  ║")
        mobile_body("Footer")
        if users_dict[user_id][2] >= 24:
            print()
            print("Money Before:", users_dict[user_id][2])
            users_dict[user_id][2] = users_dict[user_id][2] - 24
            print("Money After:", users_dict[user_id][2])
            print()
            choose_numbers(repeating_val, game_type, user_id)
        else:
            error_type = "no_funds"
            error_messages(error_type)
            print("   Going Back To Client Hub...")
            time.sleep(4)
            client_hub(user_id)

    def four_digit():
        pyautogui.hotkey('ctrl', 'l')
        mobile_body("Header")
        mobile_body("Title")
        repeating_val = True
        game_type = "four"
        print("║    4 - Digit(Single-Digit)    ║")
        print("║      #Numbers Can Repeat      ║")
        print("║                               ║")
        print("║      1 2 3 4 5 6 7 8 9 0      ║")
        print("║                               ║")
        mobile_body("Footer")
        if users_dict[user_id][2] >= 10:
            print()
            print("Money Before:", users_dict[user_id][2])
            users_dict[user_id][2] = users_dict[user_id][2] - 10
            print("Money After:", users_dict[user_id][2])
            print()
            choose_numbers(repeating_val, game_type, user_id)
        else:
            error_type = "no_funds"
            error_messages(error_type)
            print("   Going Back To Client Hub...")
            time.sleep(4)
            client_hub(user_id)

    def three_digit():
        pyautogui.hotkey('ctrl', 'l')
        mobile_body("Header")
        mobile_body("Title")
        repeating_val = True
        game_type = "three"
        print("║    3 - Digit(Single-Digit)    ║")
        print("║      #Numbers Can Repeat      ║")
        print("║                               ║")
        print("║      1 2 3 4 5 6 7 8 9 0      ║")
        print("║                               ║")
        mobile_body("Footer")
        if users_dict[user_id][2] >= 12:
            print()
            print("Money Before:", users_dict[user_id][2])
            users_dict[user_id][2] = users_dict[user_id][2] - 12
            print("Money After:", users_dict[user_id][2])
            print()
            choose_numbers(repeating_val, game_type, user_id)
        else:
            error_type = "no_funds"
            error_messages(error_type)
            print("   Going Back To Client Hub...")
            time.sleep(4)
            client_hub(user_id)

    def two_digit():
        pyautogui.hotkey('ctrl', 'l')
        mobile_body("Header")
        mobile_body("Title")
        repeating_val = False
        game_type = "two"
        print("║       EZ2 Lotto  (1/31)       ║")
        print("║        1 2 3 4 5 6 7 8        ║")
        print("║     9 10 11 12 13 14 15 16    ║")
        print("║    17 18 19 20 21 22 23 24    ║")
        print("║     25 26 27 28 29 30 31      ║")
        mobile_body("Footer")
        if users_dict[user_id][2] >= 10:
            print()
            print("Money Before:", users_dict[user_id][2])
            users_dict[user_id][2] = users_dict[user_id][2] - 10
            print("Money After:", users_dict[user_id][2])
            print()
            choose_numbers(repeating_val, game_type, user_id)
        else:
            error_type = "no_funds"
            error_messages(error_type)
            print("   Going Back To Client Hub...")
            time.sleep(4)
            client_hub(user_id)

    def go_back():
        client_hub(user_id)

    if hub_num == 1:
        grand_lotto()
    elif hub_num == 2:
        mega_lotto()
    elif hub_num == 3:
        four_digit()
    elif hub_num == 4:
        three_digit()
    elif hub_num == 5:
        two_digit()
    elif hub_num == 6:
        go_back()


def admin_hub():
    pyautogui.hotkey('ctrl', 'l')
    input_choices = 5
    location_val = "admin_page"
    mobile_body("Header")
    mobile_body("Title")
    print("║ (Admin Controls For Checking) ║")
    print("║ [1 - Generate Winning Number] ║")
    print("║  [2 - User / Admin Database]  ║")
    print("║ [3 - Lotto Number/s Database] ║")
    print("║   [4 - Clear Lotto Database]  ║")
    print("║         [5 - Sign Out]        ║")
    mobile_body("Footer")
    call_input(input_choices, location_val)


def hub_portals_five(hub_num):
    def choose_category():
        pyautogui.hotkey('ctrl', 'l')
        input_choices = 6
        location_val = "category_generate"
        mobile_body("Header")
        mobile_body("Title")
        print("║[1 - Grand Lotto    (6 / 55)  ]║")
        print("║[2 - Mega Lotto     (6 / 45)  ]║")
        print("║[3 - 4 Digit     (4 One Digit)]║")
        print("║[4 - Swertes     (3 One Digit)]║")
        print("║[5 - EZ2 Lotto   (2 Num Combi)]║")
        print("║         [6 - Go Back]         ║")
        mobile_body("Footer")
        call_input(input_choices, location_val)

    def display_people_database():
        flag_value = True
        pyautogui.hotkey('ctrl', 'l')
        print("Displaying database...")
        print()
        print("Players Full Details Database")
        print()
        for key, val in values_dict.items():
            print("User #", (key))
            print("Full Name:", val[0])
            print("User Name:", val[1])
            print("Contact Num: (+63)",val[2])
            print("Age:", val[3])
            print("Is Legal?:", val[4])
            print("Pass Code:", val[5])
            print()
        print("Players Login Details Database")
        print()
        for key, val in users_dict.items():
            print("User #", (key))
            print("User Name:", val[0])
            print("Pass Code:", val[1])
            print("Balance:", val[2])
            print()
        print("Administrators Database")
        print()
        for key, val in admin_dict.items():
            print("Admin #", key)
            print("Admin Name:", val[0])
            print("Admin Pass:", val[1])
            print("Admin Dictionary", admin_dict[key])
            print()
        while flag_value:
            try:
                exit_code = int(input("Input 0 To Exit: "))
                if exit_code != 0:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
                else:
                    flag_value = False
                    admin_hub()
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue

    def display_numbers_database():
        flag_value = True
        pyautogui.hotkey('ctrl', 'l')
        print("Display Winning Number/s / Entries / Winners")
        print()
        print("Winning Number/s")
        for game_type, combinations in winning_dict.items():
            print(game_type, combinations)
        print()
        print("All Entries")
        for user_id, game_info in entries_dict.items():
            print("User ID:", user_id)
            for key in game_info:
                print(key, ":", game_info[key])
        print()
        print("Winners Of Lotto")
        for prize, user_list in won_draw.items():
            print(prize, ":", user_list)
        print()
        while flag_value:
            try:
                exit_code = int(input("Input 0 To Exit: "))
                if exit_code != 0:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
                else:
                    flag_value = False
                    admin_hub()
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue

    def clear_database():
        global entries_dict
        global winning_dict
        global won_draw
        flag_value = True
        print()
        print("            WARNING")
        print("  !THIS WILL DELETE ALL ENTRIES!")
        print()
        print("       Delete All entries?")
        while flag_value:
            verification = input("     Delete All (Yes / No): ")
            if verification.title() == "Yes":
                flag_value = False
                print()
                print("          Processing...")
                time.sleep(4)
                entries_dict = defaultdict(lambda: defaultdict(list))
                winning_dict = {}
                won_draw = {}
                print()
                print("Lotto Winning Number/s / Entries")
                print("      Successfully Cleared!")
                time.sleep(4)
                admin_hub()
            elif verification.title() == "No":
                flag_value = False
                admin_hub()
            else:
                error_value = "neither_yes_no"
                error_messages(error_value)
                continue

    def sign_out():
        error_value = "end_session"
        error_messages(error_value)
        hub_portals_first(1)

    if hub_num == 1:
        choose_category()
    elif hub_num == 2:
        display_people_database()
    elif hub_num == 3:
        display_numbers_database()
    elif hub_num == 4:
        clear_database()
    elif hub_num == 5:
        sign_out()
# PROGRAM BODY


def hub_portals_six(hub_num):
    def grand_generate():
        game_type = "grand"
        flag_lotto = True
        combinations = 6
        start = 6
        end = 55
        grand_jackpot = []
        print()
        while flag_lotto:
            try:
                random_raffle = int(input("   (1 - Random / 2 - Raffle): "))
                print()
                if random_raffle == 1:
                    print("           Random Draw")
                    grand_jackpot = jackpot_unique(start, end, combinations)
                    flag_lotto = False
                elif random_raffle == 2:
                    print("           Raffle Draw")
                    if bool(entries_dict):
                        grand_jackpot = jackpot_raffle(entries_dict, game_type)
                        flag_lotto = False
                    else:
                        error_value = "empty_dict"
                        error_messages(error_value)
                        continue
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue
        print("Grand Lotto:", grand_jackpot)
        winning_dict["Grand Lotto"] = grand_jackpot
        grand_dict, uniq_grand, shuf_grand = verify_grand(grand_jackpot)
        if uniq_grand > 0:
            print("There is/are", uniq_grand, "winner/s of Grand Lotto - 30 Million")
        elif shuf_grand > 0:
            print("There is/are", shuf_grand, "winner/s of Grand Lotto - 200 Thousand")
        else:
            print("    0 winner/s of Grand Lotto")

        give_prize(grand_dict, uniq_grand, shuf_grand, 30000000.00, 200000.00)
        print()
        print("     Going Back Admin Hub...")
        time.sleep(4)
        admin_hub()

    def mega_generate():
        game_type = "mega"
        flag_lotto = True
        combinations = 5
        start = 6
        end = 45
        mega_jackpot = []
        print()
        while flag_lotto:
            try:
                random_raffle = int(input("   (1 - Random / 2 - Raffle): "))
                print()
                if random_raffle == 1:
                    print("           Random Draw")
                    mega_jackpot = jackpot_unique(start, end, combinations)
                    flag_lotto = False
                elif random_raffle == 2:
                    print("           Raffle Draw")
                    if bool(entries_dict):
                        mega_jackpot = jackpot_raffle(entries_dict, game_type)
                        flag_lotto = False
                    else:
                        error_value = "empty_dict"
                        error_messages(error_value)
                        continue
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue
        print("Mega Lotto:", mega_jackpot)
        winning_dict["Mega Lotto"] = mega_jackpot
        mega_dict, uniq_mega, shuf_mega = verify_mega(mega_jackpot)
        if uniq_mega > 0:
            print("There is/are", uniq_mega, "winner/s of Mega Lotto - 9 Million")
        elif shuf_mega > 0:
            print("There is/are", shuf_mega, "winner/s of Mega Lotto - 50 Thousand")
        else:
            print("    0 winner/s of Mega Lotto")
        give_prize(mega_dict, uniq_mega, shuf_mega, 9000000.00, 50000.00)
        print()
        print("     Going Back Admin Hub...")
        time.sleep(4)
        admin_hub()

    def four_generate():
        game_type = "four"
        flag_lotto = True
        combinations = 4
        start = 0
        end = 9
        four_jackpot = []
        print()
        while flag_lotto:
            try:
                random_raffle = int(input("   (1 - Random / 2 - Raffle): "))
                print()
                if random_raffle == 1:
                    print("           Random Draw")
                    four_jackpot = jackpot_repeating(start, end, combinations)
                    flag_lotto = False
                elif random_raffle == 2:
                    print("           Raffle Draw")
                    if bool(entries_dict):
                        four_jackpot = jackpot_raffle(entries_dict, game_type)
                        flag_lotto = False
                    else:
                        error_value = "empty_dict"
                        error_messages(error_value)
                        continue
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue
        print("4 Digit Lotto:", four_jackpot)
        winning_dict["4 Digit"] = four_jackpot
        four_dict, uniq_four, shuf_four = verify_four(four_jackpot)
        if uniq_four > 0:
            print("There is/are", uniq_four, "winner/s of 4 Digit Lotto - 10 Thousand")
        elif shuf_four > 0:
            print("There is/are", shuf_four, "winner/s of 4 Digit Lotto - 8 Hundred")
        else:
            print("   0 winner/s of 4 Digit Lotto")
        give_prize(four_dict, uniq_four, shuf_four, 10000.00, 800.00)
        print()
        print("     Going Back Admin Hub...")
        time.sleep(4)
        admin_hub()

    def three_generate():
        game_type = "three"
        flag_lotto = True
        combinations = 3
        start = 0
        end = 9
        three_jackpot = []
        print()
        while flag_lotto:
            try:
                random_raffle = int(input("   (1 - Random / 2 - Raffle): "))
                print()
                if random_raffle == 1:
                    print("           Raffle Draw")
                    three_jackpot = jackpot_repeating(start, end, combinations)
                    flag_lotto = False
                elif random_raffle == 2:
                    print("           Raffle Draw")
                    if bool(entries_dict):
                        three_jackpot = jackpot_raffle(entries_dict, game_type)
                        flag_lotto = False
                    else:
                        error_value = "empty_dict"
                        error_messages(error_value)
                        continue
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue
        print("Swertres Lotto:", three_jackpot)
        winning_dict["Swertres"] = three_jackpot
        three_dict, uniq_three, shuf_three = verify_three(three_jackpot)
        if uniq_three > 0:
            print("There is/are", uniq_three, "winner/s of Swertres Lotto - 4 Thousand")
        elif shuf_three > 0:
            print("There is/are", shuf_three, "winner/s of Swertres Lotto - 1.5 Thousand")
        else:
            print("   0 winner/s of Swertres Lotto")
        give_prize(three_dict, uniq_three, shuf_three, 5000.00, 1500.00)
        print()
        print("     Going Back Admin Hub...")
        time.sleep(4)
        admin_hub()

    def two_generate():
        game_type = "two"
        flag_lotto = True
        combinations = 2
        start = 1
        end = 31
        ez2_jackpot = []
        print()
        while flag_lotto:
            try:
                random_raffle = int(input("   (1 - Random / 2 - Raffle): "))
                print()
                if random_raffle == 1:
                    print("           Raffle Draw")
                    ez2_jackpot = jackpot_unique(start, end, combinations)
                    flag_lotto = False
                elif random_raffle == 2:
                    print("           Raffle Draw")
                    if bool(entries_dict):
                        ez2_jackpot = jackpot_raffle(entries_dict, game_type)
                        flag_lotto = False
                    else:
                        error_value = "empty_dict"
                        error_messages(error_value)
                        continue
                else:
                    error_value = "not_in_range"
                    error_messages(error_value)
                    continue
            except ValueError:
                error_value = "unmatched_type"
                error_messages(error_value)
                continue
        print("EZ2 Lotto:", ez2_jackpot)
        winning_dict["EZ2"] = ez2_jackpot
        two_dict, uniq_two, shuf_two = verify_two(ez2_jackpot)
        if uniq_two > 0:
            print("There is/are", uniq_two, "winner/s of EZ2 Lotto - 4 Thousand")
        elif shuf_two > 0:
            print("There is/are", shuf_two, "winner/s of EZ2 Lotto - 2 Thousand")
        else:
            print("     0 winner/s of EZ2 Lotto")
        give_prize(two_dict, uniq_two, shuf_two, 4000.00, 2000.00)
        print()
        print("     Going Back Admin Hub...")
        time.sleep(4)
        admin_hub()

    def go_back():
        admin_hub()

    if hub_num == 1:
        grand_generate()
    elif hub_num == 2:
        mega_generate()
    elif hub_num == 3:
        four_generate()
    elif hub_num == 4:
        three_generate()
    elif hub_num == 5:
        two_generate()
    elif hub_num == 6:
        go_back()


def main():
    main_home()


main()
