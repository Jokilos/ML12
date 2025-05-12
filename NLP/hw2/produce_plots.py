import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
df = pd.read_csv('test_results.csv')  # Replace with the actual path

df = df[df['iters'] > 0].copy()
df['score_per_iter'] = df['score'] / df['iters']
sns.set(style="whitegrid")
test_types = df['test_type'].unique()

for test_type in test_types:
    subset = df[df['test_type'] == test_type].copy()
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.barplot(data=subset, x='value', y='score', estimator='mean', errorbar='sd')
    plt.title(f'{test_type.upper()}: Avg Total Score by Value')
    plt.xlabel('Value')
    plt.ylabel('Average Score')
    
    plt.subplot(1, 2, 2)
    sns.barplot(data=subset, x='value', y='score_per_iter', estimator='mean', errorbar='sd')
    plt.title(f'{test_type.upper()}: Avg Score per Iter by Value')
    plt.xlabel('Value')
    plt.ylabel('Score / Iteration')

    plt.tight_layout()
    plt.savefig(f"plots/{test_type}_plot.png", dpi=300, bbox_inches='tight')
    plt.show()



