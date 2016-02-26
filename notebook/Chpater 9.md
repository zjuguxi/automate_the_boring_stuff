# Chpater 9

## Copying Files and folders

- shutil.copy(source, destination)
  
  destination可以是一个文件名
  
- shutil.copytree(source, destination)
  
  source和destination都是string

## Moving and remaining files and folders

- shutil.move(source, destination)
  
  注意：如果有同名文件，将被覆盖
  
  destination必须是文件名，移动后的文件将使用新名字

## Permanently Deleting files and folders

