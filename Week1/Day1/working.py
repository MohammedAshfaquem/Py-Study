# 🧠 1. What is a Python Interpreter?
# A Python interpreter is a program that reads, parses, and executes your Python code.

# It converts human-readable Python code into machine-understandable instructions.

# ⚙️ 2. How the Python Interpreter Works: Step-by-Step
# Let’s say you run this simple Python file:
# print("Hello World")
# Here’s what happens inside the interpreter:

# ✅ Step 1: Lexical Analysis (Tokenizing)
# Python splits your code into tokens (smallest pieces).

# For example:
# print("Hello World")
# ⟶ keyword: print, string: "Hello World"
# ✅ Step 2: Parsing
# The interpreter checks the syntax (grammar) of your code.
# If you wrote something wrong (like missing a bracket), it throws a SyntaxError here.

# ✅ Step 3: Compilation to Bytecode
# The valid Python code is converted to bytecode — a lower-level, platform-independent representation.

# File hello.py is now compiled to bytecode like __pycache__/hello.cpython-311.pyc.

# ⚠️ Note: This is not machine code — it’s still not understood by your computer directly.

# ✅ Step 4: Interpretation by Python Virtual Machine (PVM)
# Now, the Python Virtual Machine (PVM) takes that bytecode and executes it line-by-line.

# This is where the actual program runs, and you see output like:
# Hello World
# 🛠️ Example in Action
# You write:
# a = 5
# print(a + b)
# Interpreter:

# Tokenizes → a, =, 5, b, =, 3, print, a + b

# Parses → Checks if the syntax is valid

# Compiles to bytecode

# PVM executes → Adds 5 and 3 → prints 8

# 🔁 Summary (with Analogy)
# Stage	What Happens	    Analogy
# Lexical Analysis      	Breaks code into words/tokens	Splitting a sentence into words
# Parsing	                Checks grammar	Making sure the sentence makes sense
# Compilation           	Converts to bytecode	Translating to a basic codebook
# Interpretation        	PVM runs it line by line	Reading from codebook and acting