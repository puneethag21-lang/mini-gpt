text = "hello world i am puneetha aiml student i build a projects and contribute  to opensurce";
tokenizer = chartokenizer(text)
encoded = tokenizer.encode(text)
print(encoded);
decoded = tokenizer.decode(encoded)
print(decoded);
