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

class SymbolTable:
    def __init__(self):
        self.symbols = [{}]
        self.scope = 1
    
    def addScope(self):
        self.symbols.insert(0, {})
        self.scope+=1
    
    def removeScope(self):
        self.symbols.pop(0)
        self.scope-=1
    
    def insert(self, ident, value):
        for scope in self.symbols:
            if scope.keys().__contains__(ident):
                scope[ident] = value
                return
        self.symbols[0][ident] = value
    
    def lookup(self, ident):
        for scope in self.symbols:
            if scope.keys().__contains__(ident):
                return scope[ident]
        return "ERROR"

symbolTable = SymbolTable()

class EvalVisitor(FunxVisitor):
    def __init__(self):
        self.level = 0

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return
        r = self.visit(l[0])
        if str(r) != "None":
            print(r)

    # STATEMENTS

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        symbolTable.insert(l[0].getText(), self.visit(l[2]))
    
    def visitIf(self, ctx):
        l = list(ctx.getChildren())
        symbolTable.addScope()
        if self.visit(l[1]):
            r = self.visit(l[3])
            symbolTable.removeScope()
            return r
    
    def visitIfElse(self, ctx):
        l = list(ctx.getChildren())
        symbolTable.addScope()
        r = "None"
        if self.visit(l[1]):
            r = self.vist(l[3])
        else:
            r = self.visit(l[7])
        symbolTable.removeScope()
        return r
    
    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        symbolTable.addScope()
        r = "" 
        while self.visit(l[1]):
            r += self.visit(l[3]) + "\n"
        symbolTable.removeScope()
        r = r.removesuffix("\n")
        return r
        

    def visitRecStmt(self, ctx):
        l = list(ctx.getChildren())
        r0 = str(self.visit(l[0]))
        r1 = str(self.visit(l[1]))
        if r0 != "None":
            return r0 + "\n" + r1
        else:
            return r1
    
    def visitExprs(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])

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
        val = symbolTable.lookup(ident)
        if val == "ERROR":
            return "ERROR: Vairable '" + ident + "' doesn't exist in this scope"
        return val

    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())
