# Ref: https://codeforces.com/problemset/problem/430/B
import sys
import time

##
# Idea:
# We will loop while to inject var_x into possible two contiguous number => destroy them
# Then loop while to find other contiguos to delete.
# :Remove set of 3 or more continous same color ball

# Functions
def try_destroy_possible(local_list_input=[]):
    # process contiguous
    _list_input = local_list_input
    count_delete = 0
    i_start = 0
    i_end = len(_list_input) - 1
    while i_start < len(_list_input) - 1:
        i_next = i_start + 1
        count_contiguous = 1

        # debug
        if debug_opt:
            print("while-1| i_start: {0} - i_next: {1} - i_end: {2}".format(i_start, i_next, len(_list_input) - 1))
            print(_list_input)

        while i_next <= len(_list_input) - 1:
            # debug
            if debug_opt:
                print("while-2| i_start: {0} [{1}] - i_next: {2} [{3}] - i_end: {4}".format(i_start, _list_input[i_start], i_next, _list_input[i_next], len(_list_input) - 1)) # debug

            if _list_input[i_start] == _list_input[i_next]:

                # If i_start value == i_next value => contiguous value
                count_contiguous += 1

                if i_next == len(_list_input) - 1:
                    #print(count_contiguous)
                    if count_contiguous >= 3:
                        del _list_input[i_start:i_next+1]
                        count_delete += i_next - i_start + 1
                        i_start = 0
                        break
                    else:
                        break
                else:
                    i_next +=1

            else:

                if count_contiguous >= 3:
                    del _list_input[i_start:i_next]
                    count_delete += i_next - i_start
                    i_start = 0

                break

        i_start += 1

    return int(count_delete)


# Global variables
debug_opt = False

# Get input from console
# Start
first_line_input = sys.stdin.readline().strip()
second_line_input = sys.stdin.readline().strip()

# Convert
first_line_input_map = list(map(int, first_line_input.split(" ")))
# Get info

var_n = first_line_input_map[0]
var_k = first_line_input_map[1]
var_x = first_line_input_map[2]

# Size of array
list_input_original = list(map(int, second_line_input.split(" ")))
list_count_possible_destroy = []
size_list = len(list_input_original)

# Debug
if debug_opt:
    print("")
    print("List input: {0}".format(list_input_original))
    print("Size of list: {0}".format(size_list))
    print("Var X: {0}".format(var_x))

# count delete


# represent first pointer
i_start = 0

# Inject var_x into middle of posible two index has same value => 3 index has same value
# Debug
if debug_opt:
    print("")
    print("[+] Try to inject var_x")

while i_start < (size_list - 1):

    # Initialize all evaluate variables
    count_delete = 0
    i_next = i_start + 1
    list_input_process = list(list_input_original)

    # Debug
    if debug_opt:
        print("")
        print("while-0| i_start: {0} [{1}] - i_next: {2} [{3}] - i_end: {4}".format(i_start, list_input_process[i_start], i_next, list_input_process[i_next], len(list_input_process) - 1)) # debug

    # If first and next pointer are same, we can inject ball var_x at the end
    # then delete them
    if int(list_input_process[i_start]) == int(var_x) and int(list_input_process[i_next]) == int(var_x):
        del list_input_process[i_next]
        del list_input_process[i_start]
        count_delete += 2
        count_delete_try = try_destroy_possible(local_list_input=list_input_process)
        count_delete += count_delete_try
        list_count_possible_destroy.append(int(count_delete))
        i_start += 1
        continue
    else:
        i_start += 1

    #time.sleep(1)

# Process list: list_count_possible_destroy
final_list_count_possible_destroy = list(set(list_count_possible_destroy))

# Debug
if debug_opt:
    print("")
    print("List input 2nd times: {0}".format(list_input_original))
    print("List count delete possible: {0}".format(final_list_count_possible_destroy))
    print("Count delete: {0}".format(max(final_list_count_possible_destroy)))
    print("")


if len(final_list_count_possible_destroy) == 0:
    print("0")
else:
    print(max(final_list_count_possible_destroy))
