import time
import webbrowser


i =0

while(i<3):
    print("O programa iniciou as {}".format(time.ctime()))
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i +=1