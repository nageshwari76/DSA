from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(r) for r in grid)

        # try to partition in one orientation
        def check(mat):
            prefix_sum = 0
            seen = set()
            for i, row in enumerate(mat):
                prefix_sum += sum(row)
                suffix_sum = total - prefix_sum
                diff = prefix_sum - suffix_sum

                # direct equal
                if diff == 0:
                    return True

                # diff might equal a border or seen cell
                # check specific positions to maintain connectivity
                if diff == mat[0][0] or diff == mat[0][-1] or diff == row[0]:
                    return True
                if len(mat[0]) > 1 and i > 0 and diff in seen:
                    return True

                # record values for remove checks
                seen |= set(row)

            return False

        # top → bottom
        if check(grid):
            return True
        # bottom → top
        if check(grid[::-1]):
            return True

        # transpose to check left/right
        transposed = [list(col) for col in zip(*grid)]

        # left → right
        if check(transposed):
            return True
        # right → left
        if check(transposed[::-1]):
            return True

        return False