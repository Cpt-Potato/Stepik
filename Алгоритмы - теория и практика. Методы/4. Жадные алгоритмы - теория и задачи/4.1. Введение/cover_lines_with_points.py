segments = [list(map(int, input().split())) for _ in range(int(input()))]
segments.sort(key=lambda x: x[1])

res = [segments[0][-1]]
for segment in segments:
    if res[-1] <= segment[0] and segment[0] not in res:
        res.append(segment[-1])

print(len(res))
print(*res)
