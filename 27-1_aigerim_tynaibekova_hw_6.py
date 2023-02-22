import re


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


def save_data(data, filename):
    with open(filename, 'w') as f:
        f.write(data)


def read_names():
    data = read_data('MOCK_DATA.txt')
    pattern = r'^([A-Za-z\-]+)\s+(\'?[A-Za-z|\-]+)'
    names = re.findall(pattern, data, re.MULTILINE)
    names_str = '\n'.join([' '.join(name) for name in names])
    save_data(names_str, 'names.txt')
    print(f'Saved {len(names)} names to names.txt')


def read_emails():
    data = read_data('MOCK_DATA.txt')
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, data, re.MULTILINE)
    emails_str = '\n'.join(emails)
    save_data(emails_str, 'emails.txt')
    print(f'Saved {len(emails)} emails to emails.txt')


def read_filenames():
    data = read_data('MOCK_DATA.txt')
    pattern = r'^.*?\s+(\w+\.\w+)'
    filenames = re.findall(pattern, data, re.MULTILINE)
    filenames_str = '\n'.join(filenames)
    save_data(filenames_str, 'filenames.txt')
    print(f'Saved {len(filenames)} filenames to filenames.txt')


def read_colors():
    data = read_data('MOCK_DATA.txt')
    pattern = r'^.*?\s+(\w+)$'
    colors = re.findall(pattern, data, re.MULTILINE)
    colors_str = '\n'.join(colors)
    save_data(colors_str, 'colors.txt')
    print(f'Saved {len(colors)} colors to colors.txt')


def main():
    while True:
        print('1 - Read names\n2 - Read emails\n3 - Read filenames\n4 - Read colors\n5 - Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            read_names()
        elif choice == '2':
            read_emails()
        elif choice == '3':
            read_filenames()
        elif choice == '4':
            read_colors()
        elif choice == '5':
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
