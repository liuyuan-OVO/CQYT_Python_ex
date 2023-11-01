dict_a = {"name": "小明", "id": 1}
dict_b = {"name": "小红", "id": 2}
dict_c = {"name": "小刚", "id": 3}

student = [dict_a, dict_b, dict_c]

for s in student:
    print(f"姓名：{s['name']}")
    print(f"学号：{s['id']}")
    print()