
# Randomness Test
In a lottery game, there is a container which contains 50 balls numbered from 1 to 50. The lottery game consists in picking 10 balls out of the container, and ordering them in ascending order. Write a Python function which generates the output of a lottery game (it should return a list). Also describe which unit tests you could implement to test the output of your function.

# Time Spent
20 minutes

# Algorithm
Step 1 : Import the sample function from the random module
Step 2 : Generate a list of first 50 integers using the range function and typecast it to list
Step 3 : Pass the list in the sample function as the first argument and 10 as the second argument denoting 10 elements to be sampled at random from the list
Step 4 : Sort the resultant 10 numbers in ascending order using the sorted function
Step 5 : Print/Return the sorted list

# Test Ideas
Test 1 : Check if there are 10 elements returned
Test 2 : Check if all the ten elements returned are unique
Test 3 : Check if every single element is an integer
Test 4 : Check if every single integer is between 1 and 50 both inclusive