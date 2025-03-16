import tkinter as tk
from tkinter import filedialog
import os

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("工事検査用PDFファイル作成アプリ")
        self.root.geometry("950x180",)  # 横長のウィンドウサイズを設定
        # カスタムタイトルラベル
        #title_label = tk.Label(root, text="工事検査用PDFファイル作成アプリ", font=("Arial", 16), fg="white", bg="darkblue")
        #title_label.pack(fill=tk.X, pady=10)  # 横に広がるタイトルラベルを配置

        # フレームを作成して横方向に要素を配置
        frame = tk.Frame(root, height=60)
        frame.pack(padx=10, pady=10, fill=tk.X)
        frame.pack_propagate(False)  # フレームの高さを固定
        frame2=tk.Frame(root)
        frame2.pack(padx=10, pady=5, fill=tk.X)
        # フレーム2のラベル
        self.notice_label = tk.Label(
            frame2, 
            text=
            '''機能）選択したフォルダ内のすべてPDFファイルを結合し、ファイル名をしおり、フォルダ名を親しおりとして追加して一つのPDFファイルとして保存します。
注意）本アプリは住宅部建設課工事グループでpythonで開発していますが、現在ソースコードを一般公開してないため、使用したモジュールのライセンスにより、工事受注者等の都市整備局職員以外への提供・使用はライセンス違反となりますので、決して行わないでください。''',
            anchor="w",  # 左揃え
            justify="left",  # テキストを左揃え
            wraplength=1150  # ラベル内で改行
        )
        self.notice_label.pack(side=tk.LEFT, padx=10)  # 左揃えに配置
        
        # フォルダ選択ボタン
        self.folder_button = tk.Button(frame, text="フォルダを選択", bg="lightgray", command=self.select_folder)
        self.folder_button.pack(side=tk.LEFT, padx=10)

        # フォルダ選択結果表示
        self.folder_label = tk.Label(frame, text="未選択", width=30, anchor="w")
        self.folder_label.pack(side=tk.LEFT, padx=10)

        # 保存ファイル選択ボタン
        self.file_button = tk.Button(frame, text="検査用PDF保存先", bg="lightgray", command=self.select_save_file)
        self.file_button.pack(side=tk.LEFT, padx=10)

        # 保存ファイル選択結果表示
        self.file_label = tk.Label(frame, text="未選択", width=30, anchor="w")
        self.file_label.pack(side=tk.LEFT, padx=10)

        # 実行ボタン
        self.run_button = tk.Button(frame, text="PDFファイル\n作成開始", bg="lightgray", command=self.finish)
        self.run_button.pack(side=tk.LEFT, padx=10)

        # フォルダとファイルパスを保持する変数
        self.selected_folder = None
        self.selected_file = None

        # 初期フォルダ設定
        self.default_folder = os.path.expanduser("~/Documents")  # ユーザーのドキュメントフォルダを設定

        # ウィンドウの×ボタンにカスタム処理を設定
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def select_folder(self):
        """フォルダ選択ダイアログを表示"""
        folder = filedialog.askdirectory(
            title="フォルダを選択してください",
            initialdir=self.default_folder
        )
        if folder:
            self.folder_label.config(text=folder)
            self.selected_folder = folder

    def select_save_file(self):
        """保存ファイル選択ダイアログを表示"""
        file = filedialog.asksaveasfilename(
            title="保存するファイルを指定してください",
            defaultextension=".pdf",
            filetypes=[("PDFファイル", "*.pdf")],
            initialdir=self.default_folder,
            initialfile="検査用栞付結合データ.pdf"
        )
        if file:
            self.file_label.config(text=file)
            self.selected_file = file

    def finish(self):
        """選択結果を保存してウィンドウを閉じる"""
        #self.root.quit()  # メインループを終了
        self.root.destroy()  # ウィンドウを破棄
    
    def on_closing(self):
        """ウィンドウの×ボタンが押されたときの処理"""
        print("ウィンドウが閉じられました。")  # デバッグ用（不要なら削除）
        self.selected_folder = None
        self.selected_file = None
        self.root.destroy()

def select_folder_and_file():
    """フォルダとファイル選択を行い、結果を返す"""
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()  # GUIのイベントループ開始
    return app.selected_folder, app.selected_file

if __name__ == "__main__":
    folder, file = select_folder_and_file()
    print(f"選択されたフォルダ: {folder}")
    print(f"保存するファイルのパス: {file}")