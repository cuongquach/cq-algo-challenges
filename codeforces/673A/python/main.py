# ProblemLink: https://codeforces.com/problemset/problem/673/A

import sys

def main():
    # Get input from console
    first_line_input = sys.stdin.readline().strip()
    second_line_input = sys.stdin.readline().strip()
    second_line_input = list(map(int, second_line_input.split(" ")))

    # Convert to list data to process
    array_interest = second_line_input

    min_index = 0
    min_watch = 0
    
    for i in range(len(array_interest)):
        if (array_interest[i] - min_index) > 15:
            if i == 0:
                min_watch = 0 + 15
            else:
                min_watch = min_index + 15
            break
        else:
            if i == (len(array_interest) - 1):
                if (array_interest[i] + 15) >= 90:
                    min_watch = 90
                else:
                    min_watch = array_interest[i] + 15
            else:
                min_watch = array_interest[i]

        min_index = array_interest[i]

    print(min_watch)


if __name__ == "__main__":
    main()