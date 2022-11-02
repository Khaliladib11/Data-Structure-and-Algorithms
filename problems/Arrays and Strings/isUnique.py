#is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
# cannot use additional data structures?


def isUnique(str):
    for i in range(len(str)):
        count = 0
        for j in range(len(str)):
            if str[i] == str[j]:
                count += 1
                if count > 1:
                    return False
    return True



if __name__ == '__main__':

    str_input = 'khali'
    print(isUnique(str_input))
