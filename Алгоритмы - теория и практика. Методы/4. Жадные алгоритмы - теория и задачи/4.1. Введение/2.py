n_items, capacity = [int(x) for x in input().split()]
cost_and_volume = [list(map(int, input().split())) for _ in range(n_items)]
backpack = {"capacity": capacity, "cost": 0}

for item_cost, item_volume in sorted(cost_and_volume, key=lambda x: -(x[0] / x[1])):
    if item_volume <= backpack["capacity"]:
        backpack["capacity"] -= item_volume
        backpack["cost"] += item_cost
    else:
        item_piece_multiplier = backpack["capacity"] / item_volume
        item_piece_weight = item_volume * item_piece_multiplier
        item_piece_cost = item_cost * item_piece_multiplier
        backpack["capacity"] -= item_piece_weight
        backpack["cost"] += item_piece_cost
        break

print(f"{backpack['cost']:.3f}")
