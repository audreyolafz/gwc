from decimal import Decimal
import random
from datetime import datetime
current_time = datetime.now()
print(current_time)

random_list = []
random_list = [x for x in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)

cost_of_gum = Decimal('0.1')
cost_of_gumdrop = Decimal('0.35')
cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)
four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

menu = {"oatmeal": 3, "avocado toast": 6,
        "carrot juice": 5, "blueberry muffin": 2}

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["pantry"] = 22
print(sensors)

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

translations = {"English": "Sindarin", "mountain": "orod",
                "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)
