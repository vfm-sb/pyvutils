

def custom_title(string: str, exclusions: list) -> str:
    parts = string.split()
    customized_parts = []
    for part in parts:
        if part in exclusions:
            customized_parts.append(part)
        else:
            customized_parts.append(part.capitalize())
    return " ".join(customized_parts)
