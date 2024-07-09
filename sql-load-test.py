

def get_query():
    return """
SELECT ID, Name, Age, Salary, Department, City, Country FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS R FROM loadtesttable) AS ranked WHERE R <= 5
"""
