import os

if __name__ == '__main__':
    dirsWithPy = []
    for current_dir, dirs, files in os.walk('.'):
        for fileName in files:
            if fileName.endswith('.py'):
                dirsWithPy.append(current_dir.lstrip('.').lstrip('\\'))
                break
    with open('filesysout.txt', 'w') as fileSysOut:
        for dirName in dirsWithPy[1:]:
            fileSysOut.write(dirName + '\n')
    fileSysOut.close()
