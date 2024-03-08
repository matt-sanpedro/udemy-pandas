# in Pandas, data is organized in tabular data known as a Pandas DataFrame
# it is recommenmded and optimal to have one datatype per column, different datatype in column can restrict functionality and cause severe problems

"""
ChatGPT: saving time coding

- proficient python/pandas coder
- can help to bugfix, improve and write code
- does not replace coding skills, requires human oversight and intervention
- can analyze code and provide help
"""
# import pandas library and load csv
import pandas as pd
titanic = pd.read_csv("titanic.csv")
print(titanic)

# reading from file system requires use of r prefix
sales = pd.read_csv(r"C:\Tools\python\courses\udemy-pandas\section-01-intro\sales.csv")
print(sales)

# display settings: output max rows at 60 by default (will print all rows if less than 60)
print(pd.options.display.max_rows)

# display settings: output min rows at 10 by default (will print 10 rows if more than 60)
print(pd.options.display.min_rows)

# set min rows to 20 and print titanic
pd.options.display.min_rows = 20
print(titanic)

# head: first 5 rows by default
print(titanic.head(10))

# tail: last 5 rows by default
print(titanic.tail(10))
