"""
Bob loves to play with the pipelines, which are closed from one end. Bob gives you the pipeline with some queries Q. Each query contains:

Two integers X and N

If X=1, insert number Ninto the pipeline from the top • If X = 2, take out an integer that is occurring the most (i.e.

have the largest frequency in the pipeline) and remove its occurrence closest to the open end of the pipeline. If the frequency of more than one number is the same and largest, you should remove the number closest to the open end of the pipeline. In this case N = -1.

Return the list of elements that are removed during the X = 2 query. Example

Assumptions
-Q=6

⚫ query = [(1,2),(1,4), (1,3), (1,2), (2,-1),(2,-1)]

Approach

• After the first operation, the pipeline will be 2.

After the second operation, the pipeline will be 2, 4.

After the third operation, the pipeline will be 2, 4, and 3. After the fourth operation, the pipeline will be 2, 4, 3, and 2.

After the fifth operation, 2 will be removed as 2 occurs most times, and the pipeline will be 2, 4, 3.

After the sixth operation, 3 will be removed as 2, 4, and 3 occurs most times, but 3 is more close to the open side of

the pipeline, The pipeline will be: 2, 4. • Therefore, you print [2, 3] elements removed during the X =

2 query.
"""