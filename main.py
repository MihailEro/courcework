
from utils import functions


def main():
    FILENAME = 'utils/operations.json'
    LAST_OPERATIONS = 5
    FILTERED_EMPTY_FROM = True

    data, info = functions.unpacking(FILENAME)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = functions.get_filter(data, FILTERED_EMPTY_FROM)
    data = functions.get_last(data, LAST_OPERATIONS)
    data = functions.get_formatted_data(data)
    for row in data:
        print(row)


if __name__ == "__main__":
    main()