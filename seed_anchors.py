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
        "clientInfo": {"name": "seeder", "version": "1"}
    }
})
p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}) + "\n")
p.stdin.flush()

# Realistic dataset across all 5 actions
DATASET = [
    # 0: run_terminal_command
    ("run pytest tests", "run_terminal_command"),
    ("pip install requirements", "run_terminal_command"),
    ("npm run build", "run_terminal_command"),
    ("execute bash script", "run_terminal_command"),
    ("start docker container", "run_terminal_command"),
    ("run gradle build", "run_terminal_command"),

    # 1: edit_file
    ("fix syntax error in main.py", "edit_file"),
    ("add error handling to controller", "edit_file"),
    ("refactor user authentication method", "edit_file"),
    ("update config json file", "edit_file"),
    ("change button color in styles.css", "edit_file"),
    ("modify database schema migration", "edit_file"),

    # 2: search_codebase
    ("find where getUser is defined", "search_codebase"),
    ("search all references to API_KEY", "search_codebase"),
    ("locate the authentication controller", "search_codebase"),
    ("find file containing stripe webhook", "search_codebase"),
    ("grep for deprecation warnings", "search_codebase"),

    # 3: ask_user_clarification
    ("which database do you want to use", "ask_user_clarification"),
    ("should I delete this existing directory", "ask_user_clarification"),
    ("which framework version are you targeting", "ask_user_clarification"),
    ("please confirm if this migration is safe", "ask_user_clarification"),

    # 4: commit_git_changes
    ("git commit with message fix login", "commit_git_changes"),
    ("commit all staged files", "commit_git_changes"),
    ("git add and commit feature branch", "commit_git_changes"),
    ("save checkpoint commit to repository", "commit_git_changes")
]

print("Seeding 25 baseline patterns...")
for text, action in DATASET:
    send({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "log_outcome",
            "arguments": {"context": text, "selected_action": action, "accepted": True}
        }
    })

print("Training baseline weights (50 epochs)...")
train_res = send({
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {"name": "train_head", "arguments": {"epochs": 250, "batch_size": 32}}
})
print(train_res["result"]["content"][0]["text"])

p.terminate()