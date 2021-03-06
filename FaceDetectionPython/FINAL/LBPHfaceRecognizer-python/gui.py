import Tkinter as tk
import random
    
root = tk.Tk()
# width x height + x_offset + y_offset:
root.geometry("170x200+30+30") 
     


def GUI(text, i):
	ct = [random.randrange(256) for x in range(3)]
   	brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   	ct_hex = "%02x%02x%02x" % tuple(ct)
   	bg_colour = '#' + "".join(ct_hex)
   	l = tk.Label(root, 
                text= text, 
                fg='White' if brightness < 120 else 'Black', 
                bg=bg_colour)
   	l.place(x = 20, y = 30 + i*30, width=120, height=25)
   	root.mainloop()
