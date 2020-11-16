# coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

# ボタンがクリックされたときの処理
def ButtonClick():
	# テキスト入力欄に入力された文字列を取得
	b = editbox1.get()
	# メッセージとして表示する
	#tmsg.showinfo("テスト", b)

	# 4桁の数字かどうかを判定する
	isOK = False
	if len(b) != 4:
		tmsg.showerror("エラー", "4桁の文字を入力してください")
	else:
		kazuOK = True
		for i in range(4):
			if (b[i] < "0") or (b[i] > "9"):
				tmsg.showerror("エラー", "数字ではありません")
				kazuOK = False
				break
			if kazuOK:	
				isOK = True
	if isOK:			
		# 4桁の数字であったとき
		# ビットを判定
		hit = 0
		for i in range(4):
			if a[i] == int(b[i]):
				hit = hit + 1

		# ブローを決定
		blow = 0
		for j in range(4):
			for i in range(4):
				if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
					blow += 1
					break

		# ヒットが４なら当たりで終了
		if hit == 4:
			tmsg.showinfo("当たり！", "おめでとうございます。当たりです")
			# 終了
			root.destroy()
		else:
			# ビットとブロー数を表示
			rirekibox.insert(tk.END, b + " / Hit: " + str(hit) + " Blow: " + str(blow) + "\n")

		
# メインのプログラム
a = [random.randint(0, 9),
random.randint(0, 9),
random.randint(0, 9),
random.randint(0, 9)]

# ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")
root.title("数当ゲーム")

# 履歴表示のテキストボックスを作る
rirekibox = tk.Text(root, font=("Helvetica", 14))
rirekibox.place(x=400, y=0, width=200, height=400)

# ラベルを作る
label1 = tk.Label(root, text="数を入れてね", font=("Helvetica", 14))
label1.place(x = 20, y = 20)

# テキストボックスを作る
editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x = 120, y = 60)

# ボタンを作る
button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command=ButtonClick)
button1.place(x = 220, y = 60)

# ウィンドウを表示する
root.mainloop()