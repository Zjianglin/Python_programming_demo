'''
9–5. Test Scores. Update your solution to the test scores problems
(Exercises 5–3 and 6–4) by allowing a set of test scores be
loaded from a file. We leave the file format to your discretion.
'''

def main():
    '''
    A: 90–100
    B: 80–89
    C: 70–79
    D: 60–69
    F: <60
    '''
    fname = input('Enter scores record file: ')
    with open(fname, encoding='utf-8') as fin:
        for subject in fin:
            item = subject.strip().split(',')
            if int(item[1]) < 60:
                print('{:15} {:3} {:3}'.format(item[0], item[1], 'F'))
            elif int(item[1]) < 70: #[60, 69]
                print('{:15} {:3} {:3}'.format(item[0], item[1], 'D'))
            elif int(item[1]) < 80: #[70, 79]
                print('{:15} {:3} {:3}'.format(item[0], item[1], 'C'))
            elif int(item[1]) < 90: #[80, 89]
                print('{:15} {:3} {:3}'.format(item[0], item[1], 'B'))
            else:
                print('{:15} {:3} {:3}'.format(item[0], item[1], 'A'))
    print()

if __name__ == '__main__':
    main()
                    
