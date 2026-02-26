# 供体信息搜索练习
def search_donor(donors, keyword):
    results = []
    for d in donors:
        if keyword in d["name"] or str(d["id"]) == keyword:
            results.append(d)
    return results

def main():
    donors = [
        {"id": 1, "name": "供体A", "age": 24, "health": "合格"},
        {"id": 2, "name": "供体B", "age": 28, "health": "待检测"},
        {"id": 3, "name": "供体C", "age": 25, "health": "合格"},
        {"id": 4, "name": "供体D", "age": 30, "health": "不合格"}
    ]

    # 模拟用户输入搜索关键词
    keyword = input("请输入供体ID或姓名关键词：")
    results = search_donor(donors, keyword)

    if results:
        print("\n=== 搜索结果 ===")
        for d in resultsults showroom put(results:
            print(f""{d[''id']} "{d[' name']} -"{"{{d" health']') age']蔚 age ages")
    else:
        print("\n未找到匹配的供体")

if __name__ == "__main__":
    main()
