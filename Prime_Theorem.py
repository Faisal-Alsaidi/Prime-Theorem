from matplotlib.pyplot import plot, show, ylabel, xlabel, title, grid
from re import search
from time import sleep


def isPrime(num):
    """Returns whether or not a number is prime."""
    assert num >= 2, 'Please enter a number greater than 2'
    if num % 2 == 0:
        return 0

    for i in range(3, num//2+1, 2):
        if num % i == 0:
            return 0

    return 1


def eratosthenes(min_num, max_num):
    """Returns an array of all prime numbers within the range specified.

    Keyword arguments:
    min_num -- Specifies the minimum range of the prime array
    max_num -- Specifies the maximum range of the prime array"""
    if max_num <= min_num:
        print("Please enter a max range greater than the min range")
    if min_num < 3:
        min_num = 3
    # Creates an array of all odd numbers from the minimum range to the maximum range
    temp_odds = [i for i in range(3, max_num-(max_num%2-1), 2)]

    # Loops through all the numbers in the array, removing the multiples of each number (since they're not prime)
    for i in range(3, max_num, 2):
        for j in range(i*2, max_num, i):
            if j % 2 == 1:
                temp_odds[(j-3)//2] = 0  # Fancy equation which sets the value of the number in the prime array to 0

    return [i for i in temp_odds if i != 0 and i >= min_num]  # Returns an array with only the primes


def prime_sequence(max_range, sequence_num):
    """Returns an array containing the prime sequence, being that S(n+1) = S(n)+(18*x), given that n is some prime and x
    is some unknown value which results in another prime. The sum of the digits of each of the prime numbers in the
    sequence should all equal the same number, specified by num.

    Keyword arguments:
    max_range -- Specifies the maximum range of the prime sequence
    sequence_num -- Specifies which prime sequence to return"""
    primes = eratosthenes(sequence_num, max_range)
    sequence_primes = []
    increment = 9
    i = sequence_num

    while i <= max_range:
        if i in primes:
            sequence_primes.append(i)
            increment = 18

        i += increment

    return sequence_primes


def main():
    """Runs through the program, prompting the user to input different values to output a graph
    based on what they want to analyze."""
    num_range = input("Enter a range of numbers you want to search through (format x,y, ex. 3,100) >>> ")

    # Ensures the syntax of the range is correct
    if not search("^[0-9]+,[0-9]+", num_range):
        print("Please enter the range using the format specified")
        return -1

    # Parses the inputs to integers
    num_range = num_range.split(',')
    num_range[0] = int(num_range[0])
    num_range[1] = int(num_range[1])

    # Prompts the user for the sequence they want to analyze and whether or not they want to analyze the distance
    # between the numbers, ensuring that the syntax of the inputs were correct
    sequence = input("Enter the sequence you want to analyze or if you want to analyze all primes ([0-9] or 'all') >>> ")
    if sequence != "all" and not search("^[0-9]$", sequence):
        print("Please enter the value using the format specified")
        return -1

    distance_num = input("Do you want to analyse the distance between each number or the numbers "
                         "themselves? (1 or 2) >>> ")
    if distance_num not in ("1", "2"):
        print("Please enter the value using the format specified")
        return -1

    # Prints out every prime number within a range or the distance between each number
    if sequence == "all":
        # Prints out every prime number
        if distance_num == "2":
            plot(eratosthenes(num_range[0], num_range[1]))
            grid(True)
            ylabel("Prime Numbers")
            title(f"All prime numbers within the range {num_range[0]} - {num_range[1]}")
            show()
        # Prints out the distances between each prime number
        else:
            primes = eratosthenes(num_range[0], num_range[1])
            distances = []
            for i in range(len(primes)-1):
                distances.append(primes[i+1]-primes[i])
            plot(primes[:-1], distances)
            grid(True)
            ylabel("Distances")
            xlabel("Primes")
            title(f"The distances between all prime numbers within the range {num_range[0]} - {num_range[1]}")
            show()

    # Prints out the prime numbers within a specific sequence
    else:
        sequence = int(sequence)
        if sequence in [3, 6, 9]:
            print(f"No prime sequence for {sequence}")
        else:
            ones = input("Enter the ones digit you want to filter the sequence by ([1,3,7,9] or 'all' to "
                         "output the entire sequence) >>> ")
            if distance_num == "2":
                plot_nums = prime_sequence(num_range[1], sequence)

                # Trims the sequence to only include numbers within the range specified by the user
                if plot_nums[0] < num_range[0]:
                    for i in range(len(plot_nums)):
                        if plot_nums[i] >= num_range[0]:
                            del plot_nums[0:i+1]
                            break

                # If specified, filters the number based on the number in the ones digit
                if ones != 'all':
                    if int(ones) not in [1, 3, 7, 9]:
                        print("Invalid ones digit sequence")
                        return -1
                    temp = [i for i in plot_nums if int(str(i)[-1]) == int(ones)]
                    plot_nums = temp

                y_plots = [i for i in range(len(plot_nums))]
                plot(y_plots, plot_nums, 'k', y_plots, plot_nums, 'bo')
                grid(True)
                ylabel("Prime Numbers")
                title(f"All prime numbers within the {sequence} sequence in the range {num_range[0]} - {num_range[1]}")
                show()

            else:
                plot_nums = prime_sequence(num_range[1], sequence)
                distances = []

                if plot_nums[0] < num_range[0]:
                    for i in range(len(plot_nums)):
                        if plot_nums[i] >= num_range[0]:
                            del plot_nums[0:i + 1]
                            break

                if ones != 'all':
                    temp = [i for i in plot_nums if int(str(i)[-1]) == int(ones)]
                    plot_nums = temp

                for i in range(len(plot_nums) - 1):
                    distances.append(plot_nums[i + 1] - plot_nums[i])

                plot(plot_nums[:-1], distances, 'k', plot_nums[:-1], distances, 'bo')
                grid(True)
                ylabel("Distances (to next number)")
                xlabel("Prime Numbers")
                title(f"The distances between all prime numbers within the "
                      f"{sequence} sequence in the range {num_range[0]} - {num_range[1]}")
                show()


main()
sleep(5)
