# 8-Queens-HillClimbing
8-Queens puzzle implementation with Hill Climbing(Random Restart) Algorithm

## Input
Input of this algorithm is a list of integers from 0 to 7. Each integer indicates number of a row in the board. Index of each element in the list indicates number of the column. (There is only one queen in each column). For example:

```
initial_state = [0, 0, 0, 0, 0, 0, 0, 0]
```

##Output
Output will be a list of integers in which there is no two or more queens in the same horizontal or diagonal line of the board.
There is also a function names "board" which can draw the board with the locations of the queens based on the output list. For Example:

```
[6, 1, 3, 0, 7, 4, 2, 5]
```

