# Generated from YAPL.g4 by ANTLR 4.10
from Compiled.YAPLVisitor import YAPLVisitor
from symbolTable import Symbol_not_found
from expresion import Expresion
from error import printError

from semanticVisitor import symbolTable

class TemporalVar(object):
    counter = 0
    
    def __init__(self):
        self.id = TemporalVar.counter
        TemporalVar.counter += 1
        
        self.code = ''
        
    def setCode(self, code):
        print(str(self.id) + ' : \n' + code + '\n')
        self.code = code
    
    def __str__(self):
        return '(' + str(self.id) + ')'       

current_class = ''
current_method = ''
basic_types = ['Int','String','Bool']

def addLineToIntermidiateCode(line):
    file = open('./intermediate_code.txt', 'a')
    file.write(line)
    file.truncate()

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.
    
    
class Visitor(YAPLVisitor):
    
    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#my_class.
    def visitMy_class(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#AtributeFeature.
    def visitAtributeFeature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#inStringExpr.
    def visitInStringExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#voidExpr.
    def visitVoidExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#InstanceExpr.
    def visitInstanceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#BracketsExpr.
    def visitBracketsExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#outIntExpr.
    def visitOutIntExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#inBoolExpr.
    def visitInBoolExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunctionExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#LetExpr.
    def visitLetExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#outBoolExpr.
    def visitOutBoolExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#outStringExpr.
    def visitOutStringExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#idExpr.
    def visitIdExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#call.
    def visitCall(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#inIntExpr.
    def visitInIntExpr(self, ctx):
        return self.visitChildren(ctx)
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx):
        expressions = []
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal = TemporalVar()
        temporal_end = TemporalVar()
        temporal.setCode("if NOT " + str(expressions[0]) + " goto " + str(temporal_end) + "\n" + expressions[1].code + "\ngoto " + str(temporal))
        temporal_end.setCode('')
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#ifelseExpr.
    def visitIfelseExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("if " + str(expressions[0]) + " goto " + str(expressions[1]) + " \ngoto " + str(expressions[2]))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#sumExpr.
    def visitSumExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' + ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#minusExpr.
    def visitMinusExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' - ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' * ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' / ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#unaryExpr.
    def visitUnaryExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + ' = -' + str(self.visit(ctx.expr())))
        return temporal

    # Visit a parse tree produced by YAPLParser#lessThanExpr.
    def visitLessThanExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' < ' + str(expressions[1]))
        return temporal

    # Visit a parse tree produced by YAPLParser#parensExpr.
    def visitParensExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + ' = ' + str(self.visit(ctx.expr())))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' <= ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' == ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + ' =  NOT' + str(self.visit(ctx.expr())))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx):
        return ctx.getText()
    
    # Visit a parse tree produced by YAPLParser#intExpr.
    def visitIntExpr(self, ctx):
        return ctx.getText()
    
    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx):
        return 'true'
    
    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx):
        return 'false'

