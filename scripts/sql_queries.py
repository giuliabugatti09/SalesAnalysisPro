import sqlite3
import pandas as pd

def create_database(df):
    """
    Cria um banco de dados SQLite em memória e insere os dados do DataFrame.
    """
    conn = sqlite3.connect(':memory:')
    df.to_sql('sales', conn, index=False, if_exists='replace')
    return conn

def run_queries(conn):
    """
    Executa consultas SQL no banco de dados.
    """
    cursor = conn.cursor()

    # Total de vendas por produto
    cursor.execute('''
    SELECT ProductID, SUM(Total) as TotalSales
    FROM sales
    GROUP BY ProductID
    ''')
    total_sales_by_product = cursor.fetchall()
    print("Total de Vendas por Produto:\n", total_sales_by_product)

    # Total de vendas por cliente
    cursor.execute('''
    SELECT CustomerID, SUM(Total) as TotalSales
    FROM sales
    GROUP BY CustomerID
    ''')
    total_sales_by_customer = cursor.fetchall()
    print("Total de Vendas por Cliente:\n", total_sales_by_customer)

    # Verificação de integridade dos dados
    cursor.execute('''
    SELECT *
    FROM sales
    WHERE Quantity <= 0 OR Total <= 0
    ''')
    inconsistent_data = cursor.fetchall()
    print("Dados Inconsistentes:\n", inconsistent_data)

if __name__ == "__main__":
    # Exemplo de uso
    url = 'https://raw.githubusercontent.com/giuliabugatti09/SalesAnalysisPro/main/data/sales_data.csv'
    df_sales = pd.read_csv(url)
    conn = create_database(df_sales)
    run_queries(conn)
