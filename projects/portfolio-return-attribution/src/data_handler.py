import pandas as pd

def load_data():
    # Load initial data from a CSV or database
    # For simplicity, we'll create a dummy DataFrame
    data = pd.DataFrame({
        'Factor': ['ST Revisions', 'Flow', 'Sector'],
        'Portfolio': [1.0, 2.0, 3.0],
        'Linear': [0.5, 1.5, 2.5],
        'Interactions': [0.2, 0.3, 0.4],
        'Nonlinear': [0.1, 0.2, 0.3]
    })
    return data

def modify_data(data):
    # Modify data based on user inputs
    # Placeholder for actual modification logic
    return data