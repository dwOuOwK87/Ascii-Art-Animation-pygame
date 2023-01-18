# Ascii Art Animation use pygame

## Tips
Clicking "start.py" can start the animation.  
It will show the setting window at first.  
Font size bigger than 12 is recommended.

## Need python3, opencv, and pygame
```
pip install opencv-python  
pip install pygame
```

## Links
[Video here.](https://youtu.be/fqHRjAfvBsY)  
For people who just want to easily use, exe file [here](https://drive.google.com/drive/folders/10Mv6SztT0jr-yEC20ksxw8jAXGUmQwd9?usp=sharing).  
Download "Converter2.exe" and just open it.

## How to make this
>[View the previous git.](https://github.com/dwOuOwK87/Bad-Apple-Ascii-Animation.git)  
>I just copied all the thing into pygame and improved the speed of the program.  
>Why I need to improve the speed is since that pygame can display more character than console. If I use the privious code, it will laggy.

How I improved the speed of my program is to use numpy.   
the type of image is ndarray.  
We can just divided it by a number, and it will work on all elements.  
And it faster!  

Previous:  
```
index = int(image[i][j] / math.ceil(256/len(ascii_sheet)))
ascii_sheet[index]
```
Now:  
```
ascii_range = 255 // (len(ascii_sheet) - 1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) // ascii_range
...
gray_value = image[y][x]
ascii_sheet[gray_value]
```
