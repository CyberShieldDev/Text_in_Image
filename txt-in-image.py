from sys import platform
import os
if platform == "linux" or platform == "linux2":
    os.system("clear")
else:
    os.system("cls")
print("""
████████╗███████╗██╗  ██╗████████╗    ██╗███╗   ██╗    ██╗███╗   ███╗ █████╗  ██████╗ ███████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██║████╗  ██║    ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝
   ██║   █████╗   ╚███╔╝    ██║       ██║██╔██╗ ██║    ██║██╔████╔██║███████║██║  ███╗█████╗  
   ██║   ██╔══╝   ██╔██╗    ██║       ██║██║╚██╗██║    ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  
   ██║   ███████╗██╔╝ ██╗   ██║       ██║██║ ╚████║    ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚═╝  ╚═══╝    ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
    Cyber Shield Team - Azad                                                                                           


""")
def text_in_image():
    txt_file = input("[ example.txt ] Write the name of text file : ")
    img_file = input("[ example.png ] Write the name of image : ")
    save_in  = input("[ example-1.png ] Write a name to save : ")

    with open(f'{save_in}', 'wb') as out:
        out.write(open(f'{img_file}', 'rb').read())
        out.write(open(f'{txt_file}', 'rb').read())
        print(f"""
[ / ] Your image is saved as {save_in}
Just by opening the image with a notepad, go to below u can see your texts
        """)
text_in_image()
