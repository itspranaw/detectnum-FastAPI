import pickle
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load data
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)

# Convert data to numpy arrays and ensure proper types
X = X.astype('float32')
y = y.astype('int32')

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier(n_jobs=-1, random_state=42)
clf.fit(X_train, y_train)

# Print accuracy
print(f"Model accuracy: {clf.score(X_test, y_test):.4f}")

# Save the model
with open('mnist_model.pkl', 'wb') as f:
    pickle.dump(clf, f)