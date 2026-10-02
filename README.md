\# EdgeRoute ⚡



\[!\[License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

\[!\[Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

\[!\[Protocol: MCP](https://img.shields.io/badge/protocol-MCP-green.svg)](https://modelcontextprotocol.io/)



> A sub-millisecond, self-improving "System 1" edge decision engine for AI IDEs and agents (Kiro, Cursor, Claude Code, Windsurf, Cline).



EdgeRoute is a local Model Context Protocol (MCP) server that evaluates developer intent in under 2 milliseconds using an on-device linear projection head. Instead of sending every repetitive routing decision to expensive cloud LLMs, EdgeRoute classifies actions locally, abstains when uncertain, and continuously fine-tunes itself on your machine via online stochastic gradient descent (SGD).



\---



\## 🚀 Key Advantages



\- ⚡ Sub-Millisecond Decisions: Evaluates state in < 2 ms on local CPU (L1/L2 cache), with zero network latency.

\- 🛡️ Calibrated Abstention Gate: Rejects false positives by abstaining whenever confidence is below 60%, delegating complex reasoning to standard LLMs.

\- 🔄 Local Experience Replay \& On-Device SGD: Automatically adapts to your unique workflow by logging outcomes to an encrypted local SQLite buffer and running background mini-batch SGD.

\- 📊 Measurable ROI Telemetry: Tracks lifetime tokens saved, developer latency eliminated, and estimated cloud cost reductions in real time.

\- 🔒 100% Private \& Offline: Never transmits your code, prompts, or weights to external cloud servers.



\---



\## 🏛️ Architecture



User Prompt / Code Context

&#x20;          │

&#x20;          ▼

\[ Deterministic Feature Hasher ]  (zlib CRC32 / 128-d Vector)

&#x20;          │

&#x20;          ▼

\[ Linear Softmax Head (CPU) ]     (< 0.5 ms execution)

&#x20;          │

&#x20;    ┌─────┴─────────────────────┐

&#x20;    ▼                           ▼

Confidence >= 60%           Confidence < 60%

Instant Tool Execution      Abstain (Fallback to Cloud LLM)

&#x20;    │

&#x20;    ▼

\[ User Feedback Signal ]

&#x20;    │

&#x20;    ▼

\[ Local SQLite Replay Buffer ]

&#x20;    │

&#x20;    ▼ (Continuous Background Daemon)

\[ Mini-Batch SGD Weight Update ]



\---



\## 📦 Quickstart



\### 1. Clone \& Setup



git clone https://github.com/YOUR\_USERNAME/edgeroute-mcp.git

cd edgeroute-mcp

python -m venv venv



Activate virtual environment:

\- Windows: venv\\Scripts\\activate

\- macOS / Linux: source venv/bin/activate



\### 2. Install Dependencies



pip install -r requirements.txt



\### 3. Seed Baseline Intelligence



python seed\_anchors.py



\### 4. Interactive Live Test



python interactive.py



\---



\## 🔌 Platform Setup Guides



\### 1. Kiro

Add to your Kiro user config (Ctrl + Shift + P → Kiro: Open user MCP config (JSON)):



{

&#x20; "mcpServers": {

&#x20;   "edgeroute": {

&#x20;     "command": "python",

&#x20;     "args": \["/absolute/path/to/decision\_engine\_mcp.py"],

&#x20;     "disabled": false,

&#x20;     "autoApprove": \["\*"]

&#x20;   }

&#x20; }

}



To make Kiro automatically query EdgeRoute on every prompt without manual commands, create .kiro/steering/edgeroute.md:



\---

inclusion: always

\---

Before taking actions, query route\_decision from edgeroute. If abstained is false, follow the recommended action. Log outcomes using log\_outcome.



\---



\### 2. Cursor

Create or edit .cursor/mcp.json in your workspace root:



{

&#x20; "mcpServers": {

&#x20;   "edgeroute": {

&#x20;     "command": "python",

&#x20;     "args": \["/absolute/path/to/decision\_engine\_mcp.py"]

&#x20;   }

&#x20; }

}



\---



\### 3. Claude Desktop

Add to your Claude Desktop configuration file:

\- Windows: %APPDATA%\\Claude\\claude\_desktop\_config.json

\- macOS: \~/Library/Application Support/Claude/claude\_desktop\_config.json



{

&#x20; "mcpServers": {

&#x20;   "edgeroute": {

&#x20;     "command": "python",

&#x20;     "args": \["/absolute/path/to/decision\_engine\_mcp.py"]

&#x20;   }

&#x20; }

}



\---



\### 4. Claude Code (CLI)

Add to your global Claude CLI configuration (\~/.claude.json):



{

&#x20; "mcpServers": {

&#x20;   "edgeroute": {

&#x20;     "command": "python",

&#x20;     "args": \["/absolute/path/to/decision\_engine\_mcp.py"]

&#x20;   }

&#x20; }

}



\---



\### 5. Windsurf / Codeium

Open Settings → MCP Servers and add:



{

&#x20; "mcpServers": {

&#x20;   "edgeroute": {

&#x20;     "command": "python",

&#x20;     "args": \["/absolute/path/to/decision\_engine\_mcp.py"]

&#x20;   }

&#x20; }

}



\---



\### 6. VS Code (Cline / Roo Code)

In the Cline MCP settings tab, click Add New MCP Server and paste the JSON configuration.



\---



\## 🛠️ MCP Tools Reference



\- route\_decision (context: string): Evaluates prompt context in < 2 ms and returns top action, probabilities, and abstention status.

\- log\_outcome (context: string, selected\_action: string, accepted: bool): Logs user acceptance or override into the local SQLite replay buffer for future fine-tuning.

\- train\_head (epochs: int, batch\_size: int): Executes local mini-batch SGD on accumulated experience and commits updated weights.

\- get\_savings\_report (): Returns a lifetime ROI summary showing tokens saved, time saved, and monetary value generated.



\---



\## 📄 License



Distributed under the MIT License. See LICENSE for more information.

