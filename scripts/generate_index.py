#!/usr/bin/env python3
from pathlib import Path
import yaml

def generate_index():
    categories = [
        "Select",
        "Basic-Joins",
        "Basic-Aggregate-Functions",
        "Sorting-and-Grouping",
        "Advanced-Select-and-Joins",
        "Subqueries",
        "Advanced-String-Functions-Regex-Clause"
    ]
    
    content = "# 📑 Problem Index

"
    content += "Quick reference to all problems in this repository.

"
    content += "---

"
    
    base_path = Path(".")
    
    for category in categories:
        category_path = base_path / category
        if not category_path.exists():
            continue
        
        content += f"## {category.replace('-', ' ')}

"
        
        problem_folders = sorted([f for f in category_path.iterdir() if f.is_dir()])
        
        for problem_folder in problem_folders:
            yml_file = problem_folder / "problem.yml"
            if yml_file.exists():
                try:
                    with open(yml_file, 'r', encoding='utf-8') as f:
                        data = yaml.safe_load(f)
                        if data:
                            problem_num = data.get('problem_number', '?')
                            title = data.get('title', problem_folder.name)
                            difficulty = data.get('difficulty', 'Unknown')
                            solved = data.get('solved', False)
                            
                            status = "✅" if solved else "⬜"
                            content += f"{problem_num}. {status} [{title}]({category}/{problem_folder.name}/README.md) - **{difficulty}**
"
                except:
                    pass
        
        content += "
"
    
    with open("INDEX.md", "w", encoding='utf-8') as f:
        f.write(content)
    
    print("✅ INDEX.md generated successfully")


if __name__ == "__main__":
    generate_index()
