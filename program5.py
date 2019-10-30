
def reverse_ans(x):
  sri = x.split()
  sri.reverse()
  return " ".join(sri)

# test code
question = input("Enter a sentence: ")
print (reverse_ans(question))
