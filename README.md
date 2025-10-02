# Database Systems – Practical Exam (Practice Test)

**Course:** Computer Programming and Database Systems  
**Academic Year:** 2024–2025, Term II   

In this exam we were provided with a **MySQL database** with some connection parameters:
The database contained two main tables:

### 1. `SourceText(position, symbol)`
Represents a sequence of characters (`symbol`) with their position in the sequence.  
- Example: `(12, 'B')` → character **'B'** is at position **12**.

### 2. `Substitute(symbol, replacement)`
Represents substitution rules.  
- Each row specifies that any occurrence of a given `symbol` should be replaced with the string in `replacement`.  
- Example: `(C, 'dca')` means **replace 'C' with 'dca'**.

## Goal of the Exam
Apply all substitution rules from `Substitute` to the sequence represented by `SourceText`.  

- The resulting sequence must be stored in a new table called:  
  **`ResultText(position, symbol)`**  
- `ResultText` must contain the sequence of all characters **after applying the substitutions**.  
- The **order of symbols** must be preserved, both from the original `SourceText` and within each replacement string.  

## Example

### Input Tables
**SourceText**
| position | symbol |
|----------|--------|
| 1        | H      |
| 2        | F      |
| 3        | G      |
| 4        | J      |
| 5        | D      |
| 6        | F      |

**Substitute**
| symbol | replacement |
|--------|-------------|
| F      | abb         |
| J      | cda         |
| G      | cec         |

### Output Table
**ResultText**
| position | symbol |
|----------|--------|
| 1        | H      |
| 2        | a      |
| 3        | b      |
| 4        | b      |
| 5        | c      |
| 6        | e      |
| 7        | c      |
| 8        | c      |
| 9        | d      |
| 10       | a      |
| 11       | D      |
| 12       | a      |
| 13       | b      |
| 14       | b      |


- The positions in `ResultText` must **preserve the order** in `SourceText` and in each `replacement`.  
- Both **Python code** and **SQL scripts** (if any) must be delivered.  
- Delivery platform: **Blackboard (Assessments section)**.  



## Tools used:
- **Python** (for DB connection and data processing)  
- **MySQL** (database engine)  
- **DBeaver** (GUI client for validating tables and running queries interactively)  
