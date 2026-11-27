import json

quiz_data = [
    # Week 1
    {
        "id": 1,
        "week": "Week 1",
        "category": "Terminology",
        "q": "Which type of programming error allows the program to run to completion without crashing, but produces incorrect results?",
        "opts": ["Syntax Error", "Semantic / Runtime Error", "Logic Error", "IndentationError"],
        "ans": 2,
        "exp": "Logic errors occur when program grammar and operations are legal, so Python executes everything smoothly, but the reasoning is flawed (e.g., avg = a + b / 2). Only the programmer's manual testing catches logic errors."
    },
    {
        "id": 2,
        "week": "Week 1",
        "category": "Precedence & Operators",
        "q": "What is the exact output of: print(2 + 3 * 4 ** 2)?",
        "opts": ["50", "400", "80", "146"],
        "ans": 0,
        "exp": "PEMDAS evaluation: Exponentiation has highest priority: 4 ** 2 = 16. Multiplication comes next: 3 * 16 = 48. Finally addition: 2 + 48 = 50."
    },
    {
        "id": 3,
        "week": "Week 1",
        "category": "Types & Operators",
        "q": "What is the exact output and type of the expression: 10 / 2 ?",
        "opts": ["5 (int)", "5.0 (float)", "5.0 (int)", "5 (str)"],
        "ans": 1,
        "exp": "In Python 3, single slash / is true float division and ALWAYS produces a float (5.0), regardless of whether the numbers divide evenly."
    },
    {
        "id": 4,
        "week": "Week 1",
        "category": "Floor Division & Modulo",
        "q": "What does print(-17 // 5, -17 % 5) display?",
        "opts": ["-3 -2", "-4 3", "-3 3", "-4 -2"],
        "ans": 1,
        "exp": "Floor division // rounds DOWN towards negative infinity. -17 / 5 = -3.4 -> floored down is -4. By Python's invariant a = (a // b) * b + (a % b): -17 = (-4 * 5) + remainder -> remainder = -17 - (-20) = 3."
    },
    {
        "id": 5,
        "week": "Week 1",
        "category": "Associativity",
        "q": "What is the output of print(2 ** 3 ** 2)?",
        "opts": ["64", "512", "36", "128"],
        "ans": 1,
        "exp": "Exponentiation (**) is right-to-left associative in Python. It evaluates as 2 ** (3 ** 2) = 2 ** 9 = 512. (Notice (2**3)**2 would be 64)."
    },
    {
        "id": 6,
        "week": "Week 1",
        "category": "Strings & Operators",
        "q": "What happens when you run: print('Age: ' + 20)?",
        "opts": ["Prints 'Age: 20'", "Raises a TypeError", "Prints 'Age: 20.0'", "Raises a ValueError"],
        "ans": 1,
        "exp": "You cannot concatenate a string (str) with an integer (int) using +. Python raises TypeError: can only concatenate str (not 'int') to str. You must do 'Age: ' + str(20) or print('Age:', 20)."
    },
    {
        "id": 7,
        "week": "Week 1",
        "category": "Digit Extraction",
        "q": "Given integer n = 472, which expression extracts the tens digit (7)?",
        "opts": ["n // 10", "(n // 10) % 10", "n % 100", "(n % 10) // 10"],
        "ans": 1,
        "exp": "n // 10 strips the ones digit, leaving 47. Then 47 % 10 extracts the last digit of 47, which is 7."
    },

    # Week 2
    {
        "id": 8,
        "week": "Week 2",
        "category": "Boolean Operators",
        "q": "What is the value of: not False and True or False ?",
        "opts": ["True", "False", "None", "SyntaxError"],
        "ans": 0,
        "exp": "Logical precedence: not > and > or. 1) not False -> True. 2) True and True -> True. 3) True or False -> True."
    },
    {
        "id": 9,
        "week": "Week 2",
        "category": "Short-Circuiting",
        "q": "Consider: x = 5; if x > 2 or x / 0 > 1: print('OK'). What happens when this code executes?",
        "opts": ["Crashes with ZeroDivisionError", "Prints 'OK'", "Prints False", "SyntaxError"],
        "ans": 1,
        "exp": "Short-circuit evaluation: In an 'or' expression, because x > 2 is True, Python does not evaluate the right operand (x / 0 > 1). Thus no division by zero occurs, and 'OK' prints."
    },
    {
        "id": 10,
        "week": "Week 2",
        "category": "Functions & Return",
        "q": "What will x hold after running:\ndef mystery(a, b):\n    print(a + b)\nx = mystery(3, 4)",
        "opts": ["7", "None", "0", "TypeError"],
        "ans": 1,
        "exp": "mystery prints 7 to the screen, but has no return statement. Functions in Python without a return statement implicitly return None."
    },
    {
        "id": 11,
        "week": "Week 2",
        "category": "Conditionals",
        "q": "What does this code print?\ntemp = 28\nif temp > 20:\n    print('Warm')\nelif temp > 25:\n    print('Hot')\nelse:\n    print('Cold')",
        "opts": ["Warm", "Hot", "Warm and Hot", "Cold"],
        "ans": 0,
        "exp": "In an if / elif / else chain, Python executes only the FIRST condition that evaluates to True. 28 > 20 is True, so 'Warm' prints, and the entire rest of the chain is skipped."
    },
    {
        "id": 12,
        "week": "Week 2",
        "category": "Truthiness Trap",
        "q": "What will print?\nx = 5\nif x == 1 or 2:\n    print('Match')\nelse:\n    print('No match')",
        "opts": ["No match", "Match", "SyntaxError", "TypeError"],
        "ans": 1,
        "exp": "Operator precedence binds == higher than or: (x == 1) or (2). x == 1 is False, but 2 is non-zero, which evaluates to truthy (True). False or True is True!"
    },
    {
        "id": 13,
        "week": "Week 2",
        "category": "Random Module",
        "q": "What are all possible return values of random.randint(1, 3)?",
        "opts": ["1, 2 only", "1, 2, 3 inclusive", "0, 1, 2", "Floats between 1.0 and 3.0"],
        "ans": 1,
        "exp": "random.randint(a, b) includes BOTH endpoints a and b. Thus it can return 1, 2, or 3."
    },
    {
        "id": 14,
        "week": "Week 2",
        "category": "Leap Year",
        "q": "Which of the following years is NOT a leap year?",
        "opts": ["2000", "2024", "1900", "2016"],
        "ans": 2,
        "exp": "Century years must be divisible by 400. 1900 is divisible by 100 but NOT 400 (1900 % 400 = 300), so 1900 is not a leap year. 2000 is divisible by 400 and is a leap year."
    },

    # Week 3
    {
        "id": 15,
        "week": "Week 3",
        "category": "Range Function",
        "q": "What list does list(range(5, 0, -1)) produce?",
        "opts": ["[5, 4, 3, 2, 1, 0]", "[5, 4, 3, 2, 1]", "[4, 3, 2, 1, 0]", "[5, 4, 3, 2]"],
        "ans": 1,
        "exp": "range(start, stop, step) strictly stops before the stop value. Thus with stop=0 and step=-1, it stops at 1: [5, 4, 3, 2, 1]."
    },
    {
        "id": 16,
        "week": "Week 3",
        "category": "Call Stack & Frames",
        "q": "What happens to a function's local variables when the function finishes executing (returns)?",
        "opts": ["They are saved in the global scope", "Their stack frame is destroyed and variables disappear from memory", "They become None", "They are moved to the caller's frame"],
        "ans": 1,
        "exp": "Each function call creates a local frame on the call stack. Upon return, the frame is popped and destroyed; local variables vanish."
    },
    {
        "id": 17,
        "week": "Week 3",
        "category": "Accumulators",
        "q": "What is the common bug in this accumulator code?\ns = 0\nfor i in range(1, 4):\n    s = 0\n    s += i\nprint(s)",
        "opts": ["s should start at 1", "s is reset to 0 inside the loop body every iteration", "range(1, 4) produces no values", "print(s) should be indented"],
        "ans": 1,
        "exp": "Resetting s = 0 inside the loop erases accumulated progress in each iteration. On the final iteration i=3, s becomes 0 + 3 = 3 instead of 6."
    },
    {
        "id": 18,
        "week": "Week 3",
        "category": "Loop Tracing",
        "q": "How many times does this loop iterate?\ni = 10\nwhile i > 0:\n    i -= 3",
        "opts": ["3 times", "4 times", "10 times", "Infinite loop"],
        "ans": 1,
        "exp": "Trace i: Starts at 10. Iteration 1: i becomes 7. Iteration 2: i becomes 4. Iteration 3: i becomes 1. Iteration 4: i becomes -2. Then -2 > 0 is False, loop stops. Total = 4 iterations."
    },
    {
        "id": 19,
        "week": "Week 3",
        "category": "Break vs Continue",
        "q": "What will print?\nfor i in range(1, 5):\n    if i == 3:\n        continue\n    print(i, end=' ')",
        "opts": ["1 2", "1 2 4", "1 2 3 4", "4"],
        "ans": 1,
        "exp": "continue skips the remainder of the current iteration when i == 3. So 1 and 2 print, 3 is skipped, and 4 prints -> 1 2 4."
    },

    # Week 4
    {
        "id": 20,
        "week": "Week 4",
        "category": "Nested Loops",
        "q": "How many total times will print('*') execute?\nfor i in range(1, 4):\n    for j in range(2):\n        print('*')",
        "opts": ["5", "6", "8", "12"],
        "ans": 1,
        "exp": "Outer loop range(1, 4) runs 3 times (i = 1, 2, 3). Inner loop range(2) runs 2 times. Total print calls = 3 * 2 = 6."
    },
    {
        "id": 21,
        "week": "Week 4",
        "category": "Triangular Loops",
        "q": "How many times does the inner loop body run?\nfor i in range(5):\n    for j in range(i):\n        pass",
        "opts": ["10", "15", "25", "20"],
        "ans": 0,
        "exp": "For i=0: 0 times. For i=1: 1 time. For i=2: 2 times. For i=3: 3 times. For i=4: 4 times. Total = 0 + 1 + 2 + 3 + 4 = 10."
    },
    {
        "id": 22,
        "week": "Week 4",
        "category": "Grids & Diagonals",
        "q": "In a square grid of size n x n with row i and col j, which condition identifies the anti-diagonal?",
        "opts": ["i == j", "i + j == n - 1", "i + j == n", "i == n - j"],
        "ans": 1,
        "exp": "Main diagonal is i == j. The anti-diagonal (from top-right to bottom-left) satisfies row + col == n - 1 (e.g. for n=4: (0,3), (1,2), (2,1), (3,0))."
    },
    {
        "id": 23,
        "week": "Week 4",
        "category": "Code Reading",
        "q": "What does this function do?\ndef mystery(n):\n    for i in range(n + 1):\n        if i * i == n:\n            return i\n    return -1",
        "opts": ["Returns n // 2", "Returns integer square root if n is a perfect square, else -1", "Computes n squared", "Checks if n is prime"],
        "ans": 1,
        "exp": "It checks each i from 0 up to n. If i * i == n, it returns i (the integer square root). If no whole number squares to n, it returns -1."
    },
    {
        "id": 24,
        "week": "Week 4",
        "category": "Primes Algorithm",
        "q": "Why is this prime function buggy?\ndef is_prime(n):\n    for d in range(2, n):\n        if n % d == 0:\n            return False\n        else:\n            return True",
        "opts": ["range(2, n) is invalid", "return True in else exits on d = 2 without checking remaining divisors", "n % d should be n // d", "It crashes for n = 2"],
        "ans": 1,
        "exp": "Putting return True in else makes the decision after checking only the first divisor d=2! For n=9, 9 % 2 != 0, so it immediately returns True even though 9 is divisible by 3!"
    },

    # Week 5
    {
        "id": 25,
        "week": "Week 5",
        "category": "Slicing",
        "q": "What is the output of print('PYTHON'[4:1:-1])?",
        "opts": ["'OHT'", "'YTHO'", "'NOTHY'", "'OHTY'"],
        "ans": 0,
        "exp": "'PYTHON' characters: 0:P, 1:Y, 2:T, 3:H, 4:O, 5:N. Start at index 4 ('O'), step -1 down to stop 1 (excluded): takes indices 4, 3, 2 -> 'O', 'H', 'T' -> 'OHT'."
    },
    {
        "id": 26,
        "week": "Week 5",
        "category": "Slicing Direction",
        "q": "What does 'PYTHON'[0:6:-1] evaluate to?",
        "opts": ["'NOHTYP'", "'' (empty string)", "IndexError", "'PYTHON'"],
        "ans": 1,
        "exp": "Step is negative (-1), meaning movement is right-to-left. You cannot start at 0 and move backward to reach 6, so Python returns an empty string ''."
    },
    {
        "id": 27,
        "week": "Week 5",
        "category": "Slicing Defaults",
        "q": "What does 'PYTHON'[-1:-7:-1] evaluate to?",
        "opts": ["''", "'NOHTYP'", "IndexError", "'PYTHON'"],
        "ans": 1,
        "exp": "Start at index -1 ('N'), step -1 backwards past index -6 ('P') to -7: traverses the entire string in reverse -> 'NOHTYP'."
    },
    {
        "id": 28,
        "week": "Week 5",
        "category": "String Immutability",
        "q": "What happens when you run:\ns = 'hello'\ns[0] = 'H'",
        "opts": ["s becomes 'Hello'", "TypeError: 'str' object does not support item assignment", "IndexError", "ValueError"],
        "ans": 1,
        "exp": "Strings in Python are immutable. You cannot modify them in place using index assignment."
    },
    {
        "id": 29,
        "week": "Week 5",
        "category": "String Methods",
        "q": "What is the result of 'banana'.find('na')?",
        "opts": ["2", "4", "True", "3"],
        "ans": 0,
        "exp": ".find() returns the lowest index where the substring starts. The first 'na' occurs at index 2."
    },
    {
        "id": 30,
        "week": "Week 5",
        "category": "String Methods",
        "q": "What does 'banana'.find('xyz') return?",
        "opts": ["False", "None", "-1", "IndexError"],
        "ans": 2,
        "exp": "When a substring is not found, .find() returns -1 (it does NOT crash or raise an exception)."
    },
    {
        "id": 31,
        "week": "Week 5",
        "category": "List Methods",
        "q": "What will print?\nnums = [3, 1, 2]\nnums = nums.sort()\nprint(nums)",
        "opts": ["[1, 2, 3]", "None", "[3, 2, 1]", "AttributeError"],
        "ans": 1,
        "exp": "nums.sort() modifies the list in place and returns None. Assigning nums = nums.sort() replaces the list with None!"
    },
    {
        "id": 32,
        "week": "Week 5",
        "category": "Split & Words",
        "q": "What does len('Hello World 2025'.split()) return?",
        "opts": ["16", "3", "2", "4"],
        "ans": 1,
        "exp": ".split() without arguments splits on whitespace into ['Hello', 'World', '2025']. The length is 3."
    },

    # Week 6
    {
        "id": 33,
        "week": "Week 6",
        "category": "Lists & Frequencies",
        "q": "What will print?\ndef mystery(nums):\n    c = [0] * 3\n    for n in nums:\n        c[n] += 1\n    return c\nprint(mystery([0, 1, 1, 2, 1]))",
        "opts": ["[1, 3, 1]", "[0, 1, 2]", "[3, 1, 1]", "IndexError"],
        "ans": 0,
        "exp": "This uses list indices as counters: c[0] counts zeros (1), c[1] counts ones (3), c[2] counts twos (1) -> [1, 3, 1]."
    },
    {
        "id": 34,
        "week": "Week 6",
        "category": "List Equivalence",
        "q": "Under the slides definition of is_equivalent(a, b), what does is_equivalent([1, 1, 2], [2, 1]) return?",
        "opts": ["False", "True", "IndexError", "None"],
        "ans": 1,
        "exp": "is_equivalent checks whether every element in a is in b AND every element in b is in a. It ignores element frequency and order, so [1, 1, 2] and [2, 1] are equivalent (True)."
    },
    {
        "id": 35,
        "week": "Week 6",
        "category": "Neighbor Boundaries",
        "q": "Why is this loop buggy?\nfor i in range(len(nums)):\n    if nums[i] > nums[i + 1]:\n        return False",
        "opts": ["range should start at 1", "IndexError on the final iteration when i = len(nums) - 1", "nums[i + 1] requires brackets", "It fails for empty list only"],
        "ans": 1,
        "exp": "When i reaches the final index len(nums) - 1, nums[i + 1] attempts to access an index out of bounds, crashing with IndexError. The range must be range(len(nums) - 1)."
    },
    {
        "id": 36,
        "week": "Week 6",
        "category": "Sublist Sliding Window",
        "q": "Given mystery(a, b) from Week 6:\ndef mystery(a, b):\n    n = len(a)\n    for i in range(len(b) - n + 1):\n        if b[i:i + n] == a:\n            return True\n    return False\nWhat is the best name for this function?",
        "opts": ["is_equal(a, b)", "is_sublist(a, b)", "reverse_list(b)", "sort_list(a)"],
        "ans": 1,
        "exp": "It slides a window of size len(a) across list b and compares each slice with a. It returns True if a appears as a contiguous sublist in b."
    },
    {
        "id": 37,
        "week": "Week 6",
        "category": "Mutating While Looping",
        "q": "What is nums after this code runs?\nnums = [-1, -2, 3]\nfor x in nums:\n    if x < 0:\n        nums.remove(x)",
        "opts": ["[3]", "[-2, 3]", "[]", "[-1, 3]"],
        "ans": 1,
        "exp": "When nums.remove(-1) executes, -2 shifts into index 0. The loop advances to index 1 (which now holds 3), completely skipping -2. Thus -2 remains: [-2, 3]."
    },
    {
        "id": 38,
        "week": "Week 6",
        "category": "List Reversal In-Place",
        "q": "Which code snippet correctly reverses list 'nums' in-place so that the caller's list is modified?",
        "opts": ["nums = nums[::-1]", "nums.reverse()", "nums = reversed(nums)", "nums = nums.sort()"],
        "ans": 1,
        "exp": "nums.reverse() (or slice assignment nums[:] = nums[::-1]) alters the existing list in memory in-place. Writing nums = nums[::-1] merely rebinds the local name."
    },
    {
        "id": 39,
        "week": "Week 6",
        "category": "Parallel Lists",
        "q": "What is the primary danger when working with parallel lists like names and scores?",
        "opts": ["They cannot hold different data types", "Sorting one list without simultaneously sorting the other scrambles the relationship between names and scores", "They cannot exceed 100 elements", "Parallel lists cannot be passed to functions"],
        "ans": 1,
        "exp": "In parallel lists, index i links related data (e.g. names[i] owns scores[i]). If you sort scores without updating names, student 0 gets student 5's grade!"
    },
    {
        "id": 40,
        "week": "Week 6",
        "category": "Edge Cases",
        "q": "Which list operation raises a ZeroDivisionError on an empty list nums = [] ?",
        "opts": ["sum(nums)", "len(nums)", "sum(nums) / len(nums)", "nums[:2]"],
        "ans": 2,
        "exp": "For an empty list, len(nums) is 0. Computing sum(nums) / len(nums) attempts 0 / 0, raising ZeroDivisionError: division by zero."
    }
]

with open('quiz_data.json', 'w', encoding='utf-8') as f:
    json.dump(quiz_data, f, indent=2)

print(f"Generated quiz_data.json with {len(quiz_data)} questions.")
