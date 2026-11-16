# Group CLI Toolkit

A simple Python command-line toolkit featuring a Fibonacci sequence generator and a JSON-based note manager.

## 🛠️ Included Tools

- **Fibonacci CLI (`fib.py`):** Generates Fibonacci numbers from the command line.
- **Note Manager (`note.py`):** Reads, writes, and manages quick notes saved locally in a JSON file.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ehimenkenneth/DSA-CLI-TOOLs.git
   cd DSA-CLI-TOOLs
   ```
2. *(Optional)* Set up a virtual environment if you add external packages later:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## 💻 Usage

### Fibonacci Tool
Run the script to generate Fibonacci numbers:
```bash
python fib.py 10
```

### Note Tool
Read or add notes stored in JSON:
```bash
# Write a new note
python note.py add "Finish the CLI README"

# Read all saved notes
python note.py list
```
*(Update the flags/arguments above to match how your scripts currently take inputs.)*

## 👥 Team
- **Member 1** – [@github-handle](https://github.comgithub-handle)
- **Member 2** – [@github-handle](https://github.comgithub-handle)
- **Member 3** – [@github-handle](https://github.comgithub-handle)

## 🤝 Contributing
1. Pull the latest changes (`git pull origin main`).
2. Create a branch for your feature (`git checkout -b add-new-tool`).
3. Commit and push your code, then open a Pull Request.

## How It Works
1. The program prompts the user to enter two comma-separated integers (for example, `0, 1` or `5, 8`).
2. It validates the input using `split(',')` and a `try/except` block to catch invalid text or missing numbers.
3. Once valid integers are confirmed, it prints the initial two numbers and recursively calculates the next 10 numbers until 12 terms are displayed.
