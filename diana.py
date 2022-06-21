import argparse
import string
import queue


def macro_generator():
    voc = ["然然", "🤤", "🥵"]
    q = queue.Queue()
    for v in voc:
        q.put(v)
    while not q.empty():
        front = q.get()
        for v in voc:
            q.put(front + v)
        yield front
    raise StopIteration


class Token:
    def __init__(self, content="", require_convert=False):
        self.content = ""
        self.require_convert = require_convert


__TK_INITIAL  = 0
__TK_WORD     = 1
__TK_NUMBER   = 2
__TK_DQUOT    = 3
__TK_SQUOT    = 4
__TK_OPERATOR = 5
__TK_PREPROC  = 6


def tokenize(code):
    token = Token()
    tokens = []
    status = __TK_INITIAL
    idx, n = 0, len(code)
    operators = r"+-*/<>=!:;,()[]{}"
    while idx < n:
        c = code[idx]
        if status == __TK_INITIAL:
            if c in string.whitespace:
                token.content = c
                tokens.append(token)
                token = Token()
                idx += 1
                continue
            elif c.isalpha() or c == "_":
                status = __TK_WORD
            elif c.isdigit():
                status = __TK_NUMBER
            elif c == '"':
                status = __TK_DQUOT
            elif c == "'":
                status = __TK_SQUOT
            elif c in operators:
                status = __TK_OPERATOR
            elif c == "#":
                status = __TK_PREPROC
            token.content += c
        elif status == __TK_WORD:
            if c.isalnum() or c == "_":
                token.content += c
            else:
                token.require_convert = True
                tokens.append(token)
                token = Token()
                status = __TK_INITIAL
                continue
        elif status == __TK_NUMBER:
            if c.isdigit():
                token.content += c
            else:
                token.require_convert = True
                tokens.append(token)
                token = Token()
                status = __TK_INITIAL
                continue
        elif status == __TK_DQUOT:
            token.content += c
            if c == '"':
                token.require_convert = True
                tokens.append(token)
                token = Token()
                status = __TK_INITIAL
        elif status == __TK_SQUOT:
            token.content += c
            if c == "'":
                token.require_convert = True
                tokens.append(token)
                token = Token()
                status = __TK_INITIAL
        elif status == __TK_OPERATOR:
            if c in operators:
                token.content += c
            else:
                token.require_convert = True
                tokens.append(token)
                token = Token()
                status = __TK_INITIAL
                continue
        elif status == __TK_PREPROC:
            token.content += c
            if c == "\n":
                tokens.append(token)
                token = Token()
                status = __TK_INITIAL
        else:
            raise ValueError("Unexpected character %s" % c)
        idx += 1

    if status != __TK_INITIAL:
        if not token.content.startswith("#") and token.content[0] not in string.whitespace:
            token.require_convert = True
        tokens.append(token)
    return tokens


def compile(path):
    with open(path, "r") as fin:
        code = "".join(fin.readlines())
    tokens: list[Token] = tokenize(code)
    macros = dict()
    gen = macro_generator()
    buffer = ""
    for token in tokens:
        if token.require_convert:
            if token.content not in macros:
                macros[token.content] = next(gen)
            buffer += macros[token.content]
        else:
            buffer += token.content
    buffer = "\n".join([ln.strip() for ln in buffer.split("\n") if ln.strip()])
    with open(path + ".diana", "w", encoding="utf8") as fout:
        for k, v in macros.items():
            fout.write(f"#define {v} {k}\n")
        fout.write(buffer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Diana C compiler")
    parser.add_argument("-i", "--inputs", type=str, nargs="+", help="source codes")
    args = parser.parse_args()
    for path in args.inputs:
        compile(path)