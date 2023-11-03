class solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        target_len = len(target)
        previous = 0
        for i in range(0, target_len):
            res += (['Push', 'Pop'])*(target[i] - previous- 1) + ['Push']
            previous = target[i]
        return res