import os
import fnmatch

# search_path = raw_input("Enter directory path to search : ")
search_path = os.getcwd()
search_str = raw_input("Enter the search string : ")
log = open(search_path + '/jlable_log.txt', 'w')

for root, directories, file in os.walk(search_path):
    for filename in fnmatch.filter(file, '*.html'):
        file_name = os.path.join(root, filename)
        file_open = open(file_name)
        line = file_open.readline()
        line_no = 1
        while line != '':
            index = line.find(' ' + search_str + ' ')
            if (index != -1):
                print file_name, ":", line_no
                print line
                log.write(file_name + ':' + str(line_no) + '\n' + line)
            line = file_open.readline()
            line_no += 1
        file_open.close()
