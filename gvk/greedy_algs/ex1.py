class Segment:
    left: int
    right: int

    def __init__(self, left, right):
        self.left = left
        self.right = right


def get_right(segment):
    return segment.right


def check_segment(segment):
    if new_dot in range(segment.left, segment.right + 1):
        return False
    else:
        return True


n = int(input())
segments = []
for i in range(1, n + 1):
    left, right = map(int, input().split())
    segments.append(Segment(left, right))
segments = sorted(segments, key=get_right)
dots = []
while len(segments) != 0:
    new_dot = segments[0].right
    dots.append(new_dot)
    segments = list(filter(check_segment, segments))
print(len(dots))
output_string = ""
for dot in dots:
    output_string += str(dot) + " "
print(output_string.strip())
