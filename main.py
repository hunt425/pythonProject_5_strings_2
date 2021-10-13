# Hunter Tysdal
# Program_5
# CS101_Lab
# 10/11/2021


def character_value(student_id):
    # [0:5] = first 5 digits
    print(student_id[0:5])
    # convert string to list to use for loop
    lists = list(letters)
    # blank loop to append and later convert back to string
    blank = []
    print(lists)

    for i in lists:
        num_letters = ord(i) - 65
        num_letters = str(num_letters)
        blank.append(num_letters)
        continue
    print(blank)

    new_str = ''.join(blank)

    print(new_str)

    return new_str


def get_check_digit(student_id):
    one = ord(student_id[0]) - 65
    one = one * 1

    two = ord(student_id[1]) - 65
    two = two * 2

    three = ord(student_id[2]) - 65
    three = three * 3

    four = ord(student_id[3]) - 65
    four = four * 4

    five = ord(student_id[4]) - 65
    five = five * 5

    six = int(student_id[5])
    six = six * 6

    sev = int(student_id[6])
    sev = sev * 7

    eight = int(student_id[7])
    eight = eight * 8

    nein = int(student_id[8])
    nein = nein * 9

    ten = int(student_id[9])

    # all variables added together
    sume = (one + two + three + four + five + six + sev + eight + nein)
    # what the function is looking for
    avg = sume % 10

    return avg


def verify_check_digit(student_id):
    # List of Errors
    while student_id != 'q' or student_id != 'Q':

        # Length Error
        length = len(student_id)

        if length != 10:
            return 'The length of the number given must be 10'
            return -1

        # All Letters error
        for i in range(0, len(student_id)):
            if i < 5:
                if not (student_id[i].isalpha()):
                    return 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(i,
                                                                                                             student_id[
                                                                                                                 i])
                    return -1
            # All Digits Error
            if i >= 5:
                if not (student_id[i].isdigit()):
                    return 'The last 3 characters must be 0-9, the invalid character is at {} is {}'.format(i,
                                                                                                            student_id[
                                                                                                                i])
                    return -1

        # index 5 is not 1,2,3
        classes = student_id[5]
        if classes != '1' and classes != '2' and classes != '3':
            return 'The sixth character must be 1, 2, or 3'
            return -1

        # index 6 is not 1,2,3,4
        grade = student_id[6]
        if grade != '1' and grade != '2' and grade != '3' and grade != '4':
            return 'The seventh character must be 1, 2, 3, or 4'
            return -1

        # index 9 is not check digits
        if int(student_id[9]) != get_check_digit(student_id):
            return 'Check digit {} does not match calculated value {}'.format(student_id[9],
                                                                              get_check_digit(student_id))
            return -1
        else:
            return 'Library Card is a valid card'
            break

        # library card is valid


def get_school(student_id):
    if student_id[5] == '1':
        schools = 'School of Computing and ENgineering SCE'
        return schools
    elif student_id[5] == '2':
        schools = 'School of Law'
        return schools
    elif student_id[5] == '3':
        schools = 'College of Arts and Sciences'
        return schools


def get_grade(student_id):
    if student_id[6] == '1':
        level = 'Freshman'
        return level
    elif student_id[6] == '2':
        level = 'Sophomore'
        return level
    elif student_id[6] == '3':
        level = 'Junior'
        return level
    elif student_id[6] == '4':
        level = 'Senior'
        return level


# Outcome

play_again = ''
while play_again != 'q' and play_again != 'Q':
    student_id = input('Enter Library Card:\n')
    print(student_id)
    print(verify_check_digit(student_id))
    if verify_check_digit(student_id) == 'Library Card is a valid card':
        print('This card belongs to a student in {}'.format(get_school(student_id)))
        print('This card belongs to a {}'.format(get_grade(student_id)))
        play_again = input('Would you like to play again? Press q to quit\n')

else:
    print('Thank you, have a good day!')
