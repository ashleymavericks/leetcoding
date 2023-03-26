"""
Two players play a game with tiles that have integers written on them. The tile arranged in a row. In each turn, the current player removes one tile from eithe ends of the row. They do that until all tiles are removed. The score of a player sum of integers from tiles that the player removed. Assuming that the first play what is the maximum difference between the score of the first player and the the second player.

Knowing that the two players are playing optimally to maximize their scores, y is to calculate the maximum difference between the score of the first player a score of the second player.

Consider the following example -> Given an integer array Tiles of length N = 4 [3, 1, 100, 5)

The initial array is [3, 1, 100, 5]. 
So, the optimal way:

The first player takes the first element of the array. So, his score is 3 so far, and remaining elements are: [1, 100, 5]. 
The second player takes the last element of the remaining array. So, his score far 5, and the remaining elements are: [1, 100].
The first player takes the last element of the array. So, his score is 103 so far, remaining elements are: [1].
The second player takes the remaining element in the array. So, his score is 6

The maximum difference between the score of the first player and the second player is 103 - 6 = 97. Thus, the answer is 97.
"""


def solve(N, Tiles):
    DP = [[0]*N for _ in range(N)]
    for i in range(N):
        DP[i][i] = Tiles[i]
    for k in range(1, N):
        for i in range(N-k):
            j = i+k
            DP[i][j] = max(Tiles[i] - DP[i+1][j], Tiles[j] - DP[i][j-1])
    return DP[0][N-1]
