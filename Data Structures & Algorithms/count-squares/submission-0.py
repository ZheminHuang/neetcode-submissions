class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.counts[(x,y)]+=1


    def count(self, point: List[int]) -> int:

        px,py = point

        result = 0

        for (x,y), diagonal_count in self.counts.items():

            if (x==px or abs(x-px)!=abs(y-py)):
                continue
            
            corner1 = (x,py)
            corner2 = (px,y)

            result += (
                diagonal_count
                * self.counts.get(corner1, 0)
                * self.counts.get(corner2, 0)
            )


        
        return result
        
