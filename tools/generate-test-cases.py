#!/usr/bin/env python3
import json,sys
from core.agent import TestGenerationAgent
agent=TestGenerationAgent()
req=json.load(sys.stdin)
res=agent.generate(req["source"],req.get("language","python"),req.get("max_cases",20),req.get("focus"))
print(json.dumps(res))
