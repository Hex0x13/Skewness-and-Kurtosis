import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from solution import kurt, skew

# # Generating random data (normal distribution for example purposes)
# data = np.random.normal(loc=0, scale=1, size=1000)

# data.sort()
# print(data)
# # Create a histogram to visualize the distribution
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# sns.histplot(data, kde=True)
# plt.title('Histogram with KDE')

# # Compute and print skewness and kurtosis
# skewness = np.round(skew(data)['sk2'], 3)
# kurtosis = np.round(kurt(data)['kurt2'], 3)
# print(f"Skewness: {skewness}, Kurtosis: {kurtosis}")

# # Create a boxplot to visualize skewness and kurtosis
# plt.subplot(1, 2, 2)
# sns.boxplot(data=data)
# plt.title('Boxplot')

# plt.tight_layout()
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Provided data
data = [67, 63, 64, 57, 56, 55, 53, 53, 54, 54, 45, 45, 46, 47, 37, 23, 34, 44, 27, 44, 45, 34, 34, 15,
        23, 43, 16, 44, 36, 36, 35, 37, 24, 24, 14, 43, 37, 27, 36, 26, 25, 36, 26, 5, 44, 13, 33, 33, 17, 33]

# Plotting the histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=10, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Provided Data')
plt.grid(True)
plt.show()

# Calculating kurtosis
kurtosis_value = np.kurtosis(data)
print("Kurtosis:", kurtosis_value)
