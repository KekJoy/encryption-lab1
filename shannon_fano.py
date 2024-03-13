from typing import List



def shannon_fano_coding(odds: List[float], res: dict[float, str], prefix: str = ""):
    odds = sorted(odds, reverse=True)

    if len(odds) == 1:
        res[odds[0]] += prefix
        return

    total_sum = sum(odds)
    left, right = [], []
    left_sum, right_sum = 0, total_sum

    for odd in odds:
        if left_sum + odd <= right_sum - odd:
            left_sum += odd
            right_sum -= odd
            left.append(odd)
        else:
            right.append(odd)

    shannon_fano_coding(left, res, prefix + "0")
    shannon_fano_coding(right, res, prefix + "1")

    return res
