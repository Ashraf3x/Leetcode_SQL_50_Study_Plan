import os
from pathlib import Path


PROBLEMS = {
    "Select": [
        ("Recyclable and Low Fat Products", "Easy"),
        ("Find Customer Referee", "Easy"),
        ("Big Countries", "Easy"),
        ("Article Views I", "Easy"),
        ("Invalid Tweets", "Easy"),
    ],
    "Basic-Joins": [
        ("Replace Employee ID With The Unique Identifier", "Easy"),
        ("Product Sales Analysis I", "Easy"),
        ("Customer Who Visited but Did Not Make Any Transactions", "Easy"),
        ("Rising Temperature", "Easy"),
        ("Average Time of Process per Machine", "Easy"),
        ("Employee Bonus", "Easy"),
        ("Students and Examinations", "Easy"),
        ("Managers with at Least 5 Direct Reports", "Medium"),
        ("Confirmation Rate", "Medium"),
    ],
    "Basic-Aggregate-Functions": [
        ("Not Boring Movies", "Easy"),
        ("Average Selling Price", "Easy"),
        ("Project Employees I", "Easy"),
        ("Percentage of Users Attended a Contest", "Easy"),
        ("Queries Quality and Percentage", "Easy"),
        ("Monthly Transactions I", "Medium"),
        ("Immediate Food Delivery II", "Medium"),
        ("Game Play Analysis IV", "Medium"),
    ],
    "Sorting-and-Grouping": [
        ("Number of Unique Subjects Taught by Each Teacher", "Easy"),
        ("User Activity for the Past 30 Days I", "Easy"),
        ("Product Sales Analysis III", "Medium"),
        ("Classes With at Least 5 Students", "Easy"),
        ("Find Followers Count", "Easy"),
        ("Biggest Single Number", "Easy"),
        ("Customers Who Bought All Products", "Medium"),
    ],
    "Advanced-Select-and-Joins": [
        ("The Number of Employees Which Report to Each Employee", "Easy"),
        ("Primary Department for Each Employee", "Easy"),
        ("Triangle Judgement", "Easy"),
        ("Consecutive Numbers", "Medium"),
        ("Product Price at a Given Date", "Medium"),
        ("Last Person to Fit in the Bus", "Medium"),
        ("Count Salary Categories", "Medium"),
    ],
    "Subqueries": [
        ("Employees Whose Manager Left the Company", "Easy"),
        ("Exchange Seats", "Medium"),
        ("Movie Rating", "Medium"),
        ("Restaurant Growth", "Medium"),
        ("Friend Requests II: Who Has the Most Friends", "Medium"),
        ("Investments in 2016", "Medium"),
        ("Department Top Three Salaries", "Hard"),
    ],
    "Advanced-String-Functions-Regex-Clause": [
        ("Fix Names in a Table", "Easy"),
        ("Patients With a Condition", "Easy"),
        ("Delete Duplicate Emails", "Easy"),
        ("Second Highest Salary", "Medium"),
        ("Group Sold Products By The Date", "Easy"),
        ("List the Products Ordered in a Period", "Easy"),
        ("Find Users With Valid E-Mails", "Easy"),
    ],
}

# Additional folders
ADDITIONAL_FOLDERS = [
    "templates",
    "scripts",
    "tests",
    "data",
    "docs",
    "assets/badges",
    ".github/workflows",
]


def create_readme_template(problem_name, difficulty, problem_number):
    return f"""# {problem_name}

**Difficulty:** {difficulty}

---

## 📋 Problem Statement

[Add LeetCode problem description here]

---

## 💡 Hints

<details>
<summary>Click to reveal hints</summary>

### Hint 1
Think about...

### Hint 2
Consider using...

### Hint 3
Remember that...

</details>

---

## ✍️ Solution Explanation

[Add detailed explanation here]

### Approach

1. Step 1
2. Step 2
3. Step 3

### Key Points

- Point 1
- Point 2

---

## 💻 SQL Solution

```sql
-- Solution will be here
SELECT * FROM table_name;
```

---

## 🔗 LeetCode Link

[Problem Link](#)

---

## 📊 Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)
"""


def create_solution_template():
    return """-- SQL Solution
-- Write your MySQL query statement below

"""


def create_problem_yml(problem_name, difficulty, problem_number):
    return f"""problem_number: {problem_number}
title: "{problem_name}"
difficulty: {difficulty}
category: SQL
tags:
  - Database
  - SQL
leetcode_link: ""
solved: false
date_solved: null
notes: ""
"""


