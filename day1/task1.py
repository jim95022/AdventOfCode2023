# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?


class Solution:

    def get_sum(self, content: str) -> int:
        lines = content.split("\n")
        numbers = [self.__extract_number(line) for line in lines if line]
        return sum(numbers)

    def __find_first_line_digit(self, line: str) -> str:
        for char in line:
            if char.isdigit():
                return char
        raise Exception(f"{line} doesn't have digits")

    def __extract_number(self, line: str) -> int:
        first_digit = self.__find_first_line_digit(line)
        second_digit = self.__find_first_line_digit(line[::-1])
        return int(first_digit + second_digit)



if __name__ == "__main__":

    s = Solution()
    
    test_file = "test_input.txt"
    
    with open(test_file) as file:
        content = file.read()

    assert s.get_sum(content) == 142

    test_file = "input.txt"
    
    with open(test_file) as file:
        content = file.read()

    print(s.get_sum(content))

