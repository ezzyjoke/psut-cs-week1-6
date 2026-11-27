import json

flashcards_data = [
    # Week 1
    {"week": "Week 1", "q": "What is the difference between High-Level and Low-Level languages?", "a": "High-level languages (Python, C++) are human-readable, portable, and hide hardware details. Low-level languages (Assembly, Machine code) are tied directly to CPU architecture and execute instructions via registers/binary."},
    {"week": "Week 1", "q": "How does Python run your code? (Compiler vs Interpreter)", "a": "Python is a hybrid! It first compiles source code (.py) into intermediate Bytecode (.pyc), which is then interpreted instruction-by-instruction by the Python Virtual Machine (PVM)."},
    {"week": "Week 1", "q": "Name the 3 kinds of programming errors and who catches them.", "a": "1. Syntax Error: breaks grammar rules, caught by Python before running.\n2. Runtime/Semantic Error: crashes while executing (e.g. 10/0, TypeError).\n3. Logic Error: runs without crashing but produces the wrong answer; caught ONLY by the programmer through testing."},
    {"week": "Week 1", "q": "What does floor division (//) do with negative numbers? (e.g. -17 // 5)", "a": "It rounds DOWN towards negative infinity. -17 / 5 = -3.4, so floored down is -4 (NOT -3!)."},
    {"week": "Week 1", "q": "What is the result and type of 10 / 2?", "a": "5.0 of type float! Single slash / in Python 3 ALWAYS returns a float, even if there is no remainder."},
    {"week": "Week 1", "q": "What is the evaluation order and result of 2 ** 3 ** 2?", "a": "Exponentiation (**) is right-to-left associative! Evaluates as 2 ** (3 ** 2) = 2 ** 9 = 512, NOT 64."},
    {"week": "Week 1", "q": "How do you extract the last digit and strip the last digit of integer n?", "a": "Last digit: n % 10\nStrip last digit: n // 10\nTens digit: (n // 10) % 10"},
    {"week": "Week 1", "q": "What does input() return, and how do you do arithmetic with it?", "a": "input() ALWAYS returns a string (str). You must explicitly convert it using int(input()) or float(input())."},

    # Week 2
    {"week": "Week 2", "q": "What is the precedence order among logical operators: and, or, not?", "a": "Highest: not\nMiddle: and\nLowest: or\nExample: not False and True or False -> True and True or False -> True."},
    {"week": "Week 2", "q": "Explain Short-Circuit evaluation with an example.", "a": "Python stops evaluating logical expressions as soon as the outcome is certain.\n- In 'A or B': if A is True, B is never evaluated (e.g. True or 5/0 > 1 won't crash).\n- In 'A and B': if A is False, B is never evaluated."},
    {"week": "Week 2", "q": "Why is the order of conditions in an if/elif chain critical?", "a": "Python executes ONLY the first True branch and skips the rest. If a broad condition is checked before a specific one (e.g. temp > 20 before temp > 25), the second condition becomes unreachable dead code."},
    {"week": "Week 2", "q": "What is the difference between multiple separate if statements vs an if/elif/else chain?", "a": "Separate if statements are independent; all of them are tested and multiple can execute. In an if/elif/else chain, cases are mutually exclusive; at most ONE branch executes."},
    {"week": "Week 2", "q": "What does a function return if it does not have a return statement?", "a": "It returns None! print() inside a function only outputs text to the screen; it does not return data to the caller."},
    {"week": "Week 2", "q": "Is random.randint(a, b) inclusive or exclusive?", "a": "INCLUSIVE of both endpoints a and b! random.randint(1, 6) can produce 1, 2, 3, 4, 5, or 6."},
    {"week": "Week 2", "q": "What is the condition for a leap year?", "a": "Divisible by 4, EXCEPT century years (divisible by 100), which MUST be divisible by 400.\nFormula: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)."},

    # Week 3
    {"week": "Week 3", "q": "What is a Call Frame (Activation Record)?", "a": "A temporary block of memory created on the call stack when a function is called, holding its parameters and local variables. It is destroyed when the function returns."},
    {"week": "Week 3", "q": "What is Variable Shadowing?", "a": "When a local variable inside a function shares the same name as a global variable, the local variable hides (shadows) the global variable within the function body."},
    {"week": "Week 3", "q": "What sequence does range(5, 0, -1) generate?", "a": "5, 4, 3, 2, 1 (Stops strictly BEFORE 0!)."},
    {"week": "Week 3", "q": "What initial value should you use for an accumulator sum vs product?", "a": "Sum accumulator: total = 0 (neutral for addition)\nProduct/Factorial accumulator: fact = 1 (neutral for multiplication). Never reset inside the loop!"},
    {"week": "Week 3", "q": "Why is initializing largest = 0 a critical bug?", "a": "If the dataset contains only negative numbers (e.g. [-10, -5, -20]), 0 will be larger than all of them and falsely win. Always initialize largest = nums[0] or with the first user input."},
    {"week": "Week 3", "q": "What is the difference between break and continue?", "a": "break terminates the loop immediately and jumps to statements after the loop.\ncontinue skips the remainder of the current iteration and jumps to the next iteration."},
    {"week": "Week 3", "q": "How does a Sentinel loop work?", "a": "A while loop that reads values until a special sentinel value (e.g. -1 or 'quit') is entered. Key: read once BEFORE the loop, and once at the BOTTOM of the loop body."},

    # Week 4
    {"week": "Week 4", "q": "How do nested loops execute, and how many times does the inner body run?", "a": "For each single iteration of the outer loop, the inner loop runs from start to finish. If outer runs R times and inner runs C times, the body runs R * C times."},
    {"week": "Week 4", "q": "How many times does this run: for i in range(5): for j in range(i): ?", "a": "0 + 1 + 2 + 3 + 4 = 10 times."},
    {"week": "Week 4", "q": "Why is a flag/break faster than counting divisors for primality?", "a": "With a flag, as soon as a single divisor d is found (n % d == 0), we break immediately. A divisor counter checks every number up to n even if n is even."},
    {"week": "Week 4", "q": "What is the formula for the main diagonal vs anti-diagonal in an n x n grid?", "a": "Main diagonal: row == col (i == j)\nAnti-diagonal: row + col == n - 1 (i + j == n - 1)."},
    {"week": "Week 4", "q": "What is the danger of putting return True inside a loop's else branch?", "a": "It causes premature termination on the first iteration! E.g. in is_prime(9), when d=2, 9%2 != 0, so it hits else and wrongly returns True."},

    # Week 5
    {"week": "Week 5", "q": "What are positive and negative index ranges for a string of length n?", "a": "Positive indices: 0 to n - 1\nNegative indices: -n (first char) to -1 (last char). Accessing index n raises IndexError."},
    {"week": "Week 5", "q": "What are the default values in slice s[start:stop:step] when step is positive vs negative?", "a": "Positive step (+): start defaults to 0, stop defaults to len(s).\nNegative step (-): start defaults to len(s)-1 (-1), stop defaults to before index 0."},
    {"week": "Week 5", "q": "What does s[0:6:-1] evaluate to for 'PYTHON'?", "a": "Empty string ''! You cannot start at 0 and move backward with step -1 to reach index 6."},
    {"week": "Week 5", "q": "Why does s[0] = 'H' fail for string s?", "a": "Strings are IMMUTABLE in Python. To change a string, build a new one: s = 'H' + s[1:]."},
    {"week": "Week 5", "q": "What does s.find('x') return if 'x' is not in s?", "a": "Returns -1 (it does NOT crash or raise an error). Note: if s.find('a') returns 0, 0 is a valid index, not False!"},
    {"week": "Week 5", "q": "What is the difference between a.sort() and sorted(a)?", "a": "a.sort() modifies the list in-place and returns None.\nsorted(a) returns a brand new sorted list while leaving original list a unchanged."},
    {"week": "Week 5", "q": "What does a = [0] * 4 create?", "a": "[0, 0, 0, 0] — a list of 4 zeros, commonly used for frequency counting."},

    # Week 6
    {"week": "Week 6", "q": "Why use while len(nums) < 100 instead of for loop when generating unique random numbers?", "a": "Duplicates are skipped! A for loop would execute exactly 100 times, but if duplicates are skipped, fewer than 100 numbers would be collected."},
    {"week": "Week 6", "q": "What is the correct loop range to check if a list is sorted by comparing a[i] and a[i+1]?", "a": "for i in range(len(a) - 1): to prevent a[i + 1] from causing an IndexError on the last element."},
    {"week": "Week 6", "q": "What is a Parallel List and what is the #1 rule when working with them?", "a": "Two or more lists where elements at the same index i correspond to the same entity (e.g. names[i], grades[i]). Rule: Keep them the same length and NEVER sort just one list!"},
    {"week": "Week 6", "q": "How do you reverse a list in-place so caller sees the change?", "a": "nums.reverse() OR nums[:] = nums[::-1]. (Writing nums = nums[::-1] only rebinds the local variable)."},
    {"week": "Week 6", "q": "How does a frequency counter histogram list work? (e.g. c[n] += 1)", "a": "The value n itself is used as the index in the counter list: c[0] counts zeros, c[1] counts ones, etc."},
    {"week": "Week 6", "q": "What happens if you remove elements from a list while iterating: for x in a: a.remove(x)?", "a": "It shifts elements left and skips the element immediately following the removed one! E.g. [-1, -2, 3] leaves [-2, 3]."},
    {"week": "Week 6", "q": "What are the 6 critical edge cases to test for any list function?", "a": "1. Empty list []\n2. Single element [x]\n3. All duplicates [3, 3, 3]\n4. Target missing (-1 or False)\n5. Unequal lengths\n6. All negative numbers"}
]

with open('flashcards_data.json', 'w', encoding='utf-8') as f:
    json.dump(flashcards_data, f, indent=2)

print(f"Generated flashcards_data.json with {len(flashcards_data)} cards.")
