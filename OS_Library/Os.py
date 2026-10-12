import os

print("Operating system:", os.name)
print("Current folder:", os.getcwd())


items=os.listdir("Python")
for i in items:
    print(i)

current_folder=os.getcwd()
print(current_folder)

new_path="new_folder"
os.mkdir(new_path)
print(f"New Directoty {new_path} is created!")
print(os.getcwd())

lists=os.listdir('.')
for li in lists:
    print(li)

dir_name= "New_folder"
file_name="main_file"
new_file=os.path.join(dir_name,file_name)
print(new_file)

path="Desktop\Python\Python_Basics\Datatype.ipynb"
bol=os.path.exists(path)
print(bol)

path="DataStructure"
if(os.path.isdir(path)):
    print("True")
else:
    print("false")

path="check.py"
if(os.path.isfile(path)):
    print("True")
else:
    print("false")