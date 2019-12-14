import sys 
from asm_parser import *

class Assembler:
    __parser = 0
    __output_file = 0
    __binary_source = {
        '0'  : '101010',
        '1'  : '111111',
        '-1' : '111010', 
        'D'  : '001100',
        'A'  : '110000', 
        'M'  : '110000',
        '!D' : '001101',
        '!A' : '110001',
        '!M' : '110001',
        '-D' : '001111',
        '-A' : '110011',
        '-M' : '110011',
        'D+1': '011111',
        'A+1': '110111', 
        'M+1': '110111',
        'D-1': '001110',
        'A-1': '110010', 
        'M-1': '110010',
        'D+A': '000010', 
        'D+M': '000010',
        'D-A': '010011',
        'D-M': '010011',
        'A-D': '000111',
        'M-D': '000111',
        'D&A': '000111', 
        'D&M': '000000',
        'D|A': '000111',
        'D|M': '010101'
    }
    __binary_jump = {
        ''    : '000',
        'JGT' : '001',
        'JEQ' : '010',
        'JGE' : '011',
        'JLT' : '100',
        'JNE' : '101',
        'JLE' : '110',
        'JMP' : '111'
    }
    __binary_target = {
        ''   : '000',
        'M'  : '001',
        'D'  : '010',
        'MD' : '011',
        'A'  : '100',
        'AM' : '101',
        'AD' : '110',
        'AMD': '111'
    }
    def __init__(self, file_name):
        self.parser = Parser(file_name)
        self.output_file = open(file_name.partition('.')[0] + '.hack', 'w+')

    
    def __to_binary(self, n):
        n_bin = bin(n)[2:]
        return '0' * (15 - len(n_bin)) + n_bin

    def assemble(self):
        while self.parser.lines_are_left():
            operation = self.parser.get_next_operation()
            if operation.type is OperationType.A:
                binary_code = '0' + self.__to_binary(int(operation.label))
            else:
                binary_code = '111'
                source = operation.source
                if 'M' in source:  # Memory-Operation
                    a = '1'
                else: 
                    a = '0'
                binary_source = self.__binary_source[operation.source]
                binary_target = self.__binary_target[operation.target]
                binary_jump = self.__binary_jump[operation.jump]
                binary_code = '111' + a + binary_source + binary_target + binary_jump   
            self.output_file.write(binary_code + '\n')       


a = Assembler(str(sys.argv[1]))
a.assemble()
