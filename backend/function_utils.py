def save_function_file(name, language, code):
    ext = {"python": ".py", "javascript": ".js"}
    filename = f"../docker_functions/{language}_base/{name}{ext[language]}"
    with open(filename, 'w') as f:
        f.write(code)
    return filename
