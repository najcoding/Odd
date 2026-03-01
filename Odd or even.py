# Program to generate squares of numbers in a given range
# and separate them into odd and even lists.

def get_integer(prompt):
    """Safely get an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_squares(start, end):
    """Generate a list of squares for numbers in the given range."""
    return [n ** 2 for n in range(start, end + 1)]

def separate_odd_even(numbers):
    """Separate numbers into odd and even lists."""
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return evens, odds

def main():
    print("=== Square Values Generator ===")
    
    start = get_integer("Enter start of range: ")
    end = get_integer("Enter end of range: ")
    
   
    if start > end:
        start, end = end, start  
    
    squares = generate_squares(start, end)
    
    evens, odds = separate_odd_even(squares)
    
    print(f"\nSquares between {start} and {end}: {squares}")
    print(f"Even squares: {evens}")
    print(f"Odd squares: {odds}")

if __name__ == "__main__":
    main()
