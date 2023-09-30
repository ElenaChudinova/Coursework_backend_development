from utils import load_operations, find_operations_executed, datetime_operations, number_card_cod, number_check_cod
import os

operations_path = os.path.join("operations.json")
all_operations = load_operations(operations_path)

operations_executed = find_operations_executed(all_operations)
date_operations = datetime_operations(all_operations)
number_card_cod = number_card_cod(all_operations)
number_check_cod = number_check_cod(all_operations)

print(date_operations, operations_executed.get("description"))
print(number_card_cod, '->', number_check_cod)
print(operations_executed.get("amount"), operations_executed.get("name"))
print()





