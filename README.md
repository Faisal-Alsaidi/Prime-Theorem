# Prime-Theorem
A repo containing all of my programs in an effort to help prove the prime number theorem.

The prime theorem in question was developed by Nicole Molin, an old teacher of mine, who found a link between all prime numbers. The basic idea is to separate all numbers into columns where each of the digits of the numbers of each column add up to a specific number (so the first column would be 1, 10, 19, 28, etc., second column would be 2, 11, 20, 29, etc.). By analyzing these columns, it can be found that from any prime number in any column, the distance to the next prime is 18x. This can be extended to all other prime numbers in that same column, meaning that |x - y| = 18x with x and y being primes within the same column.

The purpose of my program is to display a graph showing this pattern in various ways to help find new discoveries related to it. The program uses Matplotlib to display the graph.
