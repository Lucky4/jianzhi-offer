if __name__ == '__main__':
    capacity = 8

    w = [0, 2, 3, 4, 5]
    v = [0, 3, 4, 5, 6]
    dp = [0] * (capacity+1)

    for i in range(1, len(w)):
        for j in range(capacity, -1, -1):
            if w[i] > j:
                continue
            else:
                if dp[j] > dp[j-w[i]] + v[i]:
                    continue
                else:
                    dp[j] = dp[j-w[i]] + v[i]
        print dp