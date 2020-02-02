import sys
from getch import getch

class Brainfuck:

    def __init__(self, code):
        self.code = self.cleanup(code)
        self.bracemap = self.generateBracemap()
        self.ar = [0]
        self.cellpos, self.codepos, self.codelen = 0, 0, len(self.code)

        self.interpret()

    def cleanup(self, code):
        return ''.join(filter(lambda x: x in ['.', ',', '+', '-', '[', ']', '<', '>'], list(code)))

    def generateBracemap(self):
        temp, bracemap = [], {}

        for pos, cmd in enumerate(self.code):
            if cmd == '[':
                temp.append(pos)
            elif cmd == ']':
                start = temp.pop()
                bracemap[start] = pos
                bracemap[pos] = start

        return bracemap

    def interpret(self):
        while self.codepos < self.codelen:
            cmd = self.code[self.codepos]

            if cmd == '>':
                self.cellpos += 1
                if self.cellpos == len(self.ar):
                    self.ar.append(0)
            elif cmd == '<' and self.cellpos > 0:
                self.cellpos -= 1
            elif cmd == '+' and self.ar[self.cellpos] < 255:
                self.ar[self.cellpos] += 1
            elif cmd == '-' and self.ar[self.cellpos] > 0:
                self.ar[self.cellpos] -= 1
            elif cmd == '.':
                print(chr(self.ar[self.cellpos]), end='')
            elif cmd == ',':
                self.ar[self.cellpos] = ord(getch())
            elif (cmd == '[' and self.ar[self.cellpos] == 0) or (cmd == ']' and self.ar[self.cellpos] != 0):
                self.codepos = self.bracemap[self.codepos]

            self.codepos += 1

def usage():
    print("Usage: brainfuck.py file...")
    exit()

def main(args):
    if len(args) != 2:
        usage()

    try:
        file = open(argv[1], 'r')
        c = file.read()
        file.close()
        Brainfuck(code)
    except FileNotFoundError:
        print("File Not Found.")
        exit()

if __name__ == '__main__':
    main()
