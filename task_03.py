import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)

    if len(parts) < 4:
        print(f'Invalid log line format in "{line}". Skipping line.')
        return {}
    
    date, time, level, message = parts
    log_data = {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }
    return log_data


def load_logs(file_path: str) -> list:
    logs = []

    try:

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                log_entry = parse_log_line(line)
                if log_entry:
                    logs.append(log_entry)

    except FileNotFoundError:
        print(f'Error: File "{file_path}" not found.')
        sys.exit(1)
    except Exception as e:
        print(f'Error reading file: {e}')
        sys.exit(1)
    
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = filter(lambda line: line['level'].lower() == level, logs)
    return list(filtered_logs)


def count_logs_by_level(logs: list) -> dict:
    level_list = [obj['level'] for obj in logs]
    level_counts = Counter(level_list)
    return level_counts


def display_log_counts(counts: dict):
    print('Log Level Statistics:')
    print('{:<10} {:<10}'.format('Level', 'Amount'))
    print('-' * 20)
    for level, count in counts.items():
        print('{:<10} {:<10}'.format(level, count))


def main():
    if len(sys.argv) < 2:
        print('Enter file path')
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    log_level = sys.argv[2].lower() if len(sys.argv) > 2 else None
    
    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f'\nLogs with level {log_level.upper()}:')
            for log in filtered_logs:
                print(f'{log['date']} {log['time']} - {log['message']}')
        else:
            print(f'No logs found with level {log_level.upper()}.')

if __name__ == '__main__':
    main()