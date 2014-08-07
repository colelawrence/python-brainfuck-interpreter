import sys, re, time
from msvcrt import getch, putwch
file = open(sys.argv[1])
code = file.read()
file.close()

class BrainFxck(object):
  """Evaluator for brainfxck"""
  def __init__(self):
    super(BrainFxck, self).__init__()
  def incPtr(self):
    self.ptr+=1
    if(self.ptr >= len(self.cells)):
      self.cells.append(0)
  def decPtr(self):
    self.ptr-=1
  def incCell(self):
    self.cells[self.ptr]+=1
  def decCell(self):
    self.cells[self.ptr]-=1
  def putChar(self):
    putwch(chr(self.cells[self.ptr]))
  def getChar(self):
    l = getch()
    self.cells[self.ptr] = ord(l)
  def beginWhile(self):
    if(self.cells[self.ptr] != 0):
      # char should equal the next character
      self.whileLoopChars.append(self.char - 1)
    else:
      self.inFalseWhiles += 1
  def endWhile(self):
    if(self.inFalseWhiles > 0):
      self.inFalseWhiles -= 1
    else:
      self.char = self.whileLoopChars.pop()
  def toggleDebug(self):
    self.debug = not self.debug
  def eval(self, code):
    self.debug = False
    self.cells = [0]
    self.ptr = 0
    self.char = 0
    self.whileLoopChars = []
    self.inFalseWhiles = 0
    operators = {
      ">": self.incPtr,
      "<": self.decPtr,
      "+": self.incCell,
      "-": self.decCell,
      ".": self.putChar,
      ",": self.getChar,
      "[": self.beginWhile,
      "]": self.endWhile,
      "$": self.toggleDebug
    }
    code = re.sub("[^\$><+-.,\[\]]+", "", code)
    code = list(code)
    while self.char < len(code):
      operator = code[self.char]
      if self.debug:
        print(self.cells[self.ptr], '\t', operator, '\t', self.ptr, '\t', '\t'.join(str(x) for x in self.cells))
        time.sleep(.2)
      self.char+=1
      if(not self.inFalseWhiles or operator is "]" or operator is "["):
        operators[operator]()

bf = BrainFxck()
bf.eval(code)
