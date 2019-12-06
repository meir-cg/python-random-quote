import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  f=open("output.txt", "w+")

  last = len(quotes) -1
  i = 0

  while i < 2:
    rnd = random.randint(0, last)
    print(quotes[rnd], end="")
    f.write(quotes[rnd])
    i += 1
        


if __name__== "__main__":
  primary()
