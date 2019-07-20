if __name__ == '__main__':
    fileName = 'test.txt'
    with open(fileName, 'r') as inputFile, open('test-out.txt', 'w') as outputFile:
        lines = []
        for line in inputFile:
            lines.append(line.rstrip())
        lines.reverse()
        outputFile.write("\n".join(lines))
    inputFile.close()
    outputFile.close()