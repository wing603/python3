file_read = open("README")
file_write = open("READER_附件", "w")


while True:

    t = file_read.readline()
    if not t:
        break
    file_write.write(t)

file_read.close()
file_write.close()
