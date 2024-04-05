def read_file(filename):
    with open(filename, 'r') as file:
        return set(file.read().splitlines())

def main():
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    same_lines = read_file(file1) & read_file(file2)
    different_lines = read_file(file1) ^ read_file(file2)

    with open('same.txt', 'w') as same_file:
        same_file.write('\n'.join(same_lines))

    with open('diff.txt', 'w') as diff_file:
        diff_file.write('\n'.join(different_lines))

if __name__ == "__main__":
    main()