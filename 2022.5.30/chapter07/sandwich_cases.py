print("Note: All pastrami is sold out today!\n")

sandwich_orders = ["panini sandwich", "pastrami", "egg and cress sandwich",
                   "fry sandwich", "pastrami", "bacon sandwich", "pastrami"]
finished_sandwiches = []

# 删除 'pastrami' 元素
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# 制作三明治
while sandwich_orders:
    sandwich = sandwich_orders.pop()

    finished_sandwiches.append(sandwich)
    print("I made your " + sandwich + ".")

# 打印清单
print("\nHere are all the sandwiches I made for you:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)
