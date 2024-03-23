import numpy as np

def sim(kp1, kp2):
    if not kp1 or not kp2:
        return 0
    dist = 0
    for p1, p2 in zip(kp1, kp2):
        dist += np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    return dist / len(kp1)