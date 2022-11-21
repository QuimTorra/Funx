if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor

ops = {
  '+': lambda x, y: x+y,
  '-': lambda x, y: x-y,
  '*': lambda x, y: x*y,
  '/': lambda x, y: x/y,
  '%': lambda x, y: x%y,
  '^': lambda x, y: x**y,
  '=': lambda x, y: x==y,
  '!=': lambda x, y: x!=y,
  '<': lambda x, y: x<y,
  '>': lambda x, y: x>y,
  '<=': lambda x, y: x<=y,
  '>=': lambda x, y: x>=y
}

class EvalVisitor(FunxVisitor):
    def __init__(self):
        self.nivell = 0

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))

    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        op = ops[l[1].getText()]
        return op(self.visit(l[0]), self.visit(l[2]))

    def visitRel(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
          return l[0].getText()
        op = ops[l[1].getText()]
        return op(self.visit(l[0]), self.visit(l[2]))

    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())
