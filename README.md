# Python-print-tutorial
# 📘 Python `print()` Function – Full Beginner to Intermediate Guide

## ✅ Introduction

The `print()` function in Python is one of the most commonly used built-in functions. It outputs information to the console (or other destinations like files). This guide documents key features of `print()` and how we've used it in learning so far.

---

## 🔹 Basic Syntax

```python
print(object, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

- `object`: The text or variable to print
- `sep`: Separator between multiple objects (default: space `' '`)
- `end`: What to print at the end (default: newline `\n`)
- `file`: Where to send the output (default: terminal)
- `flush`: Force the system to write the output immediately (default: `False`)

---

## 🔸 Basic Printing

```python
print("Hello, world!")
```
**Output:**
```
Hello, world!
```

---

## 🔸 Multiple Values and Separator

```python
print("Python", "is", "fun", sep="-")
```
**Output:**
```
Python-is-fun
```

---

## 🔸 No Newline (Using `end`)

```python
print("Hello", end=", ")
print("world!")
```
**Output:**
```
Hello, world!
```

---

## 🔸 Writing to a File

```python
text_file = open("hello.txt", "w")
print("Hello from Python!", file=text_file)
text_file.close()
```

- `"w"`: Write mode — creates or overwrites the file.
- `file=text_file`: Directs `print()` output into the file.
- Always use `.close()` to save and close the file.

---

## 🔸 Combining `print()` with `time.sleep()`

The `time` module lets us add delays between print statements.

### Countdown Timer
```python
import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")
```

---

### Typing Effect (Animated Text)
```python
import time

message = "Learning Python is fun!"
for char in message:
    print(char, end='', flush=True)
    time.sleep(0.1)
```

---

### Loading Animation
```python
import time

print("Loading", end='')
for _ in range(3):
    time.sleep(1)
    print('.', end='', flush=True)
print(" Done!")
```

---

### Simulated Chat
```python
import time

print("Ali: Hey, are you there?", end=' ')
time.sleep(2)
print("Sarah: Yeah, just saw your message.")
```

---

## 🧠 Summary of Skills

| Concept             | Description                                  |
|---------------------|----------------------------------------------|
| `print()` basics     | Output text or values                        |
| `end=`               | Control line endings                         |
| `sep=`               | Change separators between printed items      |
| `file=`              | Print to a file instead of the screen        |
| `flush=True`         | Forces immediate output display              |
| `time.sleep(seconds)`| Delay execution for timing effects           |


## 📁 Folder Structure 

```
python-print-tutorial/
│
├── README.md                
├── greetings_v1.py          # Writing to files 
├── greetings_v2.py          # Writing to files
├── product_number.py        # Writing integers to a files
├── input_print.py           # Ask a user name and then saves into a file
├── countdown_timer.py       # Timer with sleep
├── typing_effect.py         # Simulated typing
├── loading_dots.py          # Loading animation
└── chat_simulation.py       # Simulated conversation
```
