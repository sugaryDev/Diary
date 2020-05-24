import database.Database as database
import match_mod.CalculatorPFC as calculator
import match_mod.Analyze as analyze
import database.DatabaseExecutor as de

calculator = calculator.CalculatorPFC
database = database.Database("database/database.db")
analyze = analyze.Analyze("database/database.db")
# 10, 3, 5, 7, 15
de = de.DatabaseExecutor("database/database.db")
print(database.data_request('*'))
de.insert_records("10/10/10", "5", "ok")

"""
database:
(1, '10/10/10', 10.0, 'ok')
(2, '10/10/10', 3.0, 'bad')
(3, '10/10/10', 5.0, 'ok')
(4, '10/10/10', 7.0, 'bad')
(5, '11/10/10', 15.0, 'bad')
"""
