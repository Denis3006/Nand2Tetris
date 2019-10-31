from asm_parser import *

class Assembler:
    parser = 0
    output_file = 0

    def __init__(self, file_name):
        self.parser = Parser(file_name)
        self.output_file = open(file_name.partition('.')[0] + '.hack', 'w+')

    
    def _to_binary(self, n):
        n_bin = bin(n)[2:]
        return '0' * (15 - len(n_bin)) + n_bin


    def _get_binary_source(self, source):
        if source == '0':
            return '101010'
        elif source == '1':
            return '111111'
        elif source == '-1':
            return '111010'
        elif source == 'D':
            return '001100'
        elif source in ['A', 'M']:
            return '110000'
        elif source == '!D':
            return '001101'
        elif source in ['!A', '!M']:
            return '110001'
        elif source == '-D':
            return '001111'
        elif source in ['-A', '-M']:
            return '110011'
        elif source == 'D+1':
            return '011111'
        elif source in ['A+1', 'M+1']:
            return '110111'
        elif source == 'D-1':
            return '001110'
        elif source in ['A-1', 'M-1']:
            return '110010'
        elif source in ['D+A', 'D+M']:
            return '000010'
        elif source in ['D-A', 'D-M']:
            return '010011'
        elif source in ['A-D', 'M-D']:
            return '000111'
        elif source in ['D&A', 'D&M']:
            return '000000'
        elif source in ['D|A', 'D|M']:
            return '010101'


    def _get_binary_target(self, target):
        if target == '':
            return '000'
        elif target == 'M':
            return '001'
        elif target == 'D':
            return '010'
        elif target == 'MD':
            return '011'
        elif target == 'A':
            return '100'
        elif target == 'AM':
            return '101'
        elif target == 'AD':
            return '110'
        elif target == 'AMD':
            return '111'


    def _get_binary_jump(self, jump):
        if jump == '':
            return '000'
        elif jump == 'JGT':
            return '001'
        elif jump == 'JEQ':
            return '010'
        elif jump == 'JGE':
            return '011'
        elif jump == 'JLT':
            return '100'
        elif jump == 'JNE':
            return '101'
        elif jump == 'JLE':
            return '110'
        elif jump == 'JMP':
            return '111'

    def assemble(self):
        while self.parser.lines_are_left():
            operation = self.parser.get_next_operation()
            if operation.type is OperationType.A:
                binary_code = '0' + self._to_binary(int(operation.label))
            else:
                binary_code = '111'
                source = operation.source
                if 'M' in source:  # Memory-Operation
                    a = '1'
                else: 
                    a = '0'
                binary_source = self._get_binary_source(operation.source)
                binary_target = self._get_binary_target(operation.target)
                binary_jump = self._get_binary_jump(operation.jump)
                binary_code = '111' + a + binary_source + binary_target + binary_jump   
            self.output_file.write(binary_code + '\n')     


a = Assembler("PongL.asm")
a.assemble()
