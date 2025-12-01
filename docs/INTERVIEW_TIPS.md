# 🎯 SQL Interview Tips

Tips and best practices for SQL interviews.

---

## General Tips

1. **Understand the Problem First**
   - Read the problem statement carefully
   - Identify input and output requirements
   - Note any edge cases

2. **Plan Your Approach**
   - Break down complex problems into steps
   - Consider which SQL features to use
   - Think about performance implications

3. **Write Clean Code**
   - Use meaningful aliases
   - Format your SQL for readability
   - Add comments for complex logic

---

## Common Patterns

### Pattern 1: Self-Join
Used when comparing rows within the same table.

### Pattern 2: Aggregation with GROUP BY
Essential for summary statistics.

### Pattern 3: Window Functions
Powerful for ranking and running calculations.

### Pattern 4: Multiple CTEs
Break complex queries into manageable parts.

---

## Performance Tips

- Use appropriate JOINs (avoid CROSS JOIN unless necessary)
- Filter early with WHERE clauses
- Use indexes (when designing schema)
- Consider using EXISTS instead of IN for large datasets
- Avoid SELECT * in production

---

## Common Mistakes to Avoid

- Forgetting GROUP BY with aggregate functions
- Missing NULL handling
- Incorrect JOIN conditions
- Not considering duplicate rows
- Forgetting to ORDER BY when needed

---

## Testing Your Solution

1. Test with provided examples
2. Consider edge cases:
   - Empty tables
   - NULL values
   - Duplicate data
   - Single row scenarios

---

## Time Management

- Easy problems: 5-10 minutes
- Medium problems: 15-25 minutes
- Hard problems: 30-45 minutes

Don't spend too much time on one problem!