def slugify(text):
    return text.replace(" ", "-").replace(":", "").replace("'", "")


def create_structure():
    base_path = Path(".")
    
    print("🚀 Starting LeetCode SQL 50 Repository Setup...\n")
    
    # Create additional folders
    print("📁 Creating additional folders...")
    for folder in ADDITIONAL_FOLDERS:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ Created: {folder}")
    
    for folder in ["data", "tests"]:
        gitkeep_path = base_path / folder / ".gitkeep"
        gitkeep_path.touch()
    
    print("\n📚 Creating problem folders and files...\n")
    
    problem_counter = 1
    
    for category, problems in PROBLEMS.items():
        category_path = base_path / category
        category_path.mkdir(exist_ok=True)
        
        print(f"📂 {category}/")
        
        for problem_name, difficulty in problems:
            folder_name = f"{problem_counter:02d}-{slugify(problem_name)}"
            problem_path = category_path / folder_name
            problem_path.mkdir(exist_ok=True)
            
            readme_path = problem_path / "README.md"
            readme_path.write_text(create_readme_template(problem_name, difficulty, problem_counter), encoding='utf-8')
            
            solution_path = problem_path / "solution.sql"
            solution_path.write_text(create_solution_template(), encoding='utf-8')
            
            yml_path = problem_path / "problem.yml"
            yml_path.write_text(create_problem_yml(problem_name, difficulty, problem_counter), encoding='utf-8')
            
            print(f"   ✓ {problem_counter:02d}. {problem_name} ({difficulty})")
            
            problem_counter += 1
    
    print("\n📄 Creating root-level files...")
    
    progress_content = f"""# 📈 Progress Tracker

## Overall Progress

**Solved:** 0 / 50 (0%)

---

## By Category

| Category | Solved | Total | Progress |
|----------|--------|-------|----------|
| Select | 0 | {len(PROBLEMS['Select'])} | 0% |
| Basic Joins | 0 | {len(PROBLEMS['Basic-Joins'])} | 0% |
| Basic Aggregate Functions | 0 | {len(PROBLEMS['Basic-Aggregate-Functions'])} | 0% |
| Sorting and Grouping | 0 | {len(PROBLEMS['Sorting-and-Grouping'])} | 0% |
| Advanced Select and Joins | 0 | {len(PROBLEMS['Advanced-Select-and-Joins'])} | 0% |
| Subqueries | 0 | {len(PROBLEMS['Subqueries'])} | 0% |
| Advanced String Functions | 0 | {len(PROBLEMS['Advanced-String-Functions-Regex-Clause'])} | 0% |

---

*Last updated: {Path.cwd()}*
"""
    (base_path / "PROGRESS.md").write_text(progress_content, encoding='utf-8')
    print("   ✓ PROGRESS.md")
    
    index_content = """# 📑 Problem Index

Quick reference to all problems in this repository.

---

"""
    problem_counter = 1
    for category, problems in PROBLEMS.items():
        index_content += f"## {category.replace('-', ' ')}\n\n"
        for problem_name, difficulty in problems:
            folder_name = f"{problem_counter:02d}-{slugify(problem_name)}"
            index_content += f"{problem_counter}. [{problem_name}]({category}/{folder_name}/README.md) - **{difficulty}**\n"
            problem_counter += 1
        index_content += "\n"
    
    (base_path / "INDEX.md").write_text(index_content, encoding='utf-8')
    print("   ✓ INDEX.md")
    
    contributing_content = """# 🤝 Contributing Guidelines

Thank you for your interest in contributing!

## How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## Guidelines

- Follow the existing folder structure
- Include detailed explanations in README files
- Test your SQL solutions
- Update PROGRESS.md if solving new problems

---

Happy Contributing! 🚀
"""
    (base_path / "CONTRIBUTING.md").write_text(contributing_content, encoding='utf-8')
    print("   ✓ CONTRIBUTING.md")
    

    
    print("\n✅ Repository structure created successfully!")
    print(f"\n📊 Total problems created: {problem_counter - 1}")
    print("\n🎯 Next steps:")
    print("   1. Run: git add .")
    print("   2. Run: git commit -m 'feat: Initialize repository structure with all 50 problems'")
    print("   3. Run: git push")
    print("\n🚀 Happy coding!")


if __name__ == "__main__":
    create_structure()