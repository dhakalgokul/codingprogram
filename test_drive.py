import unittest
import statistics
import problem_1_v2
import problem_2_v2


class TestQuestion1(unittest.TestCase):

    def test_positive_q1(self):
        data = [
                "1,10000,40",
                "1,10002,45",
                "1,11015,50",
                "2,10005,42",
                "2,11051,45",
                "2,12064,42",
                "2,13161,42",
            ]
        sensor_dataset = problem_1_v2.SensorDataset(data)

    def test_negative_q1(self):
        data = [
            "1,10000,-40",
            "1,10002,-45",
            "1,11015,-50",
            "2,10005,-42",
            "2,11051,-45",
            "2,12064,-42",
            "2,13161,-42",
        ]

    def test_arrangement_q2(self):
        s = problem_2_v2.SeatArrangement()
        s.seat_student()
        self.check_the_sides(s.seats)
        self.check_front_back(s.seats[0], s.seats[1])

    def check_left_right(self,seats):
        # check the sides
        for r in seats:
            for i,c in enumerate(r):
                if 0 < i < len(r):  # middle seat
                    self.assertEqual(c, c[i-1])  # check the left side
                    self.assertEqual(c, c[i+1])  # check the right side
                elif i == 0:  # first seat
                    self.assertEqual(c, c[1])  # check the right side only
                else:  # last seat
                    self.assertEqual(c, c[i-1])  # check the left side only

    def check_front_back(self, front, back):
        for i in range(len(front)):
            self.assertEqual(front[i], back[i])