import json

# The name of the text file you must create. Do not change it -
# the marker looks for this exact filename.
OUTFILE = "calculations.txt"


def saveJsonFile():
    try:
        with open('newZooAnimals.json', 'w') as NZA:
            toStore = [
                {
                    "name": "bob",
                    "age": 20,
                    "species": "crocodile"
                },
                {
                    "name": "susan",
                    "age": 10,
                    "species": "pigeon"
                }
            ]
            json.dump(toStore, NZA)
    except FileNotFoundError as Fnf:
        print(f"Could not find file {Fnf.filename}")


def saveTextFile(multiple, valueArray, value2):
    # TODO 1: Start with 'multiple' and multiply it by every value in
    # valueArray, then divide that answer by value2.
    # For example: 5 with [1, 3, 5, 7] and value2 = 2
    #              gives 5*1*3*5*7 = 525, then 525 / 2 = 262.5

    if value2 == 0:
        print("Error: Cannot divide by zero. Writing nothing to file.")
        return

    result = multiple
    for v in valueArray:
        result *= v
    result = result / value2

    # TODO 2: Write the multiple used, the full list of values, and the
    # final answer into the file named by OUTFILE.
    # Wrap the file handling in a try/except block and print a friendly
    # message instead of crashing.
    # Hint: opening a file in 'w' mode replaces whatever was there before.
    # Consider which mode you actually want. (Using 'a' to append multiple records if called more than once)
    try:
        with open(OUTFILE, 'a') as f:
            f.write(f"Multiple: {multiple}, Values: {valueArray}, Result: {result}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def readTextFile(filename):
    # TODO 3: Open the text file you just made and read from it.
    # Wrap it in a try/except block and print a friendly message if the
    # file does not exist.
    try:
        with open(filename, 'r') as f:
            # TODO 4: Once you have the contents, print them out to the terminal.
            # Think about how to loop through them and print each one nicely.
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Friendly message: The file '{filename}' does not exist yet.")


def demo():
    saveTextFile(5, [1, 3, 5, 7], 0)

    # TODO 5: Call saveTextFile with a value2 that is not zero, then
    # display the contents of the file in the terminal.
    saveTextFile(5, [1, 3, 5, 7], 2)
    readTextFile(OUTFILE)


demo()