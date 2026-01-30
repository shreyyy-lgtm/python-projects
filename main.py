import qrcode
from PIL import Image
url=input("Enter your url: ")
file_name=input("Enter your file name: ")
if not(file_name.endswith(".png")):
    file_name=file_name + ".png"
    
img= qrcode.make(url) 
img.save(file_name)   
