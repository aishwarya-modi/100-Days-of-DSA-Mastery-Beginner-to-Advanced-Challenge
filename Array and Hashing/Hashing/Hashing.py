# Define a hash table to store scores by student name
scores = {}

# Function to add a score for a student
def add_score(name, score):
    # Calculate hash code for the name
    hash_code = hash(name)
    
    # Store the score in the hash table
    scores[hash_code] = score

# Function to retrieve the score for a student
def get_score(name):
    # Calculate hash code for the name
    hash_code = hash(name)
    
    # Retrieve the score from the hash table
    score = scores.get(hash_code)
    return score

# Add scores for students
add_score("Alice", 85)
add_score("Bob", 90)
add_score("Charlie", 75)
add_score("David", 95)
add_score("Eve", 80)

# Retrieve scores for students
print("Score for Alice:", get_score("Alice"))
print("Score for Bob:", get_score("Bob"))
print("Score for Charlie:", get_score("Charlie"))
print("Score for David:", get_score("David"))
print("Score for Eve:", get_score("Eve"))
