import numpy as np
import pandas as pd


print('creating dataframe using dictionary objects of different types')
df2 = pd.DataFrame(
    {
        "Col1": 1.0,
        "Col2": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(5)), dtype="float32"),
        "D": np.array([3] * 5, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train","trs"]),
        "F": "foo",
        "G": np.array([1,2,3,4,5]),
    }
)
print(df2)
print(df2.dtypes)
print(df2.head(2))#first two rows
print(df2.tail(3))#last three rows
print('conveting dataframe in to numpy array')
#NOTE THAT THIS IS COSTLIER SINCE DIFFERENTE DATA TYPES NEED TO BE CONVERTED INTO AN OBJECT USING
#CASTING
nparrayvalues=df2.to_numpy() 
print(nparrayvalues)
print('datatype:',nparrayvalues.dtype)
