def summary(scores):
    if not scores:
        raise ValueError("the scores list is empty")
    else:
        min = 100
        max = 0
        median = 0
        mean = 0
        for score in scores:
            if score < min:
                min = score
            if score > max:
                max = score
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
        res = {'min': min, 'max': max, 'mean': mean, 'median': median}
        return res
