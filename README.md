# CP-TOOLKIT 🏆

## Overview

CP-TOOLKIT is a **CLI tool** that automates common tasks for **competitive programming** across multiple platforms:

- ✅ **LeetCode**
- ✅ **Codeforces**
- ✅ **CodeChef**

## Features

- 🚀 **Load sample test cases**
- 🛠 **Run and test locally**
- 📤 **Submit solutions directly**
- 📊 **View contest standings**
- 📅 **List upcoming contests**
- 🔔 **Mark contests for reminders**

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/CP-TOOLKIT.git
cd CP-TOOLKIT

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # (or venv\Scripts\activate on Windows)

# Install dependencies
pip install -r requirements.txt
```

## Configuration

### 1️⃣ Add an alias for easy usage

```bash
alias tool="python main.py"
```

### 2️⃣ Edit `config.py` to:

- Add your **credentials**
- Select the **platforms** you want to use

## Usage

```bash
# Load sample test cases for a problem
tool load <problem_link>

# Run and test your solution locally
tool test <file>

# Submit your solution
tool submit <file>

# View live standings
tool standings

# List upcoming contests
tool contests
```

## Dependencies

🧠 **Just 2 brain cells** (and Python libraries 😆)

