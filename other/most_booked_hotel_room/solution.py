from typing import List
from collections import defaultdict

def most_booked(bookings: List[str]) -> str:
    count = defaultdict(int)
    max_count = 0
    max_booked = []

    for booking in bookings:
        if booking[0] == '+':
            count[booking] += 1

            if count[booking] > max_count:
                max_booked = [booking]
                max_count = count[booking]
            elif count[booking] == max_count:
                max_booked.append(booking)
    
    max_booked.sort()

    return max_booked[0][1:]

if __name__ == '__main__':
    assert most_booked(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]) == "1A"