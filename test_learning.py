import subprocess, json
p = subprocess.Popen(['python', 'decision_engine_mcp.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)
def send(req):
    p.stdin.write(json.dumps(req) + '\n'); p.stdin.flush(); return json.loads(p.stdout.readline())
send({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2024-11-05', 'capabilities': {}, 'clientInfo': {'name': 't', 'version': '1'}}})
p.stdin.write(json.dumps({'jsonrpc': '2.0', 'method': 'notifications/initialized', 'params': {}}) + '\n'); p.stdin.flush()

print('1. Logging 10 user acceptance events (teaching it: fix syntax -> edit_file)...')
for _ in range(10):
    send({'jsonrpc': '2.0', 'id': 2, 'method': 'tools/call', 'params': {'name': 'log_outcome', 'arguments': {'context': 'fix syntax error in file', 'selected_action': 'edit_file', 'accepted': True}}})

print('2. Running local gradient descent (train_head)...')
train_res = send({'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'train_head', 'arguments': {'epochs': 15}}})
print(train_res['result']['content'][0]['text'])

print('3. Testing prediction again after learning:')
decision = send({'jsonrpc': '2.0', 'id': 4, 'method': 'tools/call', 'params': {'name': 'route_decision', 'arguments': {'context': 'fix syntax error in file'}}})
print(decision['result']['content'][0]['text'])
p.terminate()
