Tkinter 

#Tkinter is Python's standard library for creating Graphical User Interfaces (GUIs). It's a thin object-oriented layer on top of the Tcl/Tk GUI toolkit.

'''Basic Structure
A Tkinter application typically involves the following steps:

Importing Tkinter: Import the tkinter module.
Creating the main window: Create an instance of the Tk class.
Adding widgets: Add various widgets (buttons, labels, text fields, etc.) to the window.
Running the main event loop: Start the application's main loop, which waits for user interactions.'''

#SIMPLE TKINTER APPLICATION:
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Run the main event loop
root.mainloop()

#COMMONLY USED WIDGETS 
#Labels
#Labels are used to display text or images.
label = tk.Label(root, text="This is a label")
label.pack()

#Buttons
#Buttons can perform an action when clicked.
button = tk.Button(root, text="Click Me", command=some_function)
button.pack()

#Entry
#Entry widgets are used to accept single-line text input from the user.
entry = tk.Entry(root)
entry.pack()

#Text
#Text widgets are used for multi-line text input.
 text = tk.Text(root)
text.pack()

#Frames
#Frames are used as containers to organize other widgets.
frame = tk.Frame(root)
frame.pack()



#Advanced Features
#Tkinter also supports more advanced features like creating menus, dialogs, canvases for drawing, and more.
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


