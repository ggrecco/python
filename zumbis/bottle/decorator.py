def negrito(f):
    def envelope():
        return "<b>" + f() + "</b>"
    return envelope

def italico(f):
    def envelope():
        return "<i>" + f() + "</i>"
    return envelope

@italico
@negrito

def alo():
    return "Alô Mundo!"

print(alo())
