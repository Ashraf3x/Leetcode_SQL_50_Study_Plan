# 📚 SQL Cheat Sheet

Quick reference for common SQL patterns used in LeetCode problems.

---

## Basic SELECT

```sql
SELECT column1, column2 
FROM table_name 
WHERE condition;
```

---

## JOINs

### INNER JOIN
```sql
SELECT a.*, b.*
FROM table_a a
INNER JOIN table_b b ON a.id = b.id;
```

### LEFT JOIN
```sql
SELECT a.*, b.*
FROM table_a a
LEFT JOIN table_b b ON a.id = b.id;
```

---

## Aggregate Functions

```sql
SELECT 
    COUNT(*) as total,
    SUM(column) as sum_value,
    AVG(column) as avg_value,
    MAX(column) as max_value,
    MIN(column) as min_value
FROM table_name
GROUP BY category;
```

---

## Window Functions

```sql
SELECT 
    column,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY value) as row_num,
    RANK() OVER (ORDER BY value DESC) as rank,
    DENSE_RANK() OVER (ORDER BY value DESC) as dense_rank
FROM table_name;
```

---

## Subqueries

```sql
SELECT *
FROM table_name
WHERE id IN (
    SELECT id 
    FROM another_table 
    WHERE condition
);
```

---

## Common Table Expressions (CTE)

```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT *
FROM cte_name;
```

---

## String Functions

```sql
SELECT 
    CONCAT(first_name, ' ', last_name) as full_name,
    UPPER(name) as uppercase,
    LOWER(name) as lowercase,
    SUBSTRING(name, 1, 3) as first_three,
    LENGTH(name) as name_length
FROM table_name;
```

---

## Date Functions

```sql
SELECT 
    DATE(datetime_column) as date_only,
    YEAR(date_column) as year,
    MONTH(date_column) as month,
    DAY(date_column) as day,
    DATEDIFF(date1, date2) as date_difference
FROM table_name;
```

---

## CASE Statements

```sql
SELECT 
    column,
    CASE 
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        ELSE default_result
    END as category
FROM table_name;
```
