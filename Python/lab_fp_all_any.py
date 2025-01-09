docs = ["DOC1", "DOC2", "DOC3", "DOC4"]
docs2 = ["exe1", "exe2", "exe3", "exe4"]

if any("DOC" in doc for doc in docs):
    print("В документах есть файл DOC")
else:
    print("В документах нет файла DOC")

if any("DOC" in doc for doc in docs2):
    print("В документах есть файл DOC")
else:
    print("В документах нет файла DOC")