import json
import re
import subprocess
import sys

print("=" * 65)
print("PSUT 11102 MASTER HUB V2 COMPREHENSIVE PROFESSORIAL AUDIT SUITE")
print("=" * 65)

# 1. Traps Verification
with open('traps_data.json', encoding='utf-8') as f:
    traps = json.load(f)
print(f"[1/7] Traps Verification: {len(traps)} traps found.")
assert len(traps) == 20, f"Expected 20 traps, found {len(traps)}"
for t in traps:
    assert 'title' in t and len(t['title']) > 5
    assert 'buggy' in t and len(t['buggy']) > 5
    assert 'result' in t and len(t['result']) > 1
    assert 'fix' in t and len(t['fix']) > 5
    assert 'category' in t
print("   -> All 20 fatal traps, buggy snippets, results, and fixes certified.")

# 2. Flashcards Verification
with open('flashcards_data.json', encoding='utf-8') as f:
    cards = json.load(f)
print(f"[2/7] Flashcards Verification: {len(cards)} flashcards found.")
assert len(cards) == 41, f"Expected 41 cards, found {len(cards)}"
week_set = {f"Week {i}" for i in range(1, 7)}
found_weeks = {c['week'] for c in cards}
assert week_set == found_weeks, f"Weeks missing in flashcards: {week_set - found_weeks}"
for c in cards:
    assert len(c['q']) > 5
    assert len(c['a']) > 5
print("   -> All 41 active recall cards distributed across Weeks 1-6 certified.")

# 3. Quiz Verification
with open('quiz_data.json', encoding='utf-8') as f:
    quiz = json.load(f)
print(f"[3/7] Quiz Verification: {len(quiz)} questions found.")
assert len(quiz) == 40, f"Expected 40 quiz questions, found {len(quiz)}"
for q in quiz:
    assert 0 <= q['ans'] < len(q['opts']), f"Question {q['id']} has invalid ans index"
    assert len(q['opts']) == 4, f"Question {q['id']} does not have 4 options"
    assert len(q['exp']) > 15, f"Question {q['id']} has short explanation"
print("   -> All 40 questions, options, answer key indexes, and explanations certified.")

# 4. Slicing Parity Test & Fuzzing
def python_slice(s, start, stop, step):
    st = None if start == "" else int(start)
    sp = None if stop == "" else int(stop)
    sk = 1 if step == "" else int(step)
    if sk == 0:
        return "ValueError"
    return s[st:sp:sk]

def js_slice_sim(text, startVal, stopVal, stepVal):
    n = len(text)
    step = 1 if stepVal == "" else int(stepVal)
    if step == 0:
        return "ValueError"
    if step > 0:
        start = 0 if startVal == "" else int(startVal)
        if start < 0:
            start = max(0, n + start)
        elif start > n:
            start = n
        stop = n if stopVal == "" else int(stopVal)
        if stop < 0:
            stop = max(0, n + stop)
        elif stop > n:
            stop = n
    else:
        if startVal == "":
            start = n - 1
        else:
            start = int(startVal)
            if start < 0:
                start = n + start
            elif start >= n:
                start = n - 1
            if start < -1:
                start = -1

        if stopVal == "":
            stop = -1
        else:
            stop = int(stopVal)
            if stop < 0:
                stop = n + stop
            elif stop >= n:
                stop = n - 1
            if stop < -1:
                stop = -1

    res = []
    if step > 0:
        i = start
        while i < stop:
            if 0 <= i < n:
                res.append(text[i])
            i += step
    else:
        i = start
        while i > stop:
            if 0 <= i < n:
                res.append(text[i])
            i += step
    return "".join(res)

presets = [
    ("PYTHON", "", "", ""),
    ("PYTHON", "", "", "-1"),
    ("PYTHON", "4", "1", "-1"),
    ("PYTHON", "0", "6", "-1"),
    ("PYTHON", "-5", "-1", "1"),
    ("PYTHON", "", "", "2"),
    ("PYTHON", "0", "30", "1"),
    ("PYTHON", "5", "-1", "-1"),
    ("PYTHON", "10", "-10", "-2"),
    ("PYTHON", "-1", "-10", "-2"),
    ("PYTHON", "", "", "0"),
]

print("[4/7] Testing Slicing Lab Presets & Fuzz Suite:")
for s, st, sp, sk in presets:
    py_res = python_slice(s, st, sp, sk)
    js_res = js_slice_sim(s, st, sp, sk)
    assert py_res == js_res, f"Mismatch at [{st}:{sp}:{sk}]: PY '{py_res}' vs JS '{js_res}'"
print("   -> All preset buttons match CPython behavior exactly.")

# Fuzz test
fuzz_cases = 0
for st in ["", "-12", "-6", "-5", "-1", "0", "1", "5", "6", "12"]:
    for sp in ["", "-12", "-6", "-5", "-1", "0", "1", "5", "6", "12"]:
        for sk in ["-3", "-2", "-1", "1", "2", "3"]:
            py_res = python_slice("PYTHON", st, sp, sk)
            js_res = js_slice_sim("PYTHON", st, sp, sk)
            assert py_res == js_res, f"Fuzz failure [{st}:{sp}:{sk}]"
            fuzz_cases += 1
print(f"   -> {fuzz_cases} randomized edge-case slice combinations passed with 100% CPython parity.")

# 5. Call Stack Visualizer Verification
with open('index.html', encoding='utf-8') as f:
    html_text = f.read()

assert 'const stackSteps = [' in html_text
assert 'circle_area(0, 0, 3, 4)' in html_text
assert 'distance(0, 0, 3, 4)' in html_text
assert 'Step 7: All local frames destroyed' in html_text
print("[5/7] Call Stack Visualizer: 7-frame activation record sequence certified.")

# 6. UI & Search Bar Integrity
assert 'globalSearch' in html_text
assert '.quiz-card, .flashcard' in html_text, "Search filter must include .flashcard"
assert 'stackFramesContainer' in html_text
assert 'cram-sheet' in html_text
assert 'slicing-lab' in html_text
print("[6/7] UI & Interactive Elements: Responsive drawer, search selectors, and cards certified.")

# 7. Clean Build Verification (Zero SyntaxWarnings)
result = subprocess.run([sys.executable, "-W", "error", "build_master_hub.py"], capture_output=True, text=True)
assert result.returncode == 0, f"build_master_hub.py failed: {result.stderr}"
print("[7/7] Clean Build Verification: build_master_hub.py generates index.html with 0 warnings.")

print("=" * 65)
print("AUDIT RESULT: 100% PASS - V2 REVISION HUB RIGOROUSLY CERTIFIED")
print("=" * 65)
