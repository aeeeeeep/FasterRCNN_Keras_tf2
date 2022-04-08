import os,sys

class FilesChange():
    def __init__(self):
        self.path = './Annotations'

    def Change(self):
        filelist = os.listdir(self.path)
        for item in filelist:
            srcfile = os.path.join(os.path.abspath(self.path), item)
            item = item.rstrip('.xml')
            item = item.zfill(5)
            line_replace = 2
            with open(srcfile,'r') as fd:
                lines = fd.readlines()
            lines[line_replace] = ('        <filename>' + item + '.jpg</filename>\n')
            lines[line_replace + 1] = ('        <path>' + format(srcfile[:-21]) + 'JPEGImages/' + item + '.jpg</path>\n')
            with open(srcfile,'w') as fd:
                fd.writelines(lines)


if __name__ == '__main__':
    demo = FilesChange()
    demo.Change()
