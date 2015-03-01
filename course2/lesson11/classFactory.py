"""
classFactory: function to return tailored classes
CREATE TABLE user (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(50), email VARCHAR(50));
"""
import pprint

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data)==len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
                                
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
            
        def retrieve(self, curs, condition=None):
            """
            curs = curser on existing db connection
            condition = string of conditions / true of all received rows
            """
            query = "SELECT {0} FROM {1}".format(", ".join(self.cols), self.table)
            if condition is not None:
                query += " WHERE " + condition
            print(query)
            curs.execute(query)
            for row in curs.fetchall():
                yield row
            
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow