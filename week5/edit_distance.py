

def edit_distance(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)

    matrix = [[0 for i in range(len_s2 + 1)] for i in range(len_s1 + 1)]
    for i in range(len_s1+1):
        matrix[i][0] = i
    for i in range(len_s2+1):
        matrix[0][i] = i

    for i in range(1, len_s1+1):
        for j in range(1, len_s2+1):
            insertion = matrix[i][j-1] + 1
            deletion = matrix[i-1][j] + 1
            match = matrix[i-1][j-1]
            mismatch = matrix[i-1][j-1] + 1

            if s1[i-1] == s2[j-1]:
                matrix[i][j] = min(insertion, deletion, match)
            elif s1[i-1] != s2[j-1]:
                matrix[i][j] = min(insertion, deletion, mismatch)
    return int(matrix[len_s1][len_s2])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
