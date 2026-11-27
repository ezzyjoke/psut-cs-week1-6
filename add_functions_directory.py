# Script to add Master Functions Directory to build_master_hub.py
import re

functions_html = """
    <!-- ========================================================================= -->
    <!-- MASTER FUNCTION DIRECTORY -->
    <!-- ========================================================================= -->
    <section id="functions-directory">
      <div class="section-header">
        <div class="section-num">📚</div>
        <h2>Master Function Directory (All Functions & Methods Used)</h2>
      </div>
      <p class="section-desc">A complete, categorized reference guide of every built-in function, standard library function, string method, list method, and custom exam algorithm function used in Weeks 1 through 6.</p>

      <!-- Category 1: Built-ins -->
      <div class="card">
        <h3 style="color:#38bdf8;">1. Python Standard Built-in Functions</h3>
        <table class="custom-table">
          <tr><th>Function</th><th>Syntax / Signature</th><th>What It Does</th><th>Return Type</th><th>Exam Example & Output</th></tr>
          <tr>
            <td><code>print()</code></td>
            <td><code>print(*args, sep=' ', end='\\n')</code></td>
            <td>Outputs values to console. <code>sep</code> controls separator between items; <code>end</code> controls line termination.</td>
            <td><code>None</code></td>
            <td><code>print(1, 2, sep='-', end='!')</code><br>&rarr; <code>1-2!</code></td>
          </tr>
          <tr>
            <td><code>input()</code></td>
            <td><code>input(prompt='')</code></td>
            <td>Pauses execution, displays prompt, waits for user to press Enter. <strong>ALWAYS returns a string!</strong></td>
            <td><code>str</code></td>
            <td><code>age = int(input('Age: '))</code><br>(Must convert to do math!)</td>
          </tr>
          <tr>
            <td><code>int()</code></td>
            <td><code>int(x)</code></td>
            <td>Converts a string or float to an integer. Truncates towards zero (chops decimals).</td>
            <td><code>int</code></td>
            <td><code>int('42') &rarr; 42</code><br><code>int(3.99) &rarr; 3</code></td>
          </tr>
          <tr>
            <td><code>float()</code></td>
            <td><code>float(x)</code></td>
            <td>Converts an integer or string to a floating-point decimal number.</td>
            <td><code>float</code></td>
            <td><code>float('2.5') &rarr; 2.5</code><br><code>float(7) &rarr; 7.0</code></td>
          </tr>
          <tr>
            <td><code>str()</code></td>
            <td><code>str(x)</code></td>
            <td>Converts any Python value to its string representation. Essential for string concatenation.</td>
            <td><code>str</code></td>
            <td><code>'Score: ' + str(95) &rarr; 'Score: 95'</code></td>
          </tr>
          <tr>
            <td><code>bool()</code></td>
            <td><code>bool(x)</code></td>
            <td>Evaluates the truthiness of <code>x</code>. <code>0</code>, <code>0.0</code>, <code>''</code>, <code>[]</code>, <code>None</code> are <code>False</code>; all else is <code>True</code>.</td>
            <td><code>bool</code></td>
            <td><code>bool(0) &rarr; False</code><br><code>bool('hi') &rarr; True</code></td>
          </tr>
          <tr>
            <td><code>type()</code></td>
            <td><code>type(x)</code></td>
            <td>Returns the class / type of the object.</td>
            <td><code>type</code></td>
            <td><code>type(10 / 2) &rarr; &lt;class 'float'&gt;</code><br><code>type(True) &rarr; &lt;class 'bool'&gt;</code></td>
          </tr>
          <tr>
            <td><code>len()</code></td>
            <td><code>len(sequence)</code></td>
            <td>Returns number of items in a string, list, or collection. Last valid index is <code>len - 1</code>.</td>
            <td><code>int</code></td>
            <td><code>len('PYTHON') &rarr; 6</code><br><code>len([10, 20]) &rarr; 2</code></td>
          </tr>
          <tr>
            <td><code>sum()</code></td>
            <td><code>sum(iterable)</code></td>
            <td>Calculates the total of all numbers in an iterable.</td>
            <td><code>int</code> / <code>float</code></td>
            <td><code>sum([10, 20, 30]) &rarr; 60</code></td>
          </tr>
          <tr>
            <td><code>max()</code></td>
            <td><code>max(a, b, ...)</code> or <code>max(list)</code></td>
            <td>Returns the largest item. When initializing manual max, never use 0 if inputs could be negative.</td>
            <td>Same as items</td>
            <td><code>max(4, 9, 2) &rarr; 9</code><br><code>max([-5, -1]) &rarr; -1</code></td>
          </tr>
          <tr>
            <td><code>min()</code></td>
            <td><code>min(a, b, ...)</code> or <code>min(list)</code></td>
            <td>Returns the smallest item. Crucial for unequal list merges: <code>min(len(a), len(b))</code>.</td>
            <td>Same as items</td>
            <td><code>min(4, 9, 2) &rarr; 2</code></td>
          </tr>
          <tr>
            <td><code>abs()</code></td>
            <td><code>abs(x)</code></td>
            <td>Returns the absolute (non-negative) magnitude of a number.</td>
            <td><code>int</code> / <code>float</code></td>
            <td><code>abs(-12) &rarr; 12</code><br><code>abs(3.5) &rarr; 3.5</code></td>
          </tr>
          <tr>
            <td><code>round()</code></td>
            <td><code>round(number, ndigits=0)</code></td>
            <td>Rounds a float to a specified number of decimal digits.</td>
            <td><code>int</code> / <code>float</code></td>
            <td><code>round(3.14159, 2) &rarr; 3.14</code></td>
          </tr>
          <tr>
            <td><code>range()</code></td>
            <td><code>range(stop)</code><br><code>range(start, stop[, step])</code></td>
            <td>Generates an immutable sequence of numbers from start up to, but NOT including, stop.</td>
            <td><code>range</code></td>
            <td><code>range(5) &rarr; 0,1,2,3,4</code><br><code>range(5,0,-1) &rarr; 5,4,3,2,1</code></td>
          </tr>
          <tr>
            <td><code>sorted()</code></td>
            <td><code>sorted(iterable)</code></td>
            <td>Returns a <strong>brand new sorted list</strong>, leaving the original sequence unchanged.</td>
            <td><code>list</code></td>
            <td><code>a = [3, 1]; b = sorted(a)</code><br>&rarr; <code>b=[1, 3], a=[3, 1]</code></td>
          </tr>
          <tr>
            <td><code>list()</code></td>
            <td><code>list(iterable)</code></td>
            <td>Constructs a mutable list from an iterable (like a range or string).</td>
            <td><code>list</code></td>
            <td><code>list(range(3)) &rarr; [0, 1, 2]</code><br><code>list('ABC') &rarr; ['A', 'B', 'C']</code></td>
          </tr>
          <tr>
            <td><code>set()</code></td>
            <td><code>set(iterable)</code></td>
            <td>Constructs a collection of unique elements. Used in slides to test if all elements are unique.</td>
            <td><code>set</code></td>
            <td><code>len(set(nums)) == len(nums)</code><br>(Returns <code>True</code> if all unique)</td>
          </tr>
        </table>
      </div>

      <!-- Category 2: Modules math and random -->
      <div class="card">
        <h3 style="color:#10b981;">2. Standard Library Modules (<code>math</code> & <code>random</code>)</h3>
        <table class="custom-table">
          <tr><th>Module Function / Const</th><th>Syntax</th><th>What It Does</th><th>Return Type</th><th>Exam Example & Output</th></tr>
          <tr>
            <td><code>math.sqrt()</code></td>
            <td><code>math.sqrt(x)</code></td>
            <td>Computes the square root &radic;x. <code>x</code> must be &ge; 0. Always returns a float.</td>
            <td><code>float</code></td>
            <td><code>math.sqrt(49) &rarr; 7.0</code></td>
          </tr>
          <tr>
            <td><code>math.pi</code></td>
            <td><code>math.pi</code></td>
            <td>Mathematical constant &pi; &approx; 3.141592653589793.</td>
            <td><code>float</code></td>
            <td><code>area = math.pi * r ** 2</code></td>
          </tr>
          <tr>
            <td><code>math.floor()</code></td>
            <td><code>math.floor(x)</code></td>
            <td>Rounds down to the nearest integer (same as <code>//</code> logic).</td>
            <td><code>int</code></td>
            <td><code>math.floor(3.8) &rarr; 3</code></td>
          </tr>
          <tr>
            <td><code>math.ceil()</code></td>
            <td><code>math.ceil(x)</code></td>
            <td>Rounds up to the nearest integer.</td>
            <td><code>int</code></td>
            <td><code>math.ceil(3.2) &rarr; 4</code></td>
          </tr>
          <tr>
            <td><code>random.randint()</code></td>
            <td><code>random.randint(a, b)</code></td>
            <td>Returns a random integer N such that a &le; N &le; b. <strong>INCLUSIVE of both endpoints!</strong></td>
            <td><code>int</code></td>
            <td><code>random.randint(1, 6)</code><br>&rarr; Can return 1, 2, 3, 4, 5, or 6</td>
          </tr>
        </table>
      </div>

      <!-- Category 3: String Methods -->
      <div class="card">
        <h3 style="color:#a855f7;">3. String Methods (Strings are IMMUTABLE &mdash; all return NEW strings)</h3>
        <table class="custom-table">
          <tr><th>String Method</th><th>Syntax</th><th>What It Does</th><th>Return Type</th><th>Exam Example & Output</th></tr>
          <tr>
            <td><code>.upper()</code></td>
            <td><code>s.upper()</code></td>
            <td>Returns a copy of <code>s</code> converted to uppercase. Original <code>s</code> is unchanged!</td>
            <td><code>str</code></td>
            <td><code>'hello'.upper() &rarr; 'HELLO'</code></td>
          </tr>
          <tr>
            <td><code>.lower()</code></td>
            <td><code>s.lower()</code></td>
            <td>Returns a copy of <code>s</code> converted to lowercase. Ideal for case-insensitive checks.</td>
            <td><code>str</code></td>
            <td><code>'PSUT'.lower() &rarr; 'psut'</code></td>
          </tr>
          <tr>
            <td><code>.strip()</code></td>
            <td><code>s.strip()</code></td>
            <td>Returns a copy with whitespace (spaces, tabs, newlines) removed from BOTH ends.</td>
            <td><code>str</code></td>
            <td><code>'  hi  '.strip() &rarr; 'hi'</code></td>
          </tr>
          <tr>
            <td><code>.find()</code></td>
            <td><code>s.find(sub[, start])</code></td>
            <td>Returns index of <strong>first</strong> occurrence of <code>sub</code>. Returns <strong>-1</strong> if not found. Does not crash!</td>
            <td><code>int</code></td>
            <td><code>'banana'.find('na') &rarr; 2</code><br><code>'banana'.find('xyz') &rarr; -1</code></td>
          </tr>
          <tr>
            <td><code>.count()</code></td>
            <td><code>s.count(sub)</code></td>
            <td>Returns number of non-overlapping occurrences of substring <code>sub</code>.</td>
            <td><code>int</code></td>
            <td><code>'banana'.count('a') &rarr; 3</code></td>
          </tr>
          <tr>
            <td><code>.replace()</code></td>
            <td><code>s.replace(old, new)</code></td>
            <td>Returns copy with all occurrences of <code>old</code> replaced by <code>new</code>.</td>
            <td><code>str</code></td>
            <td><code>'banana'.replace('a', 'o') &rarr; 'bonono'</code></td>
          </tr>
          <tr>
            <td><code>.split()</code></td>
            <td><code>s.split(sep=None)</code></td>
            <td>Splits string into a list of words. If <code>sep</code> is omitted, splits by ANY whitespace.</td>
            <td><code>list</code></td>
            <td><code>'a b c'.split() &rarr; ['a', 'b', 'c']</code><br><code>'1,2,3'.split(',') &rarr; ['1','2','3']</code></td>
          </tr>
          <tr>
            <td><code>.join()</code></td>
            <td><code>sep.join(list_of_str)</code></td>
            <td>Concatenates a list of strings into one string, inserting <code>sep</code> between each element.</td>
            <td><code>str</code></td>
            <td><code>'-'.join(['a', 'b']) &rarr; 'a-b'</code></td>
          </tr>
          <tr>
            <td><code>.startswith()</code></td>
            <td><code>s.startswith(prefix)</code></td>
            <td>Returns <code>True</code> if the string begins with <code>prefix</code>.</td>
            <td><code>bool</code></td>
            <td><code>'hello'.startswith('he') &rarr; True</code></td>
          </tr>
          <tr>
            <td><code>.endswith()</code></td>
            <td><code>s.endswith(suffix)</code></td>
            <td>Returns <code>True</code> if the string ends with <code>suffix</code> (e.g. <code>.jo</code>).</td>
            <td><code>bool</code></td>
            <td><code>'psut.edu.jo'.endswith('.jo') &rarr; True</code></td>
          </tr>
          <tr>
            <td><code>.isalpha()</code></td>
            <td><code>s.isalpha()</code></td>
            <td>Returns <code>True</code> if all characters are alphabetic letters and length &gt; 0.</td>
            <td><code>bool</code></td>
            <td><code>'Abc'.isalpha() &rarr; True</code><br><code>'A 1'.isalpha() &rarr; False</code></td>
          </tr>
          <tr>
            <td><code>.isdigit()</code></td>
            <td><code>s.isdigit()</code></td>
            <td>Returns <code>True</code> if all characters are numeric digits and length &gt; 0.</td>
            <td><code>bool</code></td>
            <td><code>'123'.isdigit() &rarr; True</code><br><code>'12.3'.isdigit() &rarr; False</code></td>
          </tr>
          <tr>
            <td><code>.rjust()</code></td>
            <td><code>s.rjust(width)</code></td>
            <td>Right-aligns string in a field of given width, padding with spaces (used in multiplication grid).</td>
            <td><code>str</code></td>
            <td><code>'4'.rjust(3) &rarr; '  4'</code></td>
          </tr>
        </table>
      </div>

      <!-- Category 4: List Methods -->
      <div class="card">
        <h3 style="color:#f59e0b;">4. List Methods (Lists are MUTABLE &mdash; in-place methods return <code>None</code>)</h3>
        <table class="custom-table">
          <tr><th>List Method</th><th>Syntax</th><th>What It Does</th><th>Mutates List?</th><th>Return Value</th><th>Exam Pitfall / Example</th></tr>
          <tr>
            <td><code>.append()</code></td>
            <td><code>a.append(x)</code></td>
            <td>Adds item <code>x</code> to the very end of list <code>a</code>.</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><code>a = [1]; a.append(2) &rarr; [1, 2]</code></td>
          </tr>
          <tr>
            <td><code>.insert()</code></td>
            <td><code>a.insert(i, x)</code></td>
            <td>Inserts item <code>x</code> at index <code>i</code>, shifting elements to the right.</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><code>a = [1, 2]; a.insert(0, 9) &rarr; [9, 1, 2]</code></td>
          </tr>
          <tr>
            <td><code>.remove()</code></td>
            <td><code>a.remove(x)</code></td>
            <td>Removes the <strong>first</strong> occurrence of value <code>x</code>. Raises <code>ValueError</code> if <code>x</code> not in list!</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><strong>DANGER:</strong> Looping with <code>a.remove(x)</code> skips subsequent elements!</td>
          </tr>
          <tr>
            <td><code>.pop()</code></td>
            <td><code>a.pop(i=-1)</code></td>
            <td>Removes and <strong>returns</strong> the item at index <code>i</code> (default is last item).</td>
            <td><strong>Yes</strong></td>
            <td><strong>Removed item</strong></td>
            <td><code>a = [10, 20]; x = a.pop() &rarr; x = 20, a = [10]</code></td>
          </tr>
          <tr>
            <td><code>.sort()</code></td>
            <td><code>a.sort()</code></td>
            <td>Sorts list <strong>in-place</strong> in ascending order.</td>
            <td><strong>Yes</strong></td>
            <td><strong><code>None</code></strong></td>
            <td><strong>FATAL TRAP:</strong> <code>a = a.sort()</code> destroys list by setting <code>a = None</code>!</td>
          </tr>
          <tr>
            <td><code>.reverse()</code></td>
            <td><code>a.reverse()</code></td>
            <td>Reverses elements of list <strong>in-place</strong>.</td>
            <td><strong>Yes</strong></td>
            <td><code>None</code></td>
            <td><code>a = [1, 2]; a.reverse() &rarr; a = [2, 1]</code> (Alters caller's list!)</td>
          </tr>
        </table>
      </div>

      <!-- Category 5: Course Custom Functions & Algorithms -->
      <div class="card">
        <h3 style="color:#f43f5e;">5. Course Algorithm Functions & Practice Problems (Weeks 1 to 6)</h3>
        <table class="custom-table">
          <tr><th>Function Name</th><th>Parameters</th><th>Core Logic & Exam Purpose</th><th>Return Value</th></tr>
          <tr>
            <td><code>distance(x1, y1, x2, y2)</code></td>
            <td><code>(x1, y1, x2, y2)</code></td>
            <td>Computes Euclidean distance between points: <code>math.sqrt((x1-x2)**2 + (y1-y2)**2)</code>.</td>
            <td><code>float</code></td>
          </tr>
          <tr>
            <td><code>circle_area(cx, cy, px, py)</code></td>
            <td><code>(cx, cy, px, py)</code></td>
            <td>Composes <code>distance</code> to compute radius $r$, then returns $\pi r^2$. Demonstrates function composition.</td>
            <td><code>float</code></td>
          </tr>
          <tr>
            <td><code>is_leap_year(year)</code></td>
            <td><code>year</code></td>
            <td>Checks leap year rule: Divisible by 400, or (divisible by 4 and NOT 100).</td>
            <td><code>bool</code> (True/False)</td>
          </tr>
          <tr>
            <td><code>days_in_february(year)</code></td>
            <td><code>year</code></td>
            <td>Reuses <code>is_leap_year(year)</code>: returns 29 if True, else 28.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>is_prime(n)</code></td>
            <td><code>n</code></td>
            <td>Flag loop testing divisors from 2 up to $n-1$. Early <code>return False</code> on first divisor; <code>return True</code> outside loop.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>print_table(n)</code></td>
            <td><code>n</code></td>
            <td>Loops <code>k</code> from 1 to 12 printing <code>n x k = n*k</code>. Helper function for nested multiplication table.</td>
            <td><code>None</code></td>
          </tr>
          <tr>
            <td><code>integer_square_root(n)</code></td>
            <td><code>n</code></td>
            <td>Slide mystery: Loops <code>i</code> from 0 to $n$. If <code>i*i == n</code> returns <code>i</code>, else returns <code>-1</code>.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>second_largest(count)</code></td>
            <td><code>count</code></td>
            <td>Slide mystery: Maintains <code>largest</code> and <code>second</code> variables across <code>count</code> user inputs.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>last_even()</code></td>
            <td>None</td>
            <td>Slide mystery: Loops until 0, overwrites <code>result = num</code> whenever <code>num % 2 == 0</code>. Returns last even number entered.</td>
            <td><code>int</code> or <code>None</code></td>
          </tr>
          <tr>
            <td><code>is_palindrome(s)</code></td>
            <td><code>s</code></td>
            <td>Two pointers <code>i = 0, j = len(s) - 1</code> advancing inward checking <code>s[i] != s[j]</code>. (Or <code>s == s[::-1]</code>).</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>is_equivalent(a, b)</code></td>
            <td><code>(a, b)</code></td>
            <td>Slide Week 6: Two-way membership test: every element of <code>a</code> in <code>b</code> AND every element of <code>b</code> in <code>a</code>. Ignores order/frequency.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>is_sublist(a, b)</code></td>
            <td><code>(a, b)</code></td>
            <td>Slide Week 6 mystery: Sliding window of size $n = len(a)$ over $b$: <code>if b[i:i+n] == a: return True</code>.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>is_sorted(nums)</code></td>
            <td><code>nums</code></td>
            <td>Neighbor comparison loop <code>range(len(nums) - 1)</code>: if <code>nums[i] > nums[i+1]</code> returns <code>False</code>.</td>
            <td><code>bool</code></td>
          </tr>
          <tr>
            <td><code>reverse_in_place(a)</code></td>
            <td><code>a</code></td>
            <td>Two pointers swapping <code>a[i], a[j] = a[j], a[i]</code> or <code>a[:] = a[::-1]</code>. Modifies original list.</td>
            <td><code>None</code></td>
          </tr>
          <tr>
            <td><code>find_index(nums, target)</code></td>
            <td><code>(nums, target)</code></td>
            <td>Linear search: returns <code>i</code> immediately when <code>nums[i] == target</code>. Returns <code>-1</code> after loop finishes.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>merge_lists(a, b)</code></td>
            <td><code>(a, b)</code></td>
            <td>Alternates elements up to <code>min(len(a), len(b))</code>, then appends slice leftovers <code>a[n:] + b[n:]</code>.</td>
            <td><code>list</code></td>
          </tr>
          <tr>
            <td><code>remove_duplicates(a)</code></td>
            <td><code>a</code></td>
            <td>Accumulator list: loops <code>for x in a:</code> and appends <code>x</code> only if <code>x not in result</code>. Preserves order.</td>
            <td><code>list</code></td>
          </tr>
          <tr>
            <td><code>count_greater(a, x)</code></td>
            <td><code>(a, x)</code></td>
            <td>Counts how many elements in list <code>a</code> are strictly greater than threshold <code>x</code>.</td>
            <td><code>int</code></td>
          </tr>
          <tr>
            <td><code>rotate_left(a)</code></td>
            <td><code>a</code></td>
            <td>Returns new list with first element moved to the back: <code>a[1:] + a[:1]</code>.</td>
            <td><code>list</code></td>
          </tr>
        </table>
      </div>
    </section>
"""

with open('build_master_hub.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add link to sidebar
sidebar_needle = '<a href="#cram-sheet" class="nav-link">📋 1-Hour Cram Sheet <span class="nav-badge">High Yield</span></a>'
new_sidebar_link = sidebar_needle + '\n    <a href="#functions-directory" class="nav-link">📚 Master Functions Directory <span class="nav-badge">All 40+</span></a>'

content = content.replace(sidebar_needle, new_sidebar_link)

# Add quick pill button
pills_needle = '<button class="pill-btn active" onclick="jumpSection(\'cram-sheet\')">📋 1-Hour Cram Sheet</button>'
new_pill = pills_needle + '\n      <button class="pill-btn" onclick="jumpSection(\'functions-directory\')">📚 Function Directory</button>'
content = content.replace(pills_needle, new_pill)

# Inject section before cram-sheet
section_needle = '    <!-- ========================================================================= -->\n    <!-- 1-HOUR EMERGENCY CRAM SHEET -->'
content = content.replace(section_needle, functions_html + '\n' + section_needle)

with open('build_master_hub.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated build_master_hub.py successfully with Master Function Directory!")
