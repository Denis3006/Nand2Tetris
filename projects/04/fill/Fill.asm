// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(START)
    // i = SCREEN[0]
    @SCREEN
    D = A
    @i
    M = D
(FOR)
    @KBD
    D = M;
    @NOT_PRESSED
    D; JEQ
    @color
    M = -1
    @FILL
    0; JMP
(NOT_PRESSED)
    @color
    M  = 0
(FILL)
    @KBD
    D = A
    @i
    D = M - D
    @1
    D = D - A
    @START
    D; JGE
    @color
    D = M
    @i
    A = M
    M = D
    @i
    M = M + 1
    @FOR
    0; JMP
    