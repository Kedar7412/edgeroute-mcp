import subprocess
import json

proc = subprocess.Popen(['python', 'decision_engine_mcp.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)

def send(req):
    proc.stdin.write(json.dumps(req) + '\n')
    proc.stdin.flush()
    return json.loads(proc.stdout.readline())

init_req = {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2024-11-05', 'capabilities': {}, 'clientInfo': {'name': 'test-client', 'version': '1.0.0'}}}
resp = send(init_req)
print('Connected to:', resp['result']['serverInfo']['name'])

proc.stdin.write(json.dumps({'jsonrpc': '2.0', 'method': 'notifications/initialized', 'params': {}}) + '\n')
proc.stdin.flush()

call_req = {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call', 'params': {'name': 'route_decision', 'arguments': {'context': 'fix syntax error in main.py'}}}
result = send(call_req)
print('Prediction Result:')
print(result['result']['content'][0]['text'])

proc.terminate()
