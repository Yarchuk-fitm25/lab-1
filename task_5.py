import time

def task_5_complexity():
    sizes = [1_000, 5_000, 10_000]
    print(f"{'Розмір (n)':<12} | {'Пошук у списку (с)':<20} | {'Пошук у множині (с)':<20}")
    print("-" * 58)

    for n in sizes:
        lst = list(range(n))
        st = set(lst)
        target = n - 1

        start_time = time.perf_counter()
        for _ in range(100):
            _ = target in lst
        list_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        for _ in range(100):
            _ = target in st
        set_time = time.perf_counter() - start_time

        print(f"{n:<12} | {list_time:<20.6f} | {set_time:<20.6f}")

if __name__ == "__main__":
    task_5_complexity()
