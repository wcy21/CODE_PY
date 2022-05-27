places = ['Sydney', 'London', 'Beijing', 'Venice', 'Dubai']

print("原始序列：")
print(places)

print("排序后的序列：")
print(sorted(places))

print("原始序列：")
print(places)

print("反向排列后的序列：")
print(sorted(places, reverse=True))

print("原始序列：")
print(places)

print("逆序后的序列：")
places.reverse()
print(places)

print("再次逆序后的序列：")
places.reverse()
print(places)

print("排序后的序列：")
places.sort()
print(places)

print("反向排序后的序列：")
places.sort(reverse=True)
print(places)
