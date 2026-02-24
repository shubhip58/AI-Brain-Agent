import re

def normalize_key(text: str) -> str:
    text = text.lower()
    text = text.replace("?", "")
    text = text.replace("'", "")
    text = text.replace("’", "")
    text = text.replace("s ", " ")
    text = text.strip()
    return text

def agent_router(prompt: str):
    text = prompt.lower().strip()

    # MEMORY SAVE
    if "remember" in text or "save" in text:
        match = re.search(r"remember my (.+?) (is|if|=) (.+)", text)
        if match:
            key = normalize_key(match.group(1))
            value = match.group(3).strip()
            return "memory_save", key, value

    # MEMORY READ
    if "what is my" in text or "recall" in text:
        match = re.search(r"what is my (.+?)[\?]?$", text)
        if match:
            key = normalize_key(match.group(1))
            return "memory_read", key, None

    # CALCULATOR
    if "what is" in text or "calculate" in text:
        expression = (
            text.replace("what is", "")
                .replace("plus", "+")
                .replace("minus", "-")
                .replace("times", "*")
                .replace("into", "*")
                .replace("divided by", "/")
                .replace("?", "")
        )
        return "calculator", expression.strip(), None

    return None, None, None