def solution(dots):
    width = max(x[0] for x in dots) - min(x[0] for x in dots)
    height = max(y[1] for y in dots) - min(y[1] for y in dots)
    return width * height