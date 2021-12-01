
import sys, random, time
from typing import List

class Letter:
  def __init__(self, upper: str, lower: str, phonetic: str, help: str) -> None:
      self.upper = upper
      self.lower = lower
      self.phonetic = phonetic
      self.help = help
  
  def display_front(self):
    print("Letter: {}, {}".format(self.upper, self.lower))

  def display_back(self) -> None:
    print("Sound:  {}\n{}".format(self.phonetic, self.help))

alphabet: List[Letter] = [
  Letter("\u0410", "\u0430", "ah, uh",      "Like father if stressed; if not, pronounced like 'u' as in hut"),
  Letter("\u0411", "\u0431", "b",           "Like boy"),
  Letter("\u0412", "\u0432", "v",           "Like very"),
  Letter("\u0413", "\u0433", "g",           "Like go; in genitive (possessive) endings ого/его like avoid, e.g., \"Dostoevsky's\" = Достоевского (duh-stah-YEHV-skuh-vuh)"),
  Letter("\u0414", "\u0434", "d",           "Like do"),
  Letter("\u0415", "\u0435", "yeh, ee, eh", "Like yesterday if stressed, before a stressed syllable pronounced as \"ee\" as in eel, or if after a stressed syllable and in only one syllable, pronounced like \"eh\" as in \"tell\""),
  Letter("\u0416", "\u0436", "zh",          "Like measure; always hard"),
  Letter("\u0417", "\u0437", "z",           "Like zoo"),
  Letter("\u0418", "\u0438", "ee",          "Like seen or the i in machine"),
  Letter("\u0419", "\u0439", "y",           "Like boy"),
  Letter("\u041A", "\u043A", "k",           "Like keep"),
  Letter("\u041B", "\u043B", "l",           "Like leek or look"),
  Letter("\u041C", "\u043C", "m",           "Like seem"),
  Letter("\u041D", "\u043D", "n, ñ",        "Like noodle; pronounced ny (palatalized, like a Spanish ñ) before ь, и, e, я, and ю."),
  Letter("\u041E", "\u043E", "oh, a, o",    "Like score when stressed; when unstressed, it is a hard a in Hakeem (syllable before stress) or the o in Gibson (elsewhere)."),
  Letter("\u041F", "\u043F", "p",           "Like spigot"),
  Letter("\u0420", "\u0440", "r",           "Heavily rolled as in Spanish rr in perro"),
  Letter("\u0421", "\u0441", "s",           "Like seem"),
  Letter("\u0422", "\u0442", "t",           "Like tattoo"),
  Letter("\u0423", "\u0443", "oo",          "Like cartoon, lips rounded as with French où"),
  Letter("\u0424", "\u0444", "f",           "Like french"),
  Letter("\u0425", "\u0445", "kh",          "Voiceless velar fricative as in the Scottish loch or German Bach"),
  Letter("\u0426", "\u0446", "ts",          "Like boots; always hard"),
  Letter("\u0427", "\u0447", "ch",          "Like cheap; always soft"),
  Letter("\u0428", "\u0448", "sh",          "Like shot; always hard (pronounced with the tip of the tongue further back in the mouth, almost a retroflex)"),
  Letter("\u0429", "\u0449", "sh",          "Similar to sheet; always soft: unlike ш, щ is palatalized, meaning that the tip of the tongue rests on the back of the lower teeth, and the sh sound is pronounced with the middle of the tongue."),
##Letter("\u042A", "\u044A", "",  ""), All my homies hate the hard sign
  Letter("\u042B", "\u044B", "yh",          "Like sit, hit, but pronounced far further down the throat, as if being punched in the stomach"),
  Letter("\u042C", "\u044C", "---",         "the soft sign - used to indicate that the preceding consonant is palatalized (in a position where it otherwise would not)"),
  Letter("\u042D", "\u044D", "eh",          "Like end (also pronounced further down the throat, as if being punched in the stomach)"),
  Letter("\u042E", "\u044E", "yoo, oo",     "Like you or Yugoslavia if stressed; if not, pronounced \"oo\" like cartoon"),
  Letter("\u042F", "\u044F", "yah, ee, eh", "Like Yacht when stressed; before a stressed syllable pronounced as \"ee\" as in eel, or if after a stressed syllable and in only one syllable, pronounced like \"eh\" as in \"tell\"")
]


def main():
  indices = [i for i in range(len(alphabet))]
  if "--random" in sys.argv:
    random.shuffle(indices)
  
  for i in indices:
    alphabet[i].display_front()
    input()
    alphabet[i].display_back()
    time.sleep(1)
    print()

if __name__ == "__main__":
  main()
