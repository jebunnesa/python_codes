def find_permutation(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1
  print(char_frequency)


  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # print("here chr "+ str1[window_end])
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      # print(char_frequency[right_char])
      if char_frequency[right_char] == 0:
        print("i am in "+ right_char)
        matched += 1
        print(matched)

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      print("hei " + str1[window_end]+ " "+ str1[window_start])
      # print(str1[window_start])
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1
  print(char_frequency)

  return False


def main():
  # print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  # print('Permutation exist: ' + str(find_permutation("asabcdxabcdysada", "bcdyabcdx")))
  # print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
