def task_2_tuples():
    incidents = [
        ("INC-101", "DDoS", 4, ["192.168.1.50", "10.0.0.15"]),
        ("INC-102", "Brute Force", 3, ["172.16.0.5"]),
        ("INC-103", "Data Leak", 5, ["192.168.100.44", "192.168.100.45", "10.0.0.99"])
    ]

    print("Колекція кортежів-записів:")
    for inc in incidents:
        print(f"  {inc}")

    def unpack_incident(record):
        code, category, severity, ip_list = record
        return f"Інцидент {code} [{category}] має критичність {severity}/5. Залучено IP: {len(ip_list)} шт."

    print("\nРозпакування першого запису:")
    print(f"  {unpack_incident(incidents[0])}")

    def aggregate_incidents(records):
        total_severity = sum(rec[2] for rec in records)
        avg_severity = total_severity / len(records) if records else 0
        total_ips = sum(len(rec[3]) for rec in records)
        return avg_severity, total_ips

    avg_sev, total_ips = aggregate_incidents(incidents)
    print(f"\nАгреговані дані:")
    print(f"  Середня критичність: {avg_sev:.2f} / 5")
    print(f"  Загальна кількість IP: {total_ips}")

    print("\nПеревірка іммутабельності:")
    try:
        incidents[0][0] = "INC-999"
    except TypeError as e:
        print(f"  Помилка: {e}")

    print(f"  IP до мутації вкладеного списку: {incidents[0][3]}")
    incidents[0][3].append("203.0.113.195")
    print(f"  IP після мутації вкладеного списку: {incidents[0][3]}")

if __name__ == "__main__":
    task_2_tuples()
