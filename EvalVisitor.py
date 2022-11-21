if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor

ops = {
    # BINOPS
  '+': lambda x, y: x+y,
  '-': lambda x, y: x-y,
  '*': lambda x, y: x*y,
  '/': lambda x, y: x/y,
  '%': lambda x, y: x%y,
  '^': lambda x, y: x**y,
    # LOGIC OPS
  '=': lambda x, y: x==y,
  '!=': lambda x, y: x!=y,
  '<': lambda x, y: x<y,
  '>': lambda x, y: x>y,
  '<=': lambda x, y: x<=y,
  '>=': lambda x, y: x>=y
}

symbols = {}

class EvalVisitor(FunxVisitor):
    def __init__(self):
        self.nivell = 0

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return
        print(self.visit(l[0]))

    # STATEMENTS

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        symbols[l[0].getText()] = self.visit(l[2])
        return symbols[l[0].getText()]

    # EXPRESIONS

    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        if l[0].getText() == '(':
            return self.visit(l[1])
        op = ops[l[1].getText()]
        return op(self.visit(l[0]), self.visit(l[2]))

    def visitRel(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
          return l[0].getText()
        op = ops[l[1].getText()]
        return op(self.visit(l[0]), self.visit(l[2]))

    def visitIdent(self, ctx):
        l = list(ctx.getChildren())
        ident = l[0].getText()
        if not symbols.keys().__contains__(ident):
            symbols[ident] = 0
        return symbols[ident] 
        


    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())
