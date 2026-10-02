import subprocess
import json

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

# Init handshake
send({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "roi-test", "version": "1"}
    }
})
p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}) + "\n")
p.stdin.flush()

print("1. Training high-confidence pattern...")
for _ in range(30):
    send({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "log_outcome",
            "arguments": {
                "context": "compile and run terminal command",
                "selected_action": "run_terminal_command",
                "accepted": True
            }
        }
    })

send({
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {"name": "train_head", "arguments": {"epochs": 30}}
})

print("2. Making fast routed decisions...")
for _ in range(15):
    send({
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {
            "name": "route_decision",
            "arguments": {"context": "compile and run terminal command"}
        }
    })

print("\n3. Generated Savings Report:")
report = send({
    "jsonrpc": "2.0",
    "id": 5,
    "method": "tools/call",
    "params": {"name": "get_savings_report", "arguments": {}}
})
print(report["result"]["content"][0]["text"])

p.terminate()