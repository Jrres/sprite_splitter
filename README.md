A tool to split spritesheets into rows taking in the user input. 

You must install the depencies in the file to run the python file using   
>> pip install --upgrade pip
>>  pip install --upgrade Pillow
Then, to run do
>> py.exe ./spriteCut.py

Example of usage: 
![char_a_p1_0bas_image](https://github.com/Jrres/sprite_splitter/assets/80206848/99ee4e42-f3b1-4eac-8cbe-4e5db0b89a99)
Imagine you have this image which represents a 512X512 sprite sheet 
If you wanted to extract a certain row such as the 7th row it would look something like this:
![cropped_sprite](https://github.com/Jrres/sprite_splitter/assets/80206848/1cff26c0-2f22-4abf-bdd5-fa27b8eeffd1)
Usually this type of sprite splitting is useful in order to have a simpler editor split the row into individual frames for us. 
However there is no free tool that simply gets a row of sprites, which is where this tool solves the problem.
Just extract the row you want from a grid of sprites and then use the result image. 

How to use the tool:
![3835be6156009a096e0149d778a24d26](https://github.com/Jrres/sprite_splitter/assets/80206848/07e01a8b-a809-4002-b70c-f966f8117ffd)
When you run the python file, you will get a form that requires multiple inputs.
Row is the row you want to extract
column is the column you want to start extracting from
Total Rows is the total number of sprites you see vertically in one column
Total Columns is the total number of sprites you see horizontally in one row
Finally select a file is required, you must select an image of type png or jpg in order to proceed
Then hit submit and you will be prompted with the resulting image as well as the file in your working directory.
