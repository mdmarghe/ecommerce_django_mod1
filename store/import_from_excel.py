import pandas as pd
from .models import Product  # Import your Product model

def import_products_from_excel(file_path):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')

        # Iterate through the rows of the DataFrame
        for index, row in df.iterrows():
            product = Product(
                name=row['Name'],
                price=row['Price'],
                digital=row['Digital'],
                producer=row['Producer'],
                denomination=row['Denomination'],
                grape_variety=row['Grape Variety'],
                crianza=row['Crianza']
            )
            product.save()

        print('Products imported successfully.')
    except Exception as e:
        print(f'Error importing products: {str(e)}')

if __name__ == "__main__":
    file_path = 'Products.xlsx'  # Replace with your Excel file path
    import_products_from_excel(file_path)
