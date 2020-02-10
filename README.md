# libs3
The purpose of this repo is to provide an easy to use interface to s3 for python developers, the core python libraries like os, shutil are easy to use and more familier to any python programmer. 

The repo aims to mimic the functionality so that your code will interact with s3 in same way as it is interacting in linux or windows filesystem, with 1 or 2 line change 

## Installation
```
pip install libs3
```

## Documentation 
A list of functions have been exposed which are working as of now and more will be added later (contributions are welcome)

### os

| Function  | Availaible | Comments |
| ------------- | ------------- | ---|
| ```os.listdir(x)``` | yes  |As s3 has no notion of directories, in order to list directories along with files we have to traverse entire bucket and filter the results. <br>For more quick results you can use <b>os.listdir(x, filesonly=True)</b> is much fast but will only returns files and not directory|
| ```os.mkdir(x)```  | no |As s3 has no concept of directory, we cannot create an empty directory|
| ```os.makedirs(x)``` | no |As s3 has no concept of directory, we cannot create an empty directory|
| ```os.remove(x)```  | no |will be added in later releases|
| ```os.removedirs(x)``` | no | will be added in later releases|
| ```os.rmdir(x)```| no | will be added in later releases|
| ```os.rename(x)```| no | will be added in later releases|
| ```os.renames(x)```| no | will be added in later releases|
| ```os.replace(x)```| no | will be added in later releases|
| ```os.scandir(x)```| no | will be added in later releases|
| ```os.walk(x)```| no | will be added in later releases|


### os.path

| Function  | Availaible | Comments |
| ------------- | ------------- | ---|
|```os.path.basename(x)```| yes | |
|```os.path.commonpath(x)```| no | will be added in later releases|
|```os.path.commonprefix(x)```| no | will be added in later releases|
|```os.path.dirname(x)```| yes | |
|```os.path.exists(x)```| yes | |
|```os.path.isfile(x)```| yes | |
|```os.path.isdir(x)```| yes | |
|```os.path.join(x)```| no | will be added in later releases|


### shutil

| Function  | Availaible | Comments |
| ------------- | ------------- | ---|
|```shutil.copyfile()```| no | will be added in later releases|
|```shutil.copy()```| yes ||
|```shutil.copytree()```| no | will be added in later releases|
|```shutil.rmtree()```| no | will be added in later releases|
|```shutil.move()```| no | will be added in later releases|
|```shutil.disk_usage()```| no | will be added in later releases|

## Example

<b>Importing the module and authorizing using s3 credentials</b>
```
from libs3 import os
os.authorize(bucket, aws_access_key_id, aws_secret_access_key)
```
<b>After authorizing access the interface like normally accessing filesystem</b>
```
print(os.listdir("/dir_1/dir_1"))
print(os.listdir("/dir_1/dir_1", filesonly=True))   # Much quicker

print(os.path.exists('/dir_1/file_2'))
print(os.path.isfile('/dir_1/file_2'))
print(os.path.isdir('/dir_1/file_2'))
print(os.path.basename('/dir_1/file_2'))
print(os.path.dirname('/dir_1/file_2'))

```
