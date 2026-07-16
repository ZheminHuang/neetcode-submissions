class TimeMap:

    def __init__(self):
        self. store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]

        left = 0
        right = len(values)-1

        result =""

        while left<=right:
            mid = left+(right-left)//2

            stored_time,stored_value = values[mid]

            if stored_time <=timestamp:
                result= stored_value 
                left = mid+1

            else:
                right = mid -1

        return result
