from filesystem import FileSystem as fs

# If output equals 1, the operation is successful

# Create File
action = fs.CreateFile("file_name.txt","content")
print(action)

# Delete File
action = fs.DeleteFile("file_name.txt")
print(action)

# Create Folder
action = fs.CreateFolder("folder_name")
print(action)

# Delete Folder
action = fs.DeleteFolder("folder_name")
print(action)

# Listing files in folder, this folder name is optional
action = fs.ListFolder("folder_name") 
print(action)

# File get content
action = fs.GetFile("file_name")
print(action)

# File upload to ipfs
action = fs.FileUpload("file_content")
print(action)
