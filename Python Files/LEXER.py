import LANG
while True:
    text = input('LexicalAnalyzer --> ')
    result, error = LANG.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)