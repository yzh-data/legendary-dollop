# 供体健康状态统计练习
def main():
    donors = [
        {"id": 1, "name": "供体A", "age": 24, "health": "合格"},
        {"id": 2, "name": "供体B", "age": 28, "health": "待检测"},
        {"id": 3, "name": "供体C", "age": 25, "health": "合格"},
        {"id": 4, "name": "供体D", "age": 30, "health": "不合格"},
        {"id": 5, "name": "供体E", "age": 26, "health": "待检测"}
    ]

    # 统计各状态人数
    status_count = {}
    for d in donors:
        status = d["health"]
        if status not in status_count:
            status_count[status] = 0
        status_count[status] += 1

    print("=== 供体健康状态统计 ===")
    for status, count in status_count.items():
        print(f"{status}: {count}人")

    # 计算合格供体的平均年龄
    qualified_ages = [d["age"] for d in donors if d["health"] == "合格"]
    if qualified_ages:
        avg_age = sum(qualified_ages) / len(qualified_ages)
        print(f"\n合格供体平均年龄：{avg_age:.1f}岁")

if __name__ == "__main__":
    main()
