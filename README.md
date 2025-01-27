# Secret Santa Project

## Introduction
This project automates the Secret Santa gift exchange process for the company. It assigns a Secret Child to each employee, ensuring the following constraints:
- An employee cannot be assigned themselves.
- No employee is assigned the same Secret Child as the previous year.


---

## Prerequisites
- Python 3.6 or higher
- Virtual environment tool (venv)

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/Sirvinayak-17/Secret-Santa-Game.git
cd Secret-Santa-Game
```

Step 2: Set Up Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

Step 3: Install the Dependencies

Install the required libraries (listed in requirements.txt) into your environment:
```
pip install -r requirements.txt
```

Step 4: Run the Project
	1.	Ensure the input files are in the data/ folder:
	•	employees.csv
	•	last_year.csv
	2.	Run 
 ```
python main.py
```

Step 5: Run the Tests
```
pytest tests/
```
 
