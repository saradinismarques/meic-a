
def read_file():
    result = open('Result.txt', 'w')

    file1 = open('TCOS.txt','r+')
    
    lines = file1.readlines()
    for line in lines:
        for c in line:
            if (c == ' '):
                result.write('\n')
            elif (c != ',' and c != '.'):
                result.write(c)               

    
    file1.close()

    result.write('\n')
    
    file2 = open('IceLyrics.txt','r+')
    lines = file2.readlines()
    for line in lines:
        for c in line:
            if (c == ' '):
                result.write('\n')
            elif (c != ',' and c != '.'):
                result.write(c)  
    file2.close()

    result.close()
    

def remove_duplicates():
    result = open('Result.txt', 'r')

    # remove dupiclate lines
    lines = result.readlines()
    lines_set = set(lines)

    out = open('Result.txt', 'w')

    for line in lines_set:
        out.write(line)
    

def main():
    read_file()
    remove_duplicates()

if __name__ == "__main__":
    main()
