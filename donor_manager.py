# 粪便捐赠供体信息管理练习
def main():
    donors = [
        {"id": 1, "name": "供体A", "age": 24, "health": "合格"},
        {"id": 2, "name": "供体B", "age": 28, "health": "待检测"},
        {"id": 3, "name": "供体C", "age": 25, "health": "合格"}
    ]

    print("=== 供体列表 ===")
    for d in donors:
        print(f"ID:{d['id']} 姓名:{d['name']} 年龄:{d['age']} 状态:{d['health']}")

    qualified = [d for d in donors if d["health"] == "合格"]
    print(f"\n合格供体数量：{len(qualified)}")

if __name__ == "__main__":
    main()
