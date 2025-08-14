# read the context of input.txt
with open("input.txt", "r") as infile:
  contents = infile.read()
  
# count the number of words
word_count = len(contents.split())

# convert all text to uppercase
uppercase_text = contents.upper()

#writes processed text and word count to output.txt
with open("output.txt", "w") as outfile:
  outfile.write("PROCESSED TEXT:\n")
  outfile.write(uppercase_text + "/n")
  outfile.write(f"\nWORD COUNT: {word_count}\n")
  
# print success message
print("✅ output.txt has been created successfully!")
