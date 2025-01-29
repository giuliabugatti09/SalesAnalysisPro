import pandas as pd
def validate_data(df):
    """
    Valida a integridade dos dados em um DataFrame.
    """
    # Verificar valores nulos
    null_values = df.isnull().sum()
    print("Valores nulos em cada coluna:\n", null_values)

    # Verificar duplicatas
    duplicate_values = df.duplicated().sum()
    print("Número de linhas duplicadas:\n", duplicate_values)

    # Verificar consistência dos dados (por exemplo, valores negativos em 'Quantity' e 'Total')
    inconsistent_quantity = df[df['Quantity'] <= 0]
    inconsistent_total = df[df['Total'] <= 0]
    print("Inconsistências em 'Quantity':\n", inconsistent_quantity)
    print("Inconsistências em 'Total':\n", inconsistent_total)

    # Verificações adicionais
    if not inconsistent_quantity.empty or not inconsistent_total.empty:
        print("Dados inconsistentes encontrados.")
    else:
        print("Dados estão consistentes.")

    return null_values, duplicate_values, inconsistent_quantity, inconsistent_total

if __name__ == "__main__":
    # Exemplo de uso
    url = 'https://raw.githubusercontent.com/giuliabugatti09/SalesAnalysisPro/main/data/sales_data.csv'
    df_sales = pd.read_csv(url)
    validate_data(df_sales)

