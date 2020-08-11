from PIL import Image,ImageGrab
import pyautogui
import time
def hit(key):
    pyautogui.keyDown(key)
    return

def iscollide(data):
    for i in range(400,425):
        for j in range(355,380):
            if data[i,j]<100:
                hit("up")
                return
             

    return         

    
if __name__=="__main__":
    print("hey Dino game about to start")
    time.sleep(2)
    hit("up")

    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        iscollide(data)
            

      # Draw the rectangle for cactus
        #for i in range(408,425):
          #  for j in range(355,380):
           #    data[i,j]=0

       #draw the rectange for birds
        #for i in range(250,300):
          #      data[i,j]=171   
        #break                                    

       # image.show()
        #break