class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp_dict:
            self.timestamp_dict[key] = {}

        self.timestamp_dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if timestamp <= 0:
            return ""

        if key in self.timestamp_dict:
            if timestamp in self.timestamp_dict[key]:
                return self.timestamp_dict[key][timestamp]
            else:
                return self.get(key, timestamp - 1)
        return ""