import ast
import operator as op
from database import SessionLocal, Memory

def tool_save_memory(key: str, value: str) -> dict:
    db = SessionLocal()
    record = db.query(Memory).filter(Memory.key == key).first()

    if record:
        record.value = value
    else:
        record = Memory(key=key, value=value)
        db.add(record)

    db.commit()
    db.close()
    return {"message": "Memory saved", "key": key, "value": value}


def tool_get_memory(key: str) -> dict:
    db = SessionLocal()
    record = db.query(Memory).filter(Memory.key == key).first()
    db.close()

    if record:
        return {"key": key, "value": record.value}
    return {"error": "No memory found for this key"}


operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}

def safe_eval(expr):
    def eval_(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        else:
            raise TypeError("Unsupported expression")

    node = ast.parse(expr, mode='eval').body
    return eval_(node)

def tool_calculate(expression: str) -> dict:
    try:
        result = safe_eval(expression)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}