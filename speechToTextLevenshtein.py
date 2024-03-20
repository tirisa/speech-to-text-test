from janome.tokenizer import Tokenizer
import Levenshtein as lev
 
def split_words_from_japanese_text(text):
    """
    日本語テキストを分かち書きする。
    """
    tokenizer = Tokenizer()
    return ' '.join(tokenizer.tokenize(text, split_words_from_japanese_text=True))
 
def calculate_wer(reference, hypothesis):
    """
    Calculate the Word Error Rate (WER) between a reference text and a hypothesis text.
    """
    distance = lev.distance(reference, hypothesis)
    wer = distance / max(len(reference.split()), len(hypothesis.split()))
    return wer
 
def read_file(filepath):
    """
    ファイルからテキストを読み込む。
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
 
# ファイルパスを指定
reference_filepath = 'AmiVoice.vtt' # 参照テキストのファイルパス
hypothesis_filepath = 'hypothesis.txt' # 仮説テキストのファイルパス
 
# ファイルからテキストを読み込む
reference_text = read_file(reference_filepath)
hypothesis_text = read_file(hypothesis_filepath)
 
# 分かち書きを行う 
split_words_from_japanese_text_reference = split_words_from_japanese_text(reference_text) 
split_words_from_japanese_text_hypothesis = split_words_from_japanese_text(hypothesis_text)
 
# WERを計算する
# 単語誤り率（Word Error Rate; WER）＝（挿入単語数 ＋ 置換単語数 ＋ 削除単語数）／正解単語数
wer = calculate_wer(split_words_from_japanese_text_reference, split_words_from_japanese_text_hypothesis)
print(f"WER: {wer:.2%}")