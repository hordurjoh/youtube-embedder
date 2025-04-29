import tkinter as tk
from tkinter import messagebox
import webbrowser

video_ids = []

def add_videos():
    ids_text = entry.get("1.0", tk.END).strip()
    ids_list = ids_text.split()
    added_count = 0

    for video_id in ids_list:
        video_id = video_id.strip()
        if len(video_id) == 11:
            video_ids.append(video_id)
            listbox.insert(tk.END, f"Video ID: {video_id}")
            added_count += 1
        else:
            continue

    entry.delete("1.0", tk.END)
    
    if added_count == 0:
        messagebox.showerror("No Valid IDs", "Please paste valid 11-character YouTube Video IDs.")

def generate_html():
    if not video_ids:
        messagebox.showwarning("No Videos", "You have not added any videos yet.")
        return
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>YouTube Video List</title>
</head>
<body>
<h1>My YouTube Video List</h1>
"""
    for vid in video_ids:
        html_content += f"""
<div style="margin-bottom: 20px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/{vid}?autoplay=0" frameborder="0" allowfullscreen></iframe>
</div>
"""
    html_content += """
</body>
</html>
"""

    with open("youtube_video_list.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    webbrowser.open("youtube_video_list.html")
    messagebox.showinfo("Success", "HTML page created and opened!")

# GUI Setup
root = tk.Tk()
root.title("YouTube Video List Builder")

tk.Label(root, text="Paste YouTube Video IDs (one per line or space separated):").pack(pady=5)
entry = tk.Text(root, width=50, height=5)
entry.pack(pady=5)

tk.Button(root, text="Add Videos", command=add_videos).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Generate HTML Page", command=generate_html).pack(pady=10)

root.mainloop()
