import json

# =========================================================================
# DATA DEFINITIONS FOR PSUT 11102 MIDTERM PREP HUB V2
# =========================================================================

# 20 FATAL EXAM TRAPS
traps_data = [
    {
        "id": 1,
        "title": "The Accidental None from a = a.sort()",
        "category": "Lists & Methods",
        "buggy": "nums = [4, 2, 7]\nnums = nums.sort()\nprint(nums)  # What prints?",
        "result": "Prints None!",
        "error_type": "NoneType assignment / Subsequent AttributeError",
        "explanation": "nums.sort() modifies the list in place and returns None. By assigning nums = nums.sort(), you overwrite the list with None. Subsequent operations like nums.append() will crash. If you want a new sorted list while keeping the original, use sorted(nums). If you want to sort in place, call nums.sort() on its own line without assignment.",
        "fix": "nums = [4, 2, 7]\nnums.sort()            # Modifies nums directly\nprint(nums)            # [2, 4, 7]\n\n# OR for a new list:\nnums = [4, 2, 7]\nnew_nums = sorted(nums) # nums remains [4, 2, 7]\nprint(new_nums)        # [2, 4, 7]"
    },
    {
        "id": 2,
        "title": "Division / ALWAYS Produces a float",
        "category": "Operators & Types",
        "buggy": "res = 10 / 2\nprint(res, type(res))",
        "result": "5.0 <class 'float'> (NOT 5 int!)",
        "error_type": "Type surprise in output prediction",
        "explanation": "In Python 3, the single slash operator (/) is true division and ALWAYS yields a float, even if the division has no remainder (e.g. 10 / 2 -> 5.0, 4 / 2 -> 2.0). If an exam question asks for the exact output or type, writing 5 is marked WRONG; it must be 5.0. To obtain an integer result, use floor division // (e.g. 10 // 2 -> 5).",
        "fix": "print(10 / 2)   # 5.0 (float)\nprint(10 // 2)  # 5   (int)"
    },
    {
        "id": 3,
        "title": "Negative Floor Division Rounds DOWN to -Infinity (-17 // 5)",
        "category": "Operators & Math",
        "buggy": "print(17 // 5)\nprint(-17 // 5)\nprint(-17 % 5)",
        "result": "3, -4, 3",
        "error_type": "Mathematical logic misconception",
        "explanation": "Floor division (//) always rounds DOWN towards negative infinity. 17 / 5 is 3.4 -> floored down is 3. However, -17 / 5 is -3.4 -> floored down is -4 (NOT -3!). By Python's invariant a = (a // b) * b + (a % b), we have: -17 = (-4 * 5) + remainder -> -17 = -20 + 3. Thus, -17 % 5 is +3, not -2!",
        "fix": "# Memory Rule:\n# 17 // 5  =  3  (remainder 17 - 15 = 2)\n# -17 // 5 = -4  (remainder -17 - (-20) = 3)"
    },
    {
        "id": 4,
        "title": "Right-to-Left Exponentiation Associativity (2 ** 3 ** 2)",
        "category": "Precedence & PEMDAS",
        "buggy": "print(2 ** 3 ** 2)",
        "result": "512 (NOT 64!)",
        "error_type": "Precedence evaluation error",
        "explanation": "While operators like +, -, *, /, //, % evaluate left-to-right, exponentiation (**) has RIGHT-TO-LEFT associativity. 2 ** 3 ** 2 evaluates as 2 ** (3 ** 2) = 2 ** 9 = 512. To force left-to-right evaluation, explicit parentheses are required: (2 ** 3) ** 2 = 8 ** 2 = 64.",
        "fix": "print(2 ** 3 ** 2)     # Evaluated as 2 ** (3 ** 2) = 512\nprint((2 ** 3) ** 2)   # Evaluated as (8) ** 2 = 64"
    },
    {
        "id": 5,
        "title": "print() vs return: The Reusability & None Trap",
        "category": "Functions",
        "buggy": "def add(a, b):\n    print(a + b)\n\nx = add(2, 3)\nprint(x * 2)",
        "result": "Prints 5, then crashes with TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'",
        "error_type": "TypeError / Misunderstanding function returns",
        "explanation": "print() displays text on the screen for humans to see. return sends a value back to the program so it can be stored in a variable, passed to another function, or used in arithmetic. If a function reaches the end without executing a return statement, Python automatically returns None. Because x is assigned None, trying to compute x * 2 crashes.",
        "fix": "def add(a, b):\n    return a + b   # Returns value to caller\n\nx = add(2, 3)      # x = 5\nprint(x * 2)       # Prints 10"
    },
    {
        "id": 6,
        "title": "The Unreachable Dead-Code Branch in if / elif Chains",
        "category": "Conditionals",
        "buggy": "temp = 28\nif temp > 20:\n    print('Warm')\nelif temp > 25:\n    print('Hot')  # UNREACHABLE DEAD CODE!\nelse:\n    print('Cold')",
        "result": "Prints 'Warm' even though temp is 28!",
        "error_type": "Logic bug / Unreachable condition",
        "explanation": "In an if / elif / else chain, Python tests conditions sequentially from top to bottom and executes ONLY the FIRST branch whose condition evaluates to True. Any subsequent branches are completely skipped. Because any number greater than 25 is also greater than 20, the second condition temp > 25 can never run. When writing threshold checks, always check the most restrictive condition first (descending order for >).",
        "fix": "temp = 28\nif temp > 25:      # Most restrictive condition first\n    print('Hot')\nelif temp > 20:\n    print('Warm')\nelse:\n    print('Cold')"
    },
    {
        "id": 7,
        "title": "String Immutability & Reassignment",
        "category": "Strings",
        "buggy": "s = 'Jello'\ns[0] = 'H'  # Crashes!\ns.upper()   # Does nothing useful!\nprint(s)",
        "result": "TypeError: 'str' object does not support item assignment",
        "error_type": "TypeError",
        "explanation": "In Python, strings are IMMUTABLE. You cannot alter individual characters within an existing string in memory. Furthermore, string methods like .upper(), .lower(), .replace(), and .strip() DO NOT modify the string in place; they return a brand new string. You must assign the result to a variable.",
        "fix": "s = 'Jello'\ns = 'H' + s[1:]   # Build new string: 'Hello'\ns = s.upper()       # Reassign returned new string: 'HELLO'\nprint(s)"
    },
    {
        "id": 8,
        "title": "Modifying a List While Iterating Over It",
        "category": "Loops & Lists",
        "buggy": "nums = [-1, -2, 3, 4]\nfor x in nums:\n    if x < 0:\n        nums.remove(x)\nprint(nums)  # Predict output!",
        "result": "[-2, 3, 4] (-2 was skipped and NOT removed!)",
        "error_type": "Silent logical corruption",
        "explanation": "When nums.remove(-1) executes at index 0, Python shifts all remaining elements one position to the left. The value -2 shifts into index 0. The for loop then advances its internal index pointer to index 1 (which now contains 3), completely skipping -2! Never modify a list's size while looping directly over it. Loop over a slice copy nums[:] or construct a new list.",
        "fix": "nums = [-1, -2, 3, 4]\n# Solution A: Iterate over a shallow copy\nfor x in nums[:]:\n    if x < 0:\n        nums.remove(x)\n\n# Solution B: List comprehension\nnums = [x for x in nums if x >= 0]"
    },
    {
        "id": 9,
        "title": "Slicing Direction Mismatch Yields Empty Sequence ('')",
        "category": "Slicing",
        "buggy": "s = 'PYTHON'\nprint(s[0:6:-1])\nprint(s[-1:-7:1])",
        "result": "'' (empty string for both!)",
        "error_type": "Output prediction mistake",
        "explanation": "The step argument determines the direction of traversal. A negative step (-1) moves backward (right-to-left). You cannot start at index 0 and travel backwards to reach index 6, so Python returns an empty string ''. Similarly, a positive step (+1) moves forward (left-to-right); you cannot start at index -1 (the end) and move forward to reach index -7 (the front).",
        "fix": "# For reversing or stepping backwards:\nprint(s[::-1])       # 'NOHTYP'\nprint(s[-1:-7:-1])   # 'NOHTYP'\nprint(s[5::-1])      # 'NOHTYP'"
    },
    {
        "id": 10,
        "title": "Initializing Max to 0 with All-Negative Numbers",
        "category": "Loop Patterns",
        "buggy": "nums = [-10, -5, -20, -2]\nlargest = 0  # FATAL MISTAKE!\nfor n in nums:\n    if n > largest:\n        largest = n\nprint('Largest:', largest)",
        "result": "Prints Largest: 0 (0 was not even in the list!)",
        "error_type": "Algorithm boundary flaw",
        "explanation": "Initializing a running maximum to 0 assumes at least one value will be >= 0. If all values are negative, the condition n > largest is never True, and 0 erroneously wins. Always initialize largest with the first element of the collection (largest = nums[0]) or the first user input before the loop.",
        "fix": "nums = [-10, -5, -20, -2]\nlargest = nums[0]  # Initialize with first real value\nfor n in nums[1:]:\n    if n > largest:\n        largest = n\nprint('Largest:', largest)  # -2"
    },
    {
        "id": 11,
        "title": "Neighbor Comparison Boundary Crash: range(len(a))",
        "category": "Loops & Lists",
        "buggy": "nums = [1, 3, 5, 2]\nfor i in range(len(nums)):\n    if nums[i] > nums[i + 1]:  # CRASHES on last iteration!\n        print('Not sorted')",
        "result": "IndexError: list index out of range",
        "error_type": "IndexError",
        "explanation": "When i reaches len(nums) - 1 (index 3), evaluating nums[i + 1] attempts to access nums[4], which does not exist. Whenever comparing adjacent elements a[i] and a[i + 1], the loop range MUST be range(len(nums) - 1).",
        "fix": "nums = [1, 3, 5, 2]\nfor i in range(len(nums) - 1):  # Stops before last element\n    if nums[i] > nums[i + 1]:\n        print('Not sorted')\n        break"
    },
    {
        "id": 12,
        "title": "Short-Circuit Evaluation Preventing Runtime Crashes",
        "category": "Boolean Logic",
        "buggy": "x = 5\nif x > 2 or x / 0 > 1:\n    print('Safe!')\nelse:\n    print('Danger!')",
        "result": "Prints 'Safe!' without crashing",
        "error_type": "Predicting crash when short-circuit prevents it",
        "explanation": "Python uses short-circuit evaluation for boolean operators. In an 'or' expression, if the left operand evaluates to True, the outcome is guaranteed to be True, so Python NEVER evaluates the right operand. Thus, x / 0 is never executed. Similarly, in 'A and B', if A is False, B is skipped.",
        "fix": "# Useful guard pattern in computing:\n# if len(s) > 0 and s[0] == 'A':  <- Safe against empty string IndexError!"
    },
    {
        "id": 13,
        "title": "The if x == 1 or 2: Truthiness Trap",
        "category": "Conditionals",
        "buggy": "x = 5\nif x == 1 or 2:\n    print('Matched!')\nelse:\n    print('No match')",
        "result": "Prints 'Matched!' even though x is 5!",
        "error_type": "Truthiness logical bug",
        "explanation": "Python parses this expression based on operator precedence: (x == 1) or (2). x == 1 evaluates to False, but any non-zero number (like 2) evaluates to True in a boolean context! Therefore, False or True is True! The condition will ALWAYS evaluate to True regardless of x.",
        "fix": "# Correct syntax:\nif x == 1 or x == 2:\n    print('Matched!')\n# OR Pythonic membership:\nif x in (1, 2):\n    print('Matched!')"
    },
    {
        "id": 14,
        "title": "random.randint(a, b) is INCLUSIVE of Both Ends",
        "category": "Built-in Modules",
        "buggy": "import random\n# Student thinks randint excludes b like range()\nroll = random.randint(1, 6)",
        "result": "Can produce 1, 2, 3, 4, 5, AND 6",
        "error_type": "API boundary misconception",
        "explanation": "Unlike range(a, b) which stops at b - 1, random.randint(a, b) includes BOTH endpoints a and b. random.randint(1, 6) can return 6 (ideal for dice). If you need an exclusive upper bound, random.randrange(a, b) acts like range().",
        "fix": "# random.randint(0, 1000) generates values from 0 up to and including 1000."
    },
    {
        "id": 15,
        "title": "Premature return Inside Search Loops",
        "category": "Search & Algorithms",
        "buggy": "def is_prime(n):\n    if n < 2:\n        return False\n    for d in range(2, n):\n        if n % d == 0:\n            return False\n        else:\n            return True  # BUG! Exits on d = 2!",
        "result": "is_prime(9) returns True! (9 is NOT prime)",
        "error_type": "Premature loop termination",
        "explanation": "Putting return True in an else branch inside the loop causes the function to exit during the very first iteration. For n = 9, when d = 2, 9 % 2 != 0, so it hits else and returns True immediately without ever testing d = 3! A search can only return True AFTER all candidates have been checked without finding a divisor.",
        "fix": "def is_prime(n):\n    if n < 2:\n        return False\n    for d in range(2, n):\n        if n % d == 0:\n            return False\n    return True  # Placed OUTSIDE and AFTER the loop"
    },
    {
        "id": 16,
        "title": "Local vs Global Rebinding vs In-Place Mutation",
        "category": "Functions & Scope",
        "buggy": "def reverse_wrong(a):\n    a = a[::-1]  # Creates local 'a', caller list unchanged!\n\nnums = [1, 2, 3]\nreverse_wrong(nums)\nprint(nums)  # Still [1, 2, 3]!",
        "result": "Prints [1, 2, 3]",
        "error_type": "Scope rebinding vs in-place mutation",
        "explanation": "Writing a = a[::-1] inside a function creates a new local variable named 'a' pointing to a new reversed list in memory. The caller's list remains unchanged! To modify the caller's list, you must either call an in-place method like a.reverse() or perform slice assignment a[:] = a[::-1].",
        "fix": "def reverse_correct(a):\n    a[:] = a[::-1]  # Slice assignment mutates the existing list\n\nnums = [1, 2, 3]\nreverse_correct(nums)\nprint(nums)  # [3, 2, 1]"
    },
    {
        "id": 17,
        "title": "UnboundLocalError in Linear Search",
        "category": "Debugging & Scope",
        "buggy": "def find_index(nums, target):\n    for i in range(len(nums)):\n        if nums[i] == target:\n            pos = i\n            break\n    return pos  # Crashes if target not in nums!\n\nfind_index([1, 2, 3], 9)",
        "result": "UnboundLocalError: cannot access local variable 'pos' where it is not associated with a value",
        "error_type": "UnboundLocalError",
        "explanation": "If the target is not in the list, the if statement never runs, so the variable pos is never created. When Python reaches return pos, pos does not exist! Either initialize pos = -1 before the loop or return i immediately upon finding the target and return -1 after the loop.",
        "fix": "def find_index(nums, target):\n    for i in range(len(nums)):\n        if nums[i] == target:\n            return i\n    return -1"
    },
    {
        "id": 18,
        "title": "Merging Lists of Unequal Lengths Index Crash",
        "category": "Parallel Lists & Algorithms",
        "buggy": "def merge(a, b):\n    res = []\n    for i in range(len(a)):\n        res.append(a[i])\n        res.append(b[i])  # Crashes if len(b) < len(a)!\n    return res",
        "result": "IndexError: list index out of range (if b shorter than a)",
        "error_type": "IndexError / Silent data dropping",
        "explanation": "Looping up to len(a) assumes both lists are identical in length. If b is shorter, b[i] crashes. If b is longer, elements of b beyond len(a) are silently dropped. Always loop up to min(len(a), len(b)), then append remaining elements using slice slicing a[n:] + b[n:].",
        "fix": "def merge_safe(a, b):\n    res = []\n    n = min(len(a), len(b))\n    for i in range(n):\n        res.append(a[i])\n        res.append(b[i])\n    res += a[n:] + b[n:]  # Attach leftovers\n    return res"
    },
    {
        "id": 19,
        "title": "String Slices NEVER Throw IndexError",
        "category": "Slicing Edge Cases",
        "buggy": "s = 'CAT'\nprint(s[10])      # Case A: direct index\nprint(s[0:10])    # Case B: slice",
        "result": "Case A raises IndexError. Case B prints 'CAT' safely without error!",
        "error_type": "IndexError vs Slicing Graceful Clamping",
        "explanation": "Direct indexing s[i] requires the index to exist (-len <= i < len); otherwise it raises an IndexError. In contrast, slicing s[start:stop] is designed to gracefully clamp out-of-bounds indices to the sequence boundaries. s[0:100] on a 3-character string simply returns the 3 characters.",
        "fix": "# Direct indexing: check len first\nif len(s) > 10:\n    val = s[10]\n# Slicing: always safe\nval = s[0:10]"
    },
    {
        "id": 20,
        "title": "string.split() Delimiter Behavior",
        "category": "String Methods",
        "buggy": "s = 'apple   banana   orange'\nprint(s.split())\nprint(s.split(' '))",
        "result": "s.split() -> ['apple', 'banana', 'orange']\ns.split(' ') -> ['apple', '', '', 'banana', '', '', 'orange']",
        "error_type": "Output prediction mistake",
        "explanation": "s.split() with NO arguments treats runs of consecutive whitespace (spaces, tabs, newlines) as a single delimiter and removes empty strings. But s.split(' ') splits on EVERY SINGLE space character, resulting in numerous empty strings '' for consecutive spaces.",
        "fix": "# Use s.split() for general whitespace splitting\nwords = s.split()"
    }
]

# Write to file
with open('traps_data.json', 'w', encoding='utf-8') as f:
    json.dump(traps_data, f, indent=2)

print("Generated traps_data.json successfully with 20 detailed traps.")
