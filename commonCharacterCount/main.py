# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def countChar(s, c):
    count = 0
    for i in range(len(s)):
        if c == s[i]:
            count += 1

    return count


def solution(s1, s2):
    counted_or_not = []
    count = 0
    determiner = 0
    for c in s1:
        if c in s2 and c not in counted_or_not:
            determiner = min(countChar(s1, c), countChar(s2, c))
            count += determiner
            counted_or_not.append(c)

    return count




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution("a", "aaa"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
