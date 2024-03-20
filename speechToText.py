from janome.tokenizer import Tokenizer
import re

def tokenize_japanese_text(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    words = [token.surface for token in tokens]
    return words

# vttファイルから日本語テキストを取得する関数
def extract_japanese_text_from_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 日本語テキストの部分を抽出する処理を実装
        # 例: 日本語テキストが含まれる行に絞り込む

        japanese_text = ""
        for line in lines:
            if ">" in line:
                # "字幕開始"以降の行が日本語テキストとして抽出される
                # ここでは単純に連結しているが、必要に応じてテキストの整形を行う
                cleaned_text = re.sub('<.*?>|\n', '', line) #<誰がしゃべったか>+改行コード(/n)
                japanese_text += cleaned_text

            # 他にも特定のパターンやキーワードに基づいて別の抽出方法を利用することができる

        return japanese_text

# vttファイルのパス
test_file_path = "AmiVoice.vtt"
# correct_file_path = ""

# vttファイルから日本語テキストを取得
test_text = extract_japanese_text_from_vtt(test_file_path)
# correct_text = extract_japanese_text_from_vtt(correct_file_path)

# 形態素解析による単語への分割
test_words = tokenize_japanese_text(test_text)
# correct_words = tokenize_japanese_text(correct_text)

# 正しいスクリプトとの比較などによる認識率の計算を実行
# この部分は、実際に使用する正しいスクリプトとの比較を行うために追加処理が必要です

print(test_words)

def calculate_recognition_rate(correct_script, test_script):
    correct_words = correct_script.split()
    test_words = test_script.split()

    word_count = len(correct_words)
    correct_count = 0

    for i in range(min(len(correct_words), len(test_words))):
        if correct_words[i] == test_words[i]:
            correct_count += 1

    recognition_rate = (correct_count / word_count) * 100
    return recognition_rate

# 正しいスクリプトとテストスクリプトの例
correct_script = "This is a test script for evaluation"
test_script = "This is a test script for validation"

# 認識率計算
recognition_rate = calculate_recognition_rate(correct_script, test_script)
print(f"Recognition Rate: {recognition_rate:.2f}%")