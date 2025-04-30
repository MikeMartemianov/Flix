import re

# Все типы токенов
token_spec = [
    ("NUMBER",   r"\d+"),           # Числа
    ("STRING",   r'"[^"]*"'),       # Строки в кавычках
    ("ID",       r"[a-zA-Z_]\w*"),  # Имена переменных и функций
    ("ASSIGN",   r"="),             # Присваивание
    ("LPAREN",   r""),            # (
    ("RPAREN",   r""),            # )
    ("LBRACE",   r"\{"),            # {
    ("RBRACE",   r"\}"),            # }
    ("LBRACK",   r""),            # [
    ("RBRACK",   r""),            # ]
    ("DOT",      r"\."),            # .
    ("COMMA",    r","),             # ,
    ("COLON",    r":"),             # :
    ("PLUS",     r"\+"),            # +
    ("MINUS",    r"-"),             # -
    ("NEWLINE",  r"\n"),            # Перевод строки
    ("SKIP",     r"[ \t]+"),        # Пробелы и табы
    ("COMMENT",  r"#.*"),           # Комментарии
]

# Объединяем все токены в одно большое выражение
tok_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_spec)

def tokenize(code):
    tokens = []
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind in ("SKIP", "COMMENT"):
            continue
        tokens.append((kind, value))
    return tokens