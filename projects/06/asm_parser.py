from enum import Enum

class OperationType(Enum):
    A = 1
    C = 2
    LABEL = 3


class Operation:
    type
    target = ''
    source = ''
    label = ''
    jump = ''
    
    def __init__(self, code_line):
        if code_line[0] == '@':
            self.type = OperationType.A
            self.label = code_line[1:]
        elif code_line[0] == '(':
            self.type = OperationType.LABEL
            self.label = code_line[1:-1]
        else:
            self.type = OperationType.C
            if '=' in code_line:
                self.target = code_line.partition('=')[0]
                self.source = code_line.partition('=')[2].partition(';')[0]
                self.jump = code_line.partition('=')[2].partition(';')[2]
            else:
                self.target = ''
                self.source = code_line[0]
                self.jump = code_line[2:]


class Parser:
    _code_lines = []
    _current_line = -1

    def __init__(self, file_name):
        asm_file = open(file_name)
        for line in asm_file:
            if line[0] != '\n' and (line[0] != '/' and line[1] != '/'):
                self._code_lines.append(line.split()[0])


    def lines_are_left(self):
        return self._current_line + 1 < len(self._code_lines)


    def get_next_operation(self):
        self._current_line += 1
        return Operation(self._code_lines[self._current_line])