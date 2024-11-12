import numpy as np
import scipy
from sklearn.ensemble import RandomForestClassifier

# Display versions of the libraries
print("NumPy version:", np.__version__)
print("SciPy version:", scipy.__version__)
print("Scikit-learn version:", sklearn.__version__)

# Create a random forest classifier example
clf = RandomForestClassifier(n_estimators=10)
print("RandomForestClassifier is ready to use.")


