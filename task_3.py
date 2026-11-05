def task_3_dictionaries():
    log_text = """
    Failed login attempt from 192.168.1.50 using root.
    Failed login attempt from 10.0.0.15 using admin.
    Successful login from 192.168.1.10 using operator.
    Failed login attempt from 192.168.1.50 using root.
    Connection timeout from 172.16.0.5.
    Failed login attempt from 192.168.1.50 using admin.
    """

    words = []
    for line in log_text.strip().split('\n'):
        cleaned_line = line.replace('.', ' ').replace(',', ' ')
        for word in cleaned_line.split():
            words.append(word.lower())

    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    print(f"Усього токенів: {len(words)}, унікальних: {len(freq_dict)}")

    print("\nСортування за спаданням частоти:")
    sorted_by_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_by_freq[:6]:
        print(f"  '{word}': {count}")

    frequent_terms = {k: v for k, v in freq_dict.items() if v >= 2}
    print(f"\nDict comprehension (частота >= 2):\n  {frequent_terms}")

if __name__ == "__main__":
    task_3_dictionaries()
