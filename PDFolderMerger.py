import sys
import m01make_treedata as m01
import m02merge_from_treedata as m02
import m03make_bookmark as m03
import m04file_name_replace as m04
import m05select_folder as m05
import m06finish_message as m06
# ユーザーにフォルダを選択させる
folder_path ,output_file_path= m05.select_folder_and_file()
if folder_path is None or output_file_path is None:
    print("キャンセルされたため処理を中断します。")
    sys.exit(1)  # 終了コード1（異常終了）
print(f"選択されたフォルダ: {folder_path}")

# m01からデータを作成
df, max_levels = m01.main(folder_path)

# データの各カラムのファイル名の変更
df=m04.modify_pdf_names_in_all_columns(df)

df = df.sort_values(by='sortpath', ascending=True)
# Excelファイルに保存
#df.to_excel('Treedata.xlsx', index=False)
# 'Page Count' を累積して 'Page All' を新たに追加
df['Page All'] = df['Page Count'].shift(1).cumsum().fillna(0).astype(int)
# 'Page All' を左端の列に移動
cols = ['Page All'] + [col for col in df.columns if col != 'Page All']
df = df[cols]
# データをExcelファイルに保存
#df.to_excel('Treedata.xlsx', index=False)

# PDFをマージ
output_pdf = m02.merge_pdfs_from_df(df)

# 結合したPDFを保存
output_pdf.save(output_file_path)

# マージしたPDFにブックマークを追加
m03.add_bookmarks_to_pdf(df, max_levels, output_pdf,output_file_path)

m06.main(f'{output_file_path}を保存しました。\nOKボタンを押してください。')
