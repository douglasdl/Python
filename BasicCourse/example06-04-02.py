# coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg

# ボタンがクリックされたときの処理
def ButtonClick():
	tmsg.showinfo("テスト", "クリックされたよ")

# メインのプログラム
root = tk.Tk()
root.geometry("400x150")
root.title("数当ゲーム")

label1 = tk.Label(root, text="数を入れてね", font=("Helvetica", 14))
label1.place(x = 20, y = 20)

editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x = 120, y = 60)

button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command=ButtonClick)
button1.place(x = 220, y = 60)

root.mainloop()