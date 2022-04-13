src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def bigger_then_priv():
     result = []
     for i, val in enumerate(src):
          if i == 0:
               continue
          if val > src[i - 1]:
               result.append(val)
     yield result


print(*bigger_then_priv())
