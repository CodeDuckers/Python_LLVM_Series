from abc import ABC, abstractmethod
from enum import Enum

class NodeType(Enum):
    Program = "Program"

    # Statements
    ExpressionStatement = "ExpressionStatement"

    # Expressions
    InfixExpression = "InfixExpression"

    # Literals
    IntegerLiteral = "IntegerLiteral"
    FloatLiteral = "FloatLiteral"


class Node(ABC):
    @abstractmethod
    def type(self) -> NodeType:
        """ Returns back the NodeType """
        pass

    @abstractmethod
    def json(self) -> dict:
        """ Returns back the JSON representation of this AST node """
        pass


class Statement(Node):
    pass

class Expression(Node):
    pass

class Program(Node):
    """ The root node for the AST """
    def __init__(self) -> None:
        self.statements: list[Statement] = []

    def type(self) -> NodeType:
        return NodeType.Program
    
    def json(self) -> dict:
        return {
            "type": self.type().value,
            "statements": [{stmt.type().value: stmt.json()} for stmt in self.statements]
        }

# region Statements
class ExpressionStatement(Statement):
    def __init__(self, expr: Expression = None) -> None:
        self.expr: Expression = expr

    def type(self) -> NodeType:
        return NodeType.ExpressionStatement
    
    def json(self) -> dict:
        return {
            "type": self.type().value,
            "expr": self.expr.json()
        }
# endregion
    
# region Expressions
class InfixExpression(Expression):
    def __init__(self, left_node: Expression, operator: str, right_node: Expression = None):
        self.left_node: Expression = left_node
        self.operator: str = operator
        self.right_node: Expression = right_node

    def type(self) -> NodeType:
        return NodeType.InfixExpression
    
    def json(self) -> dict:
        return {
            "type": self.type().value,
            "left_node": self.left_node.json(),
            "operator": self.operator,
            "right_node": self.right_node.json()
        }
# endregion

# region Literals
class IntegerLiteral(Expression):
    def __init__(self, value: int = None) -> None:
        self.value: int = value
    
    def type(self) -> NodeType:
        return NodeType.IntegerLiteral
    
    def json(self) -> dict:
        return {
            "type": self.type().value,
            "value": self.value
        }
    
class FloatLiteral(Expression):
    def __init__(self, value: float = None) -> None:
        self.value: float = value
    
    def type(self) -> NodeType:
        return NodeType.FloatLiteral
    
    def json(self) -> dict:
        return {
            "type": self.type().value,
            "value": self.value
        }
# endregion