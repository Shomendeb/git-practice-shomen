import datetime
from utils import add, subtract

# Previous code from Task 3
print("Name: Shomen Deb")
print("Today's Date:", datetime.date.today())

# Calling the new calculator functions
result_add = add(5, 3)
result_sub = subtract(10, 4)
result_mult = multiply(4, 7)  
result_div_normal = divide(10, 2)     # Normal division
result_div_error = divide(10, 0)      # Testing the error handling

print(f"5 + 3 = {result_add}")
print(f"10 - 4 = {result_sub}")
print(f"4 * 7 = {result_mult}")  
print(f"10 / 2 = {result_div_normal}")
print(f"10 / 0 = {result_div_error}")  # Will print the error message safely