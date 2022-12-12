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
  '>=': lambda x, y: x>=y,
  'and': lambda x, y: x and y,
  'or': lambda x, y: x or y,
  'not': lambda x: not x
}

class SymbolTable:
    def __init__(self):
        self.symbols = [{}]
        self.funcs = [{}]
        self.scope = 1
    
    def addScope(self):
        self.symbols.insert(0, {})
        self.scope+=1
    
    def removeScope(self):
        if len(self.symbols) == 1: return
        self.symbols.pop(0)
        self.scope-=1
    
    def insert(self, ident, value):
        if self.symbols[0].keys().__contains__(ident):
            self.symbols[0][ident] = value
            return
        self.symbols[0][ident] = value
    
    def insertFunx(self, ident, value):
        if self.funcs[0].keys().__contains__(ident):
            self.funcs[0][ident] = value
            return
        self.funcs[0][ident] = value
    
    def lookup(self, ident):
        if self.symbols[0].keys().__contains__(ident):
            return self.symbols[0][ident]
        if self.funcs[0].keys().__contains__(ident):
            return self.funcs[0][ident]
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

    def visitCLI(self, ctx):
        l = list(ctx.getChildren())
        script = l[0].getText()
        if script == ":scope":
            print(symbolTable.symbols)
        elif script == ":fns":
            print(symbolTable.funcs)

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        symbolTable.insert(l[0].getText(), self.visit(l[2]))
    
    # Declaration of a function
    def visitFunc(self, ctx):
        l = list(ctx.getChildren())
        ident = l[0].getText()
        args = self.visit(l[1])
        code = l[3]
        symbolTable.insertFunx(ident, (args, code))
    
    def visitIf(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            r = self.visit(l[3])
            return r
    
    def visitIfElse(self, ctx):
        l = list(ctx.getChildren())
        r = "None"
        if self.visit(l[1]):
            r = self.visit(l[3])
        else:
            r = self.visit(l[7])
        return r
    
    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        r = "" 
        cond = self.visit(l[1])
        if type(cond) == str:
            return cond
        while cond:
            rr = self.visit(l[3])
            r += rr if str(rr) != "None" else ""
            cond = self.visit(l[1])
        return r
        

    def visitRecStmt(self, ctx):
        l = list(ctx.getChildren())
        r0 = self.visit(l[0])
        if r0 != None:
          return r0
        r1 = self.visit(l[1])
        if r1 != None:
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
        a1 = self.visit(l[0])
        a2 = self.visit(l[2])
        if l[1].getText() == "/" and a2 == 0:
            return "ERROR: Division by 0"
        if type(a1) == str:
            return a1
        if type(a2) == str:
            return a2
        return op(a1, a2)

    def visitRel(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
          return l[0].getText()
        if l[0].getText() == 'not':
            return ops['not'](self.visit(l[1]))
        op = ops[l[1].getText()]
        a1 = self.visit(l[0])
        a2 = self.visit(l[2])
        if type(a1) == str:
            return a1
        if type(a2) == str:
            return a2
        return op(a1,a2)

    def visitIdentFN(self, ctx):
        l = list(ctx.getChildren())
        ident = l[0].getText()
        # FUNCTION
        sb = symbolTable.lookup(ident)
        if sb == "ERROR":
            symbolTable.removeScope()
            return "ERROR: Function '" + ident + "' was not declarated"
        args = sb[0]
        if len(args) != len(l[1:]):
            symbolTable.removeScope()
            return "ERROR: Function '" + ident + "' requires " + str(len(args)) + " arguments, but got " + str(len(l[1:]))
        
        vals = []
        for arg in l[1:]:
            vals.append(self.visit(arg))
        symbolTable.addScope()
        for (sym, val) in zip(args, vals):
            symbolTable.insert(sym, val)
        r = self.visit(sb[1])
        symbolTable.removeScope()
        return r


    def visitIdentVAR(self, ctx):
        l = list(ctx.getChildren())
        ident = l[0].getText()
        # VARIABLE 
        arg = symbolTable.lookup(ident)
        if arg == "ERROR":
            print(ident, symbolTable.symbols)
            return "ERROR: Vairable '" + ident + "' doesn't exist in this scope"
        return arg

    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())
    
    def visitArg(self, ctx):
        l = list(ctx.getChildren())
        ls = []
        for c in l:
            ls.append(c.getText())
        return ls
