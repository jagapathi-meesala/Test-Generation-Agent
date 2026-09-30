#!/usr/bin/env python3
import json,sys
from core.agent import TestGenerationAgent
agent=TestGenerationAgent()
req=json.load(sys.stdin)
res=agent.validate(req["cases"])
print(json.dumps(res))
