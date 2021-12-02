
import sys, random, codecs
from typing import List


alphabet: List[List[str]] = [
  ["\u0410", "\u0430"], # А
  ["\u0411", "\u0431"], # Б
  ["\u0412", "\u0432"], # В
  ["\u0413", "\u0433"], # Г
  ["\u0414", "\u0434"], # Д
  ["\u0415", "\u0435"], # Е
  ["\u0416", "\u0436"], # Ж
  ["\u0417", "\u0437"], # З
  ["\u0418", "\u0438"], # И
  ["\u0419", "\u0439"], # Й
  ["\u041A", "\u043A"], # К
  ["\u041B", "\u043B"], # Л
  ["\u041C", "\u043C"], # М
  ["\u041D", "\u043D"], # Н
  ["\u041E", "\u043E"], # О
  ["\u041F", "\u043F"], # П
  ["\u0420", "\u0440"], # Р
  ["\u0421", "\u0441"], # С
  ["\u0422", "\u0442"], # Т
  ["\u0423", "\u0443"], # У
  ["\u0424", "\u0444"], # Ф
  ["\u0425", "\u0445"], # Х
  ["\u0426", "\u0446"], # Ц
  ["\u0427", "\u0447"], # Ч
  ["\u0428", "\u0448"], # Ш
  ["\u0429", "\u0449"], # Щ
  ["\u042A", "\u044A"], # Ъ
  ["\u042B", "\u044B"], # Ы
  ["\u042C", "\u044C"], # Ь
  ["\u042D", "\u044D"], # Э
  ["\u042E", "\u044E"], # Ю
  ["\u042F", "\u044F"]  # Я
]


def read_word_corpus() -> List[List[str]]:
  s = ""
  with codecs.open("corpus.txt", mode="r", encoding="utf-8") as f:
    s = f.read()
  corpus = s.split("\n")
  return [[word] for word in corpus]


def print_list(l: List[str]) -> None:
  for i, s in enumerate(l):
    if i != 0:
      print(", ", end="")
    print("{}".format(s), end="")
  print(" - ", end="")


def main(corpus):
  indices = [i for i in range(len(corpus))]
  if "--random" in sys.argv:
    random.shuffle(indices)  
  loop = True
  while loop:
    if "--loop" not in sys.argv:
      loop = False
    for i in indices:
      print_list(corpus[i])
      user_input = input()
      while user_input not in corpus[i] and user_input != "skip":
        print("Incorrect")
        print_list(corpus[i])
        user_input = input()


if __name__ == "__main__":
  corpus = alphabet
  if "--words" in sys.argv:
    corpus = read_word_corpus()
  main(corpus)
