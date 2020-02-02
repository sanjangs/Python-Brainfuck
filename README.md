# Brainfuck

*Adapted from [Wikipedia article on Brainfuck](https://en.wikipedia.org/wiki/Brainfuck).*

Brainfuck is an esoteric programming language created in 1993 by Urban Müller, and is notable for its extreme minimalism.

The language consists of only eight simple commands and an instruction pointer. While it is fully Turing complete, it is not intended for practical use, but to challenge and amuse programmers. Brainfuck simply requires one to break commands into microscopic steps.

The language's name is a reference to the slang term brainfuck, which refers to things so complicated or unusual that they exceed the limits of one's understanding.

## Language Design

Brainfuck has 8 basic instructions:

* `>` - move the pointer right
* `<` - move the pointer left
* `+` - increment the current cell
* `-` - decrement the current cell
* `.` - output the value of the current cell
* `,` - **replace** the value of the current cell with input
* `[` - jump to the **matching** `]` instruction if the current value is zero
* `]` - jump to the **matching** `[` instruction if the current value is **not** zero

A brainfuck program is a sequence of these commands, possibly interspersed with other characters (which are ignored). The commands are executed sequentially, with some exceptions: an instruction pointer begins at the first command, and each command it points to is executed, after which it normally moves forward to the next command. The program terminates when the instruction pointer moves past the last command.

As the name suggests, Brainfuck programs tend to be difficult to comprehend. This is partly because any mildly complex task requires a long sequence of commands, and partly it is because the program's text gives no direct indications of the program's state. These, as well as Brainfuck's inefficiency and its limited input/output capabilities, are some of the reasons it is not used for serious programming. Nonetheless, like any Turing complete language, Brainfuck is theoretically capable of computing any computable function or simulating any other computational model, if given access to an unlimited amount of memory.[8] A variety of Brainfuck programs have been written.[9] Although Brainfuck programs, especially complicated ones, are difficult to write, it is quite trivial to write an interpreter for Brainfuck in a more typical language such as C due to its simplicity. There even exist Brainfuck interpreters written in the Brainfuck language itself.[10][11]

Brainfuck is an example of a so-called Turing tarpit: It can be used to write any program, but it is not practical to do so, because Brainfuck provides so little abstraction that the programs get very long or complicated.

## Examples

### Hello World! Program
```
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```
