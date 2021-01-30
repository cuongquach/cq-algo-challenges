# ProblemLink: http://codeforces.com/problemset/problem/572/A

import sys

def main():
	# Get input from console
	first_line_input = sys.stdin.readline().strip()
	second_line_input = sys.stdin.readline().strip()
	second_line_input = list(map(int, second_line_input.split(" ")))

	third_line_input = sys.stdin.readline().strip()
	third_line_input = list(map(int, third_line_input.split(" ")))

	fourth_line_input = sys.stdin.readline().strip()
	fourth_line_input = list(map(int, fourth_line_input.split(" ")))

	# Convert to list data to process
	var_k = second_line_input[0]
	var_m = second_line_input[1]

	array_A = third_line_input
	array_B = fourth_line_input

	# Sort order of array A | ascending order
	array_A.sort()

	# Sort order of array B | descending order
	array_B.sort(reverse=True)

	# Pick k numbers in array_A
	list_k_array_A = array_A[0:var_k]
	
	# Pick m numbers in array_B
	list_m_array_B = array_B[0:var_m]

	# Get the highest and lowest number in array_A
	highest_no_list_m_array_A = list_k_array_A[-1]
	lowest_no_list_m_array_A  = list_k_array_A[0]

	# Get the lowest number in array_B
	lowest_no_list_m_array_B = list_m_array_B[-1]

	# Process
	flag_ans = "NO"
	if highest_no_list_m_array_A < lowest_no_list_m_array_B and lowest_no_list_m_array_A < lowest_no_list_m_array_B:
		flag_ans = "YES"

	# Print out answer
	print(flag_ans)


if __name__ == "__main__":
    main()