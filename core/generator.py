import ast
from .analyzer import analyze_python


def _case(case_id, target, category, inputs, expected, rationale, line):
    return {"id":case_id,"target":target,"category":category,"inputs":inputs,"expected":expected,"rationale":rationale,"provenance":{"source_line":line,"method":"deterministic-ast-analysis"}}


def generate_python_tests(source: str, max_cases: int = 20, focus: str | None = None) -> dict:
    analysis=analyze_python(source)
    tree=ast.parse(source)
    cases=[]
    for fn in analysis["functions"]:
        if focus and focus.lower() not in fn["name"].lower():
            continue
        if fn["parameters"]:
            values={p: 0 for p in fn["parameters"]}
            cases.append(_case(f"{fn['name']}-baseline",fn["name"],"baseline",values,"function returns or completes without an input-validation failure","Baseline coverage for the callable's parameter surface.",fn["line"]))
            values={p: 1 for p in fn["parameters"]}
            cases.append(_case(f"{fn['name']}-positive",fn["name"],"boundary-positive",values,"function follows the positive/non-zero path when applicable","Deterministic positive-value probe for numeric-like parameters.",fn["line"]))
        else:
            cases.append(_case(f"{fn['name']}-no-args",fn["name"],"baseline",{},"function completes according to its contract","Baseline coverage for a zero-argument callable.",fn["line"]))
        node=next((n for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name==fn["name"]),None)
        if node and any(isinstance(n,ast.If) for n in ast.walk(node)):
            cases.append(_case(f"{fn['name']}-branch",fn["name"],"branch",{p:0 for p in fn["parameters"]},"conditional behavior is exercised and observable","The function contains an explicit conditional branch.",fn["line"]))
    cases=cases[:max_cases]
    return {"cases":cases,"count":len(cases),"analysis":analysis,"limitations":["Generated cases are proposals; source code is not executed.","Generic numeric probes may not satisfy domain-specific preconditions."]}
