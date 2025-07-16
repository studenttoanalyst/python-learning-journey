# Histogram of Test Scores
# Show the distribution of test scores.
Scores = [50, 60, 65, 70, 70, 75, 80, 85, 90, 95, 100]
import matplotlib.pyplot as plt
plt.hist(Scores,bins=5)
plt.title("HISTOGRAM")
plt.xlabel("scores")
plt.ylabel("Frequency")
plt.show()