def find_dup_str(s, n):
    for index in range(len(s)-n+1):
        temp_string = s[index:index+n]
        updated_string = s[index+n:]
        if updated_string.find(temp_string) != -1 and len(updated_string) != 0:
            return temp_string
    return ""

program Find_Duplicate_String(s, n):
    for i from 0 to len(s) - 1:
        temp_s = s substring of length n starting at index i
        updated_s = s substring of length n starting at index n + i
        if updated_s contains any substring which matches temp_s:
            return temp


def find_max_dups(s):
    if len(s) > 1:
        for i in range(len(s)):
            if find_dup_str(s, i) != "":
                longest_dup = find_dup_str(s, i)
        return longest_dup
    else:
        return ""

while True:
    base_string = input("Enter a string to search through: ")
    substring_length = int(input("Enter a substring length: "))
    print(find_dup_str(base_string, substring_length))
    print(find_max_dups(base_string))
