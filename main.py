import numpy as np
import pandas as pd

def numpy_df():
    # Create a DataFrame with random data
    df = pd.DataFrame(np.random.randn(5, 3), columns = ['A', 'B', 'C'])

    # Print the DataFrame
    print('DataFrame:')
    print(df)

    # Convert DataFrame to NumPy array
    arr = df.to_numpy()

    # Print the NumPy array
    print('\nNumPy array:')
    print(arr)

numpy_df()