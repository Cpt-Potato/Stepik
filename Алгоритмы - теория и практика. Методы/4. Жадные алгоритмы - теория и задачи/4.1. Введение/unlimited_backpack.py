n_items, capacity = [int(x) for x in input().split()]
cost_and_volume = [tuple(map(int, input().split())) for _ in range(n_items)]
cost_and_volume.sort(key=lambda x: -(x[0] / x[1]))
backpack = {"capacity": capacity, "cost": 0}

for item_cost, item_volume in cost_and_volume:
    if item_volume <= backpack["capacity"]:
        backpack["capacity"] -= item_volume
        backpack["cost"] += item_cost
    else:
        backpack["cost"] += item_cost * (backpack["capacity"] / item_volume)
        break

print(f"{backpack['cost']:.3f}")
