# IE2-Triangle

This repository contains the template code for In-Class Exercise 2 on Unit Testing. The exercise focuses on writing **unit tests**, assessing **test effectiveness**, and analyzing **code coverage**.

**Note:** The following instructions use Python 3. Ensure you are using the correct command (`python3` or `python`) based on your system.

---

## Installation
We recommend using a **virtual environment** (Python venv or Conda) to install the required dependencies.

### **Preferred Python Version**: **Python 3.8+**

### **Steps to Install**:
1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
2. Test the setup by running:
   ```bash
   cd test_suit
   python3 -m test_triangle
   ```
3. Test the initial test suite by running:
   ```bash
   ./test.sh
   ```

For more details, refer to:
- [Pytest Documentation](https://pypi.org/project/pytest/)
- [Unittest Documentation](https://docs.python.org/3/library/unittest.html)

---

## Control Flow Graph (CFG) Analysis
Follow these steps (**Ubuntu/Linux**) to generate CFG:

### **Step 1: Install Dependencies**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip graphviz
pip3 install py2cfg --user
```

### **Step 2: Verify Installation (if `py2cfg` is not found)**
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### **Step 3: Generate the CFG**
```bash
cd test_suit/
py2cfg isTriangle.py
```
A **`.svg` file** will be generated. Open it in a browser to visualize the control flow.

---

### **Task:**
1. Identify execution flow for:
   - **Normative Cases**: Equilateral, Isosceles, and Scalene triangles.
   - **Exceptional Cases**: Invalid sides and Triangle inequality violations.
2. Submit your findings in a **PDF file (`cfg_analysis.pdf`)**.

---
## Testing & Analysis

You need to create three test suites in the **`test_suit/`** folder to analyze different coverage metrics.

### **Statement Coverage**
1. Create `test_statementCoverage.py`.
2. Run:
   ```bash
   ./statement_coverage.sh
   ```
3. Aim for **75% or higher** statement coverage.

### **Decision (Branch) Coverage**
1. Create `test_decisionCoverage.py`.
2. Run:
   ```bash
   ./decision_coverage.sh
   ```
3. Aim for **75% or higher** decision coverage.

### **Coverage Analysis**
- We use the **Coverage** tool to analyze statement and decision coverage.
- View reports in `test_suit/statement_html/index.html` and `test_suit/decision_html/index.html`.
- Read more: [Coverage.py Documentation](https://coverage.readthedocs.io/en/7.2.7/)

---

## **Automated Test Generation using Fuzzing**

Fuzz testing generates **random inputs** to find edge cases. You will use **Faker** or **python-fuzz** to generate test cases for `isTriangle.py`.

### **Step 1: Install Faker**
```bash
pip install faker
```

### Step 2: Implement a test suite **test_fuzzTesting.py**

### **Step 3: Compare Coverage of Manual vs. Fuzz Testing**
Run **manual tests**:
```bash
coverage run --branch -m unittest discover
coverage report -m
```
Run **fuzz testing**:
```bash
coverage run --branch -a test_fuzzTesting.py
coverage report -m
```
Combine both results and analyze whether fuzz testing improves coverage.
Generate an HTML report for detailed analysis:
```bash
coverage html
```
Open `htmlcov/index.html` to review coverage metrics.

**Note:** Since fuzz testing generates **random** values, different runs will produce different results. Focus on comparing general **coverage improvements** rather than specific percentages.

---

## Additional Readings: Mutation Testing (Optional)

Mutation testing measures how well a test suite detects small modifications (mutants) in the code. While not required, you can explore mutation testing using the **MutPy** tool.

### **Mutation Testing Setup**
1. Create `test_mutationAdequate.py`.
2. Run:
   ```bash
   ./mutation.sh
   ```
3. Inspect generated mutants in `mutation_output.log` in `test_suit/`.

### **Mutation Report Analysis**
- View the report in `test_suit/mutation_report.html/index.html`.
- Mutants labeled **“killed”** were detected by tests.
- Mutants labeled **“survived”** were not detected, meaning tests need improvement.
- Read more: [MutPy Documentation](https://github.com/mutpy/mutpy)

---

## Troubleshooting
**Issue: `py2cfg` not found?**
```bash
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Issue: `isAlive()` error from MutPy?**
1. Open `utils.py` in the MutPy installation folder.
2. Change `if self.isAlive():` to `if self.is_alive():`.

---

This repository provides a structured approach to **unit testing, code coverage, and automated test generation**. If you have any issues, refer to the provided documentation links or reach out for assistance.

Happy testing! 

