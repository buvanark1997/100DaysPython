# #File reading and writing
# file = open("sampleTextFile.txt")
# print(file.read())
# file.close() #need to close without fail
#
# #no need of closing in below
# #mode of open is with read mode
# with open("sampleTextFile.txt") as file:
#     print(file.read())
#
# with open("sampleTextFile.txt",mode="w") as file:
#     file.write("written by me!!")
# with open("sampleTextFile.txt") as file:
#     print(file.read())
#
# with open("sampleTextFile.txt",mode="a") as file:
#     file.write("\n appended text.")
# with open("sampleTextFile.txt") as file:
#     print(file.read())
#
# #using absolute file path
# # with open("/Users/h537006/KT.txt") as filewithlongpath: #root folder (c:)will get appended before
# #     print(filewithlongpath.read())
# #using relative file path
# with open("../../KT.txt") as absfile:
#     print(absfile.read())
#
# with open("../Files/sampleTextFile.txt") as absfile:
#     print(absfile.read())


def letter_constructing():
    # https: // www.w3schools.com / python / python_file_write.asp
    with open("Input/Names/invited_names.txt") as names_file:
        LIST_NAMES=names_file.readlines()
    with open("Input/Letters/starting_letter.txt") as letter_file:
        mail_content = letter_file.read()
    for name in LIST_NAMES:
       mail_content = mail_content.replace("[name]", name)
       letter_name = "Output/ReadyToSend/"+"letter_for_"+name.strip()+".txt"
       with open(letter_name,mode="w") as outputfile:
          outputfile.write(mail_content.strip())





letter_constructing()