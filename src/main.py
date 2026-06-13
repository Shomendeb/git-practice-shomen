import datetime
from utils import add, subtract

# Previous code from Task 3
print("Name: Shomen Deb")
print("Today's Date:", datetime.date.today())

# Calling the new calculator functions
result_add = add(5, 3)
result_sub = subtract(10, 4)
result_mult = multiply(4, 7)  # Added this line

print(f"5 + 3 = {result_add}")
print(f"10 - 4 = {result_sub}")
print(f"4 * 7 = {result_mult}")  # Added this line