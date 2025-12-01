# 🔍 Common SQL Patterns in LeetCode

Frequently used patterns and techniques.

---

## 1. Finding Duplicates

```sql
SELECT column, COUNT(*) as count
FROM table_name
GROUP BY column
HAVING COUNT(*) > 1;
```

---

## 2. Running Totals

```sql
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM transactions;
```

---

## 3. Ranking with Ties

```sql
SELECT 
    name,
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) as rank
FROM students;
```

---

## 4. Finding Nth Highest

```sql
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET N-1;
```

---

## 5. Consecutive Dates/Numbers

```sql
WITH numbered AS (
    SELECT 
        date,
        ROW_NUMBER() OVER (ORDER BY date) as rn,
        DATE_SUB(date, INTERVAL ROW_NUMBER() OVER (ORDER BY date) DAY) as grp
    FROM table_name
)
SELECT MIN(date), MAX(date), COUNT(*) as consecutive_days
FROM numbered
GROUP BY grp
HAVING COUNT(*) >= 3;
```

---

## 6. Percentage Calculations

```sql
SELECT 
    category,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM table_name) as percentage
FROM table_name
GROUP BY category;
```

---

## 7. First/Last Record Per Group

```sql
SELECT *
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY group_id ORDER BY date DESC) as rn
    FROM table_name
) t
WHERE rn = 1;
```

---

## 8. Pivot Data

```sql
SELECT 
    id,
    MAX(CASE WHEN type = 'A' THEN value END) as value_a,
    MAX(CASE WHEN type = 'B' THEN value END) as value_b
FROM table_name
GROUP BY id;
```
