package main

import (
	"fmt"
)

// Define a hash map to store scores by student name
var scores map[string]int

func main() {
	// Initialize the hash map
	scores = make(map[string]int)

	// Add scores for students
	addScore("Alice", 85)
	addScore("Bob", 90)
	addScore("Charlie", 75)
	addScore("David", 95)
	addScore("Eve", 80)

	// Retrieve scores for students
	fmt.Println("Score for Alice:", getScore("Alice"))
	fmt.Println("Score for Bob:", getScore("Bob"))
	fmt.Println("Score for Charlie:", getScore("Charlie"))
	fmt.Println("Score for David:", getScore("David"))
	fmt.Println("Score for Eve:", getScore("Eve"))
}

// Function to add a score for a student
func addScore(name string, score int) {
	// Calculate hash code for the name
	hashCode := hash(name)

	// Store the score in the hash map
	scores[name] = score
}

// Function to retrieve the score for a student
func getScore(name string) int {
	// Retrieve the score from the hash map
	score := scores[name]
	return score
}

// Hash function
func hash(s string) int {
	// Simple hash function: sum ASCII values of characters
	hashCode := 0
	for _, c := range s {
		hashCode += int(c)
	}
	return hashCode
}
