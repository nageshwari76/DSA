from collections import deque
from typing import List

class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int
    ) -> List[List[int]]:

        m, n = len(image), len(image[0])

        clr = image[sr][sc]

        if clr == color:
            return image

        q = deque([(sr, sc)])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()

            image[r][c] = color

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and image[nr][nc] == clr
                ):
                    q.append((nr, nc))

        return image