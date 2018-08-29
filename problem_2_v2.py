class SeatArrangement():
    student_number: int

    def __init__(self, student = None):
        if type(student) is not int or student is None or student%3 != 0:
            """Default Student number 12"""
            self.student_number = 12
        else:
            self.student_number = student

        self.maths_student = self.student_number // 3

        # split the case to even number and odd number
        self.first_row = list(range(self.student_number // 2)) if self.student_number % 2 == 0 else list(range((self.student_number // 2) + 1))
        self.second_row = list(range(self.student_number // 2))

        self.last_num_of_first_row = len(self.first_row) - 1

        # if you pick something, you need to pop the same number in the second row
        # as well as the number of the sides
        self.seats = []
        self.display = [list(self.first_row),list(self.second_row)]

    def seat_student(self):
        while len(self.first_row)+len(self.second_row) >= self.maths_student\
                and self.maths_student != 0 : # The number of math students should be bigger the the number of the left seats
            self.first_row_check()
            self.second_row_check()

    def first_row_check(self):
        while (len(self.first_row) > 0 and self.maths_student != 0):
            # self.dump()
            i = input("FIRST ROW / which seat do you want a student to sit : ")
            if i == 'n':
                break
            n = int(i)
            try:
                if 0 < n < self.last_num_of_first_row:
                    self.first_row.remove(n)
                    try:
                        self.first_row.remove(n-1)  # left seat
                    except ValueError:
                        pass
                    try:
                        self.first_row.remove(n+1)  # right seat
                    except ValueError:
                        pass
                    self.second_row.remove(n)

                elif n == 0:
                    # first item
                    self.first_row.pop(0)  # first item
                    self.second_row.pop(0)  # first item in the second row
                    try:
                        self.first_row.pop(0)  # second item
                    except IndexError:
                        pass
                elif n == self.last_num_of_first_row:
                    # last index
                    self.first_row.pop(-1)
                    self.second_row.pop(-1)
                    try:
                        self.first_row.pop(-1)
                    except IndexError:
                        pass
                else:
                    raise Exception("Index Error")
                self.seats.append(["f", n])
                self.maths_student -= 1
            except Exception as e:
                print(e)


    def second_row_check(self):
        while (len(self.second_row) > 0 and self.maths_student != 0):
            # self.dump()
            i = input("FIRST ROW / which seat do you want a student to sit : ")
            if i == 'n':
                break
            n = int(i)
            try:
                if 0 < n < self.last_num_of_first_row:
                    self.second_row.remove(n)
                    try:
                        self.second_row.remove(n-1)  # left seat
                    except ValueError:
                        pass
                    try:
                        self.second_row.remove(n+1)  # right seat
                    except ValueError:
                        pass
                elif n == 0:
                    self.second_row.pop(0)  # first item in the second row
                elif n == self.last_num_of_first_row:
                    # last index
                    self.second_row.pop(-1)
                else:
                    raise Exception("Index Error")

                self.seats.append(["s", n])
                self.maths_student -= 1
            except Exception as e:
                print(e)

    def dump(self):
        print(self.first_row)
        print(self.second_row)

    def result_dump(self):
        for s in self.seats:
            if s[0] == 'f':
                self.display[0][s[1]] = 'M'
            else:
                self.display[1][s[1]] = 'M'

        for s in self.display:
            print(s)


