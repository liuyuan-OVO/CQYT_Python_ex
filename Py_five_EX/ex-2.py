universities = {
    "大学A": {
        "province": "省份A",
        "type": "类型A"
    },
    "大学B": {
        "province": "省份B",
        "type": "类型B"
    },
    "大学C": {
        "province": "省份C",
        "type": "类型C"
    }
}

for university, info in universities.items():
    print(f"大学名称：{university}")
    print(f"所属省份：{info['province']}")
    print(f"类型：{info['type']}")
    print()