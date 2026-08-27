'''tokanizer classes'''
class chartokenizer:
    def __init__(self, text):
        self.vocab = sorted(list(set(text)))
        self.stoi = {ch: i for i, ch in enumerate(self.vocab)}
        self.itos = {i: ch for i, ch in enumerate(self.vocab)}

    def encode(self, text):
        return [self.stoi[ch] for ch in text]

    def decode(self, tokens):
        return ''.join([self.itos[i] for i in tokens])
