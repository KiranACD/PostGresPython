
class QueryBuilder:
    
    @staticmethod
    def create_table_query(table_name, *columns):
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        for _, column in enumerate(columns):
            if _ == 0:
                query += f'{column}'
            else:
                query += f', {column}'
        query += ');'
        return query
    
    @staticmethod
    def create_column_name(column_name, data_type):
        return f'{column_name} {data_type}'