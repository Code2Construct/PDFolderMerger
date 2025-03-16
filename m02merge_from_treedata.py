import os
from fitz import Document  # fitz.open() の代わりに Document を使用
from pandas import read_excel  # pandas の必要な関数のみをインポート

def merge_pdfs_from_df(df):
    """
    データフレームの指定列にあるPDFファイルを結合して1つのPDFファイルを作成します。

    Args:
        df (pd.DataFrame): PDFファイルのパスが格納されたデータフレーム。

    Returns:
        Document: 結合されたPDFドキュメントオブジェクト。
    """
    output_pdf = Document()  # 空のPDFを作成
    paths = df['Full Path'] 

    for path in paths:
        if os.path.isfile(path) and path.lower().endswith('.pdf'):
            with Document(path) as pdf:
                for page_num in range(pdf.page_count):
                    output_pdf.insert_pdf(pdf, from_page=page_num, to_page=page_num)
        else:
            print(f"Skipping: {path} (Not a PDF file or is a folder)")

    return output_pdf

if __name__ == '__main__':
    excel_path = "Treedata.xlsx"  # Excelファイルのパス
    df = read_excel(excel_path, sheet_name=0)  # pandas の read_excel を直接使用
    output_pdf_path = "merged_output.pdf"

    output_pdf = merge_pdfs_from_df(df)
    output_pdf.save(output_pdf_path)
    output_pdf.close()
    
    print(f"Merged PDF saved as {output_pdf_path}")
