import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from solution import kurt, skew

# Generating random data (normal distribution for example purposes)
data = np.random.normal(loc=0, scale=1, size=1000)

# Create a histogram to visualize the distribution
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.histplot(data, kde=True)
plt.title('Histogram with KDE')

# Compute and print skewness and kurtosis
skewness = np.round(skew(data)['sk2'], 3)
kurtosis = np.round(kurt(data)['kurt2'], 3)
print(f"Skewness: {skewness}, Kurtosis: {kurtosis}")

# Create a boxplot to visualize skewness and kurtosis
plt.subplot(1, 2, 2)
sns.boxplot(data=data)
plt.title('Boxplot')

plt.tight_layout()
plt.show()
