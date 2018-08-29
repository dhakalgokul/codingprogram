# Enter the number of students
student_number = int(input("Enter the number of students: "))

# split the students to remainder 0,1,2
maths_student = student_number // 3
physics_student = student_number // 3
chemicals_student = student_number // 3

# split the case to even number and odd number
first_row = list(range(student_number // 2)) if student_number % 2 == 0 else list(range((student_number // 2) + 1))
second_row = list(range(student_number // 2))
last_num_of_first_row = len(first_row)-1

# if you pick something, you need to pop the same number in the second row
# as well as the number on the sides

seats = []
while len(first_row) >= maths_student:
    print(first_row)
    print(second_row)

    n = int(input("Which seat do you like to seat the math student in the first row"))
    if(maths_student>len(first_row)+len(second_row)):
        print("N/A")
        break
    else:
        try:
            if n in first_row:
                if n != 0 and n != last_num_of_first_row:
                    first_row.remove(n)
                    second_row.remove(n)
                    try:
                        first_row.remove(n - 1)
                    except Exception as e:
                        print(e)
                    try:
                        first_row.remove(n + 1)
                    except Exception as e:
                        print(e)

                elif n == 0:
                    first_row.pop(0)
                    first_row.pop(0)
                    second_row.pop(0)
                elif n == last_num_of_first_row:
                    first_row.pop(-1)
                    first_row.pop(-1)
                    second_row.pop(-1)
                else:
                    raise Exception("out of index")
                seats.append(['f', n])
        except Exception as e:
            print(e)

        maths_student -= 1

while len(second_row) >= maths_student:
    print(first_row)
    print(second_row)

    n = int(input("Which seat do you like to seat the math student in the second row"))
    if(maths_student>len(first_row)+len(second_row)):
        print("N/A")
        break
    else:
        try:
            if n in second_row:
                if n != 0 and n != last_num_of_first_row:
                    second_row.remove(n)
                    try:
                        second_row.remove(n-1)
                    except Exception as e:
                        print(e)
                    try:
                        second_row.remove(n+1)
                    except Exception as e:
                        print(e)

                elif n == 0:
                    second_row.pop(0)
                elif n == last_num_of_first_row:
                    second_row.pop(-1)
                else:
                    raise Exception("out of index")
                seats.append(['s', n])
        except Exception as e:
            print(e)

print(seats)