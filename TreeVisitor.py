if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor

class TreeVisitor(FunxVisitor):
    def __init__(self):
        self.nivell = 0

    def visitMul(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'MUL(*)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitDiv(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'DIV(/)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitMod(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'MOD(%)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitSum(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'SUM(+)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitSub(self, ctx):
        l = list(ctx.getChildren())
        print('  ' *  self.nivell + 'SUB(-)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              FunxParser.symbolicNames[l[0].getSymbol().type] +
              '(' +l[0].getText() + ')')
