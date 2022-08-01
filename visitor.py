# Generated from __my__.g4 by ANTLR 4.10
from Compiled.__my__Visitor import __my__Visitor
from symbolTable import SymbolsTable

symbolTable = SymbolsTable()
# This class defines a complete generic visitor for a parse tree produced by __my__Parser.

class Visitor(__my__Visitor):

    # Visit a parse tree produced by __my__Parser#my_class.
    def visitMy_class(self, ctx):
        class_name = ctx.TYPE()[0]
        symbolTable.AddSymbol(
            str(class_name),
            'Class, ' + str(class_name), 
            'Global'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#MethodFeature.
    def visitMethodFeature(self, ctx):
        func_name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(func_name),
            'Feature, ' + str(type),
            'Bracket Feature'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#DeclarationFeature.
    def visitDeclarationFeature(self, ctx):
        func_name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(func_name),
            'Feature, ' + str(type),
            'Arrow Feature'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#formal.
    def visitFormal(self, ctx):
        var_name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(var_name),
            str(type),
            'Function Parameter'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#divideExpr.
    def visitDivideExpr(self, ctx):
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        print('division between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        else: 
            print('Error is returned\n\n' + ctx.getText())
            return {'type':'ERROR', 'value':ctx.getText()}


    # Visit a parse tree produced by __my__Parser#ifelseExpr.
    def visitIfelseExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#intExpr.
    def visitIntExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'Int', 'value':ctx.getText()}


    # Visit a parse tree produced by __my__Parser#FunctionExpr.
    def visitFunctionExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#voidExpr.
    def visitVoidExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#trueExpr.
    def visitTrueExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'bool', 'value':ctx.getText()}


    # Visit a parse tree produced by __my__Parser#MethodExpr.
    def visitMethodExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#LetExpr.
    def visitLetExpr(self, ctx):
        ids = ctx.ID()
        types = ctx.TYPE()
        for index in range(0, len(ids)):
            symbolTable.AddSymbol(
                str(ids[index]),
                str(types[index]),
                'Let Declaration Variable' if index == 0  else 'Let Declaration parameter'
            )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#InstanceExpr.
    def visitInstanceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#lessThanExpr.
    def visitLessThanExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#BracketsExpr.
    def visitBracketsExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#parensExpr.
    def visitParensExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#minusExpr.
    def visitMinusExpr(self, ctx):
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        print('substraction between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        else: 
            print('Error is returned\n\n' + ctx.getText())
            return {'type':'ERROR', 'value':ctx.getText()}


    # Visit a parse tree produced by __my__Parser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#timesExpr.
    def visitTimesExpr(self, ctx):
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        print('multiplication between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        else: 
            print('Error is returned\n\n' + ctx.getText())
            return {'type':'ERROR', 'value':ctx.getText()}

    # Visit a parse tree produced by __my__Parser#stringExpr.
    def visitStringExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'String', 'value':ctx.getText()}


    # Visit a parse tree produced by __my__Parser#negateExpr.
    def visitNegateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#notExpr.
    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#sumExpr.
    def visitSumExpr(self, ctx):
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        print('sum between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        #TODO
        elif children[0].get('type') == 'String' and children[1].get('type') == 'String':
            print('String is returned\n\n')
            return {'type':'String', 'value':ctx.getText()}
        else: 
            print('Error is returned\n\n')
            return {'type':'ERROR', 'value':ctx.getText()}
    # Visit a parse tree produced by __my__Parser#whileExpr.
    def visitWhileExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by __my__Parser#falseExpr.
    def visitFalseExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'bool', 'value':ctx.getText()}


    # Visit a parse tree produced by __my__Parser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by __my__Parser#idExpr.
    def visitIdExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'ID', 'value':ctx.getText()}


    # Visit a parse tree produced by __my__Parser#equalExpr.
    def visitEqualExpr(self, ctx):
        return self.visitChildren(ctx)