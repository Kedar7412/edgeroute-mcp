import subprocess
import json
import time

p = subprocess.Popen(
    ["python", "decision_engine_mcp.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
    bufsize=1
)

def send(req):
    p.stdin.write(json.dumps(req) + "\n")
    p.stdin.flush()
    return json.loads(p.stdout.readline())

send({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "interactive", "version": "1"}
    }
})
p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}) + "\n")
p.stdin.flush()

print("\n" + "="*50)
print("EdgeRoute Live Decision Tester")
print("Type any prompt (or 'stats' for ROI report, 'exit' to quit)")
print("="*50 + "\n")

while True:
    try:
        user_input = input("Enter prompt > ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            break
        if user_input.lower() == "stats":
            res = send({"jsonrpc": "2.0", "id": 99, "method": "tools/call", "params": {"name": "get_savings_report", "arguments": {}}})
            print(res["result"]["content"][0]["text"])
            continue

        start = time.perf_counter()
        res = send({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "route_decision", "arguments": {"context": user_input}}})
        elapsed_ms = (time.perf_counter() - start) * 1000

        data = json.loads(res["result"]["content"][0]["text"])
        status = "[CONFIDENT - ROUTED]" if not data["abstained"] else "[ABSTAINED - FALLBACK]"
        print(f"\n{status}")
        print(f"Predicted Action : {data['action']}")
        print(f"Confidence       : {data['confidence'] * 100:.1f}%")
        print(f"Execution Latency: {elapsed_ms:.2f} ms")
        print("Probabilities    :")
        for act, prob in data["probabilities"].items():
            print(f"  - {act.ljust(25)}: {prob * 100:.1f}%")
        print("-" * 50)
    except (KeyboardInterrupt, EOFError):
        break

p.terminate()