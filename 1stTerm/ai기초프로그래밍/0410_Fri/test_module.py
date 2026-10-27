def count_words(text):
    cnt_words = len(text.split())
    print(f"단어 수: {cnt_words}")

def count_characters(text):
    cnt_char = len(text.replace(" ", ""))
    print(f"문자 수(공백 제외): {cnt_char}")