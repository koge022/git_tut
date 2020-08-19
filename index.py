import re

INPUT_PH = "?>"
QA_NONE = "no answer..."

qa_list = [
    ["k8s", "kubernetes"],
    ["vscode", "visual stadio code"],
    ["quest", "answer2"]
]


def qa_search(q):
    for qa in qa_list:
        if re.search(qa[0], q):
            return qa[1]
    return QA_NONE


if __name__ == '__main__':
    while True:
        q = input(INPUT_PH)
        if len(q) == 0:
            break
        print(qa_search(q))
