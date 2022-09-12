# aoc2021
My quick and dirty solutions to the puzzles on AdventOfCode 2021.

```python
import oracledb as ora

# Connect to db
con = ora.OraConnection('n_il_read')

# Open a cursor
cur = con.cursor()

# Define sql statement
sql = r"""SELECT AR, MANAD, TO_CHAR(DATUM,'YYYY-MM-DD HH24:MI:SS') AS DATUM 
          FROM N_VS.T_IDS_INK_DATUM_D 
          WHERE AR = :ar AND MANAD = :manad ORDER BY DATUM"""

# Set bind variables
flt = dict(ar=2021, manad=5)

# Execute sql statement
cur.execute(sql, flt)

# Alternative A. Use Cursor.rowfactory() to modifiy output -> each row being output as a dictionary
cur.rowfactory = ora.rowfactory_dictionary(cur)

# Alternative B. Use Cursor.rowfactory() to modifiy output -> each row being output as a namedtuple
cur.rowfactory = ora.rowfactory_namedtuple(cur)

# Fetch result
res = cur.fetchall()
...
...
```
