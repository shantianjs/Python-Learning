import os,re

os.chdir(r'F:\新建文件夹')
path= os.getcwd()
li=os.listdir('.')
pattern=re.compile(r'(，\s*)$',re.DOTALL|re.MULTILINE)
def remove_null():
    with open(r'F:\新建文件夹\', 'r+') as file:
        file1 = open(r'F:\新建文件夹\tem.txt', 'w')
        flag = False
        for line in file:
            if line is '\n':
                file1.write('')
            else:
                file1.write(line)
        file1.close()

def remove_unnecessary_space():
    with open(r'F:\新建文件夹\tem.txt','r+') as file:
        file1=open(r'F:\新建文件夹\tem1.txt','w')
        flag= False
        for line in file:
            matched= pattern.search(line)
            if matched:
                tem=matched.group()
                print(line,len(tem))
                file1.write(pattern.sub('，',line,1))
                flag =True
                print('successful')
            else:
                if flag:
                    file1.write(line.lstrip())
                    flag=False
                else:
                    file1.write(line)
        file1.close()
remove_null()
remove_unnecessary_space()

