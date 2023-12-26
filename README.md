# Maximum Array Removal Cost
Author: [Jack Robbins](https://github.com/jackr276)

This is a simple program that finds the minimum cost in reducing an array's size to one element.

Sample Run:
Starting with: [4, 6, 8] 

1st Step:
  - Remove 4 and 6, cost = 4+6 = 10
  - Add 10 to the back of the array
  - Total cost is 10
  - Array is now [8, 10]

2nd Step:
  - Remove 8 and 10, cost = 10+8 = 18
  - Add 18 to the back of the array
  - Total cost is now 10 + 18 = 28
  - Array is now [18], one element long, no more steps

The program in this project does this for every possible removal order in order to find the lowest cost in reducing an array to one element in size.
