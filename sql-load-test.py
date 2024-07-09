

def get_query():
    return """
SELECT ID, Name, Age, Salary, Department, City, Country FROM loadtesttable WHERE Name like 'A%' AND Age BETWEEN 30 AND 40
"""
