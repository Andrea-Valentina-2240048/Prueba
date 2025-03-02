import numpy as np

# Total number of candidates
num_candidates = 30
total_votes = 5000

# Generate 30 random numbers that sum to 5000 (votes per candidate)
votes_per_candidate = np.random.multinomial(total_votes, np.ones(num_candidates) / num_candidates)

# Create an array of candidate numbers (1 to 30)
candidates = np.arange(1, num_candidates + 1)

# Sorting candidates by votes in descending order
sorted_indices = np.argsort(-votes_per_candidate)  # Negative sign to sort descending
sorted_candidates = candidates[sorted_indices]  # Reorder candidates
sorted_votes = votes_per_candidate[sorted_indices]  # Reorder votes

# Print results
print("\nVotes per candidate (before sorting):")
for candidate, votes in zip(candidates, votes_per_candidate):
    print(f"Candidate {candidate} received {votes} votes")

print("\nVotes per candidate (sorted from highest to lowest):")
for candidate, votes in zip(sorted_candidates, sorted_votes):
    print(f"Candidate {candidate} received {votes} votes")
