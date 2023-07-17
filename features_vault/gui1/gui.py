import tkinter as tk
from PIL import Image, ImageTk

# Create the Tkinter window
window = tk.Tk()
window.title("Sebastian")

# Make the window full screen
window.attributes('-fullscreen', True)

# Create a frame with a black background
frame = tk.Frame(window, bg="black")
frame.pack(fill=tk.BOTH, expand=True)

# Load the GIF image using Pillow
image = Image.open("/Users/fallenprince/Downloads/final_seb.gif")
frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(image))
        image.seek(len(frames))  # Move to the next frame
except EOFError:
    pass

# Calculate the center position of the window
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
gif_width = image.width
gif_height = image.height
center_x = (window_width - gif_width) // 2
center_y = (window_height - gif_height) // 2

# Display the GIF image in a label, centered in the frame
label = tk.Label(frame, image=frames[0], bg="black")
label.place(x=center_x, y=center_y)

def update_label(index):
    frame = frames[index]
    label.configure(image=frame)
    window.after(100, update_label, (index + 1) % len(frames))

# Start updating the label with the frames
update_label(0)

# Start the Tkinter event loop
window.mainloop()
