def summary(scores):
    if not scores:
        raise ValueError("the scores list is empty")
    else:
        min_val = 100
        max_val = 0
        median = 0
        mean = 0
        for score in scores:
            min_val = min(score, float(min_val))
            max_val = max(score, float(max_val))
            mean = mean + score
        mean = mean / len(scores)
        scores.sort()
        n = len(scores)
        if n % 2 == 0:
            median = (scores[n//2 - 1] + scores[n//2]) / 2
        else:
            median = scores[n//2]
        mean = round(mean, 2)
        median = round(median, 2)
        res = {'min': min_val, 'max': max_val, 'mean': mean, 'median': median}
        return res
