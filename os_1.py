import os
#Built-in dir function
#print(dir(os))---> # all the attributes and methods that we have
#access to within the module we passed in
print(os.getcwd()) #get the current work directory
os.chdir('C:/Users/alber/Desktop/')
print(os.listdir()) #show folders/files in the current directory,
#i.e. Python Data science

#To create a new directory we can use two methods: mkdir or makedirs 
# #which differ from each other.
# mkdirs() will create the specified directory path in its entirety
# where mkdir() will only create the bottom most directory, failing if 
# it can't find the parent directory of the directory it is trying to create.

#In other words mkdir() is like mkdir and mkdirs() is like mkdir -p.

#For example, imagine we have an empty /tmp directory. The following code

#new File("/tmp/one/two/three").mkdirs();
#would create the following directories:

#/tmp/one
#/tmp/one/two
#/tmp/one/two/three
#Where this code:

#new File("/tmp/one/two/three").mkdir();
#would not create any directories - as it wouldn't find /tmp/one/two - and 
#would return false.
#os.mkdir('demo_test_vuoto')
#os.makedirs('demo_test_vuoto_2/sub_directory')
#Analogously to delete folders with respectively os.rmdir and os.removedirs
#os.removedirs('demo_test_vuoto_2/sub_directory')