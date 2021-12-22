prime_numbers = [11, 3, 7, 5, 2]

# sort the list
prime_numbers.sort()
print(prime_numbers)

# Python3 program to Create a matrix with
# alternating rectangles of O and X

# Function to print alternating rectangles
# of 0 and X
def fill0X(m, n):
	
	# k - starting row index
	# m - ending row index
	# l - starting column index
	# n - ending column index
	# i - iterator
	i, k, l = 0, 0, 0

	# Store given number of rows and
	# columns for later use
	r = m
	c = n

	# A 2D array to store the output
	# to be printed
	a = [[None] * n for i in range(m)]
	x = 'X' # Initialize the character to
			# be stored in a[][]

	# Fill characters in a[][] in spiral form.
	# Every iteration fills one rectangle of
	# either Xs or Os
	while k < m and l < n:
		
		# Fill the first row from the
		# remaining rows
		for i in range(l, n):
			a[k][i] = x
		k += 1

		# Fill the last column from
		# the remaining columns
		for i in range(k, m):
			a[i][n - 1] = x
		n -= 1

		# Fill the last row from the
		# remaining rows
		if k < m:
			for i in range(n - 1, l - 1, -1):
				a[m - 1][i] = x
			m -= 1

		# Print the first column from
		# the remaining columns
		if l < n:
			for i in range(m - 1, k - 1, -1):
				a[i][l] = x
			l += 1

		# Flip character for next iteration
		x = 'X' if x == '0' else '0'

	# Print the filled matrix
	for i in range(r):
		for j in range(c):
			print(a[i][j], end = " ")
		print()

# Driver Code
if __name__ == '__main__':
	
	print("Output for m = 5, n = 6")
	fill0X(5, 6)

	print("Output for m = 4, n = 4")
	fill0X(4, 4)

	print("Output for m = 3, n = 4")
	fill0X(3, 4)
	
# This code is contributed by pranchalK
