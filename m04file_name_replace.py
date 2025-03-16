import re
from pandas import DataFrame  # pd.DataFrame のため
from pandas import set_option  # 表示オプション設定のため

def modify_pdf_names_in_all_columns(df: DataFrame) -> DataFrame:
    """
    DataFrame内のすべての列に含まれる文字列を変更します。

    ただし、列名が "Full Path" の場合は変更をスキップします。

    修正内容:
    - "【本文】" → "本_"
    - "【鑑】" → "a鑑_"
    - "【添付" → "b添"
    - "】" → "_"
    - 値が.pdfで終わらない場合に、先頭に半角数字2文字と"-"があればそれを削除する

    Args:
        df (DataFrame): 変更対象のデータフレーム

    Returns:
        DataFrame: 変更後のデータフレーム
    """
    def modify_name(value):
        if isinstance(value, str):
            if value.endswith('.pdf'):
                value = (value.replace("【本文】", "")
                            .replace("【鑑】", "ｶ鑑_")
                            .replace("【添付", "ﾃ")
                            .replace("】", "_"))
                value = re.sub(r'^00(\d{2})-', r'', value)  # 00XX- を削除
            else:
                value = re.sub(r'^(\d{2})-', r'', value)  # XX- を削除
        return value

    for column in df.columns:
        if column != "Full Path":
            df[column] = df[column].apply(modify_name)

    return df

if __name__ == '__main__':
    set_option('display.unicode.east_asian_width', True)  # 表示設定（オプション）
    
    data = {
        "column1": ["【本文】example1.pdf", "example2.txt", "12-example3.txt"],
        "Full Path": ["C:/path/to/12-file1.pdf", "C:/path/to/file2.pdf", None],
        "column3": ["34-textfile.doc", "0034-【本文】【鑑】example6.pdf", "78-example7.pdf"]
    }

    df = DataFrame(data)

    print("変更前のデータフレーム:")
    print(df)

    modified_df = modify_pdf_names_in_all_columns(df)

    print("\n変更後のデータフレーム:")
    print(modified_df)



