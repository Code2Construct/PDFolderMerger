import tkinter as tk

class FileSelectorApp:
    def __init__(self, root, message):
        """引数として受け取ったメッセージを表示"""
        self.root = root
        self.root.title("工事検査用PDFファイル作成アプリ")
        self.root.geometry("800x150")

        # 引数で受け取ったメッセージをラベルに表示
        self.status_label = tk.Label(root, text=message, font=("Arial", 9))
        self.status_label.pack(pady=10)

        # 「OK」ボタンの追加
        self.ok_button = tk.Button(root, text="     OK      ", font=("Arial", 20), command=self.on_ok_button_click)
        self.ok_button.pack(pady=10)

    def on_ok_button_click(self):
        """OKボタンが押された時の処理"""
        print("OKボタンが押されました。")
        self.root.quit()  # メインループを終了
        self.root.destroy()  # ウィンドウを破棄

def main(message):
    """親モジュールから引数を渡してウィンドウを表示"""
    root = tk.Tk()
    app = FileSelectorApp(root, message)  # メッセージを引数として渡す
    root.mainloop()

if __name__ == "__main__":
    # 親モジュールから渡すメッセージ
    message = "処理が終わりました。OKボタンを押してください。"
    main(message)  # 引数としてメッセージを渡す
