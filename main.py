import tkinter as tk
import subprocess
import threading

script_path_list = [
  "/Users/ikaros/Documents/practice/python-tk/sleep.sh",
  "/Users/ikaros/Documents/practice/python-tk/sleep2.sh",
]

def execute(path):
  result = subprocess.run(path, stdout=subprocess.PIPE,encoding='utf8')
  return result.stdout


def process_script():
  for script_path in script_path_list:
    header_label.configure(text=f'正在處理 {script_path}')
    print(execute(script_path))
  header_label.configure(text='處理完畢')
  calculate_btn.configure(state=tk.NORMAL)

  
def btn_click():
  calculate_btn.configure(state=tk.DISABLED)
  t = threading.Thread(target=process_script)
  t.start()

window = tk.Tk()
window.geometry('800x600')
window.configure(background='white')

header_label = tk.Label(window, text='等待開始', width=100)
header_label.pack()

calculate_btn = tk.Button(window, text='GO', command=btn_click)
calculate_btn.pack()

window.mainloop()