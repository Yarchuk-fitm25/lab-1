def task_4_sets():
    subnet_a = ["host-01", "host-02", "host-03", "host-04", "host-02"]
    subnet_b = ["host-03", "host-04", "host-05", "host-06", "host-05"]

    set_a = set(subnet_a)
    set_b = set(subnet_b)

    print(f"Множина A: {sorted(set_a)}")
    print(f"Множина B: {sorted(set_b)}")

    intersection_set = set_a & set_b
    union_set = set_a | set_b
    symmetric_diff = set_a ^ set_b

    print(f"Перетин (A & B): {sorted(intersection_set)}")
    print(f"Об’єднання (A | B): {sorted(union_set)}")
    print(f"Симетрична різниця (A ^ B): {sorted(symmetric_diff)}")

    subset_test_1 = {"host-03", "host-04"}.issubset(set_a)
    subset_test_2 = set_a.issubset(set_b)

    print(f"Чи є {{'host-03', 'host-04'}} підмножиною A? {subset_test_1}")
    print(f"Чи є множина A підмножиною B? {subset_test_2}")

if __name__ == "__main__":
    task_4_sets()
