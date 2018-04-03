file_read = open("README")
file_write = open("READER_附件", "w")

t = file_read.read()
file_write.write(t)

file_read.close()
file_write.close()
