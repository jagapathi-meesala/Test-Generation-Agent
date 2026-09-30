import ast
from dataclasses import dataclass


@dataclass(frozen=True)
class FunctionInfo:
    name: str
    parameters: tuple[str, ...]
    has_return_annotation: bool
    branch_count: int
    line: int


def analyze_python(source: str) -> dict:
    if not isinstance(source, str) or not source.strip():
        raise ValueError("source must be a non-empty string")
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise ValueError(f"invalid Python syntax: {exc.msg} at line {exc.lineno}") from exc
    functions=[]
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            branches=sum(isinstance(n,(ast.If,ast.For,ast.While,ast.Try,ast.Match)) for n in ast.walk(node))
            params=tuple(a.arg for a in node.args.posonlyargs+node.args.args+node.args.kwonlyargs)
            functions.append(FunctionInfo(node.name,params,node.returns is not None,branches,node.lineno))
    functions.sort(key=lambda x:(x.line,x.name))
    return {"language":"python","functions":[f.__dict__ for f in functions],"function_count":len(functions)}
