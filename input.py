# coding=utf-8

class ReadFile(object):
    """docstring for ReadFile"""
    def __init__(self, fileToRead):
        super(ReadFile, self).__init__()
        self.fileToRead = fileToRead
        self.fs = {}
    def read(self):
        f = open(self.fileToRead,'r')
        for line in f.readlines():
            if len(line):
                if line.startswith('content:'):
                    self.fs['content'] = line[8:]
                elif line.startswith('link:'):
                    self.fs['link'] = line[5:]
                elif line.startswith('comment:'):
                    self.fs['comment'] = line[8:]
    def show(self):
        print self.fs

if __name__ == '__main__':

    r = ReadFile('test.md')
    r.read()
    r.show()
