#coding: utf8
import os
import codecs

def getFileBypath(path):
    all_file_list = []
    if os.path.exists(path) and os.path.isdir(path):
        for file in os.listdir(path):
            file_path = os.path.join(path,file)
            if os.path.isdir(file_path):
                # list dir
                print("find folder:"+str(file_path))
                getFileBypath(file_path)
            else:
                # print file name
                all_file_list.append(file.split('.')[0])
    else:
        print("{} file not found".format(path))

    return all_file_list


def getFileContent(f):
    temp_file = f
    if isinstance(f,str):
        temp_file = codecs.open(f,encoding='utf-8')
    while True:
        bulk = temp_file.read(4049)
        if bulk:
            yield bulk
        else:
            break

if __name__ == "__main__":
    print(str(getFileBypath('../历史小说')))
    for line in getFileContent(os.path.join('../历史小说','丁香花_高阳_TXT小说天堂.txt')):
        print(str(line))