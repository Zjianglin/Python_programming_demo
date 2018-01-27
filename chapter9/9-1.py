'''
9-1. File Filtering. Display all lines of a file, except those that start
with a pound sign ( # ), the comment character for Python,
Perl, Tcl, and most other scripting languages.
Extra credit: Also strip out comments that begin after the first
character.
'''

def display_all(fname, comment=False):
    with open(fname, encoding='utf-8') as fin:
        for line in fin:
            if line.strip() and line.strip()[0] == '#':
                continue;
            if comment and '#' in line:
                    print(line[:line.find('#')])
            else:
                print(line)


def main():
    print('*** inter comment is ignored: ')
    display_all('example.txt')
    print('*** inter comment is filtered: ')
    display_all('example.txt', comment=True)

if __name__ == '__main__':
    main()
    
            