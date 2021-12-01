
import sys, random
from typing import List

alphabet: List[str] = [
  "\u0410, \u0430", # 
  "\u0411, \u0431", # 
  "\u0412, \u0432", # 
  "\u0413, \u0433", # 
  "\u0414, \u0434", # 
  "\u0415, \u0435", # 
  "\u0416, \u0436", # 
  "\u0417, \u0437", # 
  "\u0418, \u0438", # 
  "\u0419, \u0439", # 
  "\u041A, \u043A", # 
  "\u041B, \u043B", # 
  "\u041C, \u043C", # 
  "\u041D, \u043D", # 
  "\u041E, \u043E", # 
  "\u041F, \u043F", # 
  "\u0420, \u0440", # 
  "\u0421, \u0441", # 
  "\u0422, \u0442", # 
  "\u0423, \u0443", # 
  "\u0424, \u0444", # 
  "\u0425, \u0445", # 
  "\u0426, \u0446", # 
  "\u0427, \u0447", # 
  "\u0428, \u0448", # 
  "\u0429, \u0449", # 
  "\u042A, \u044A", # 
  "\u042B, \u044B", # 
  "\u042C, \u044C", # 
  "\u042D, \u044D", # 
  "\u042E, \u044E", # 
  "\u042F, \u044F"  # 
]


def main():
  indices = [i for i in range(len(alphabet))]
  if "--random" in sys.argv:
    random.shuffle(indices)
  
  loop = True

  while loop:
    if "--loop" not in sys.argv:
      loop = False

    for i in indices:
      print("{} - ".format(alphabet[i]), end="")
      upper = alphabet[i][0]
      lower = alphabet[i][3]
      letter = input()
      while letter not in [upper, lower, "skip"]:
        print("Incorrect")
        print("{} - ".format(alphabet[i]), end="")
        letter = input()




if __name__ == "__main__":
  main()
