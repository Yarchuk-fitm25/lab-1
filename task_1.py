import time
import random


def task_1_lists():
    print("=" * 60)
    print("ЗАВДАННЯ 1: Списки (індексація, зрізи та мутації)")
    print("=" * 60)

    hosts = ["firewall-01", "router-core", "switch-access-1", "ids-sensor", "gateway-vpn", "dns-primary"]
    print(f"[Початковий список хостів]: {hosts} (довжина: {len(hosts)})")

    print(f"Перший елемент (індекс 0): {hosts[0]}")
    print(f"Останній елемент (від’ємний індекс -1): {hosts[-1]}")

    slice_middle = hosts[1:4]
    print(f"Зріз [1:4] (середні елементи): {slice_middle}")

    slice_step = hosts[0:6:2]
    print(f"Зріз [0:6:2] (з кроком 2): {slice_step}")

    slice_reversed = hosts[::-1]
    print(f"Зріз [::-1] (інвертований порядок): {slice_reversed}")

    hosts.append("proxy-edge")
    print(f"Після append('proxy-edge'): {hosts}")

    hosts.insert(2, "backup-router")
    print(f"Після insert(2, 'backup-router'): {hosts}")
    
    hosts.remove("ids-sensor")
    print(f"Після remove('ids-sensor'): {hosts}")

    hosts[0:2] = ["fw-primary-new", "fw-secondary-new"]
    print(f"Після заміни діапазону hosts[0:2]: {hosts}")
    print(f"Фінальна довжина списку: {len(hosts)}\n")
