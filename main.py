import os
import json
from src.pipeline import NL2SQLPipeline

def create_dummy_schema(path):
    """
    Creates a dummy schema based on the paper's Case Studies [cite: 153-179].
    Table 1: Sales (RevenueColumn, SaleDate, ProductName, RegionName, CustomerID)
    Table 2: Customers (ID, CustomerName)
    """
    schema = {
        "tables": [
            {
                "name": "Sales",
                "columns": [
                    {"name": "RevenueColumn", "type": "FLOAT"},
                    {"name": "SaleDate", "type": "DATE"},
                    {"name": "ProductName", "type": "VARCHAR"},
                    {"name": "RegionName", "type": "VARCHAR"},
                    {"name": "CustomerID", "type": "INT", "foreign_key": "Customers.ID"}
                ]
            },
            {
                "name": "Customers",
                "columns": [
                    {"name": "ID", "type": "INT", "primary_key": True},
                    {"name": "CustomerName", "type": "VARCHAR"}
                ]
            }
        ]
    }
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(schema, f, indent=2)
    print(f" Created dummy schema at {path}")

def main():
    schema_path = "data/schema_metadata.json"
    
    # 1. Setup Data
    if not os.path.exists(schema_path):
        create_dummy_schema(schema_path)

    # 2. Initialize Engine
    print(" Initializing NL2SQL Engine (LlamaEmbedder + Graph Metadata)...")
    try:
        engine = NL2SQLPipeline(schema_path=schema_path)
    except Exception as e:
        print(f"Error initializing pipeline: {e}")
        return

    # 3. Interactive Loop
    print("\n Context-Aware NL2SQL System Ready.")
    print("   Type 'exit' to quit.\n")
    
    while True:
        user_query = input(" Enter your question: ")
        if user_query.lower() in ['exit', 'quit']:
            break
            
        try:
            sql_result = engine.generate(user_query)
            print(f"\n Generated SQL:\n{sql_result}\n")
            print("-" * 50)
        except Exception as e:
            print(f" Error generating SQL: {e}")

if __name__ == "__main__":
    main()