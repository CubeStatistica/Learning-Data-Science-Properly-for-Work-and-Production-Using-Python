# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
import sys

# Prints current Python version
print("Current version of Python is ", sys.version)
print("working")


text = "X-DSPAM-Confidence:    0.8475"


idx_start = text.find(':')
print("idx_start:", idx_start)

num = text[idx_start+1:].strip()
print(type(num), num)

num = float(num)
print(type(num), num)