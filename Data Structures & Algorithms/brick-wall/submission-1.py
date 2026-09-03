class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ed={}
        for row in wall:
            p=0
            for bricks in row[:-1]:
                p += bricks
                ed[p] = ed.get(p,0)+1
        mx_ed = max(ed.values(),default=0)
        return len(wall) - mx_ed