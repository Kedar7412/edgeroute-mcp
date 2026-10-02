\# EdgeRoute ⚡



\[!\[License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

\[!\[Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

\[!\[Protocol: MCP](https://img.shields.io/badge/protocol-MCP-green.svg)](https://modelcontextprotocol.io/)



> A sub-millisecond, self-improving "System 1" edge decision engine for AI IDEs and agents (Kiro, Cursor, Claude Code, Windsurf, Cline).



EdgeRoute is a local Model Context Protocol (MCP) server that evaluates developer intent in \*\*under 2 milliseconds\*\* using an on-device linear projection head. Instead of sending every repetitive routing decision to expensive cloud LLMs, EdgeRoute classifies actions locally, abstains when uncertain, and continuously fine-tunes itself on your machine via online stochastic gradient descent (SGD).



\---



\## 🚀 Key Advantages



\- \*\*⚡ Sub-Millisecond Decisions:\*\* Evaluates state in `< 2 ms` on local CPU (L1/L2 cache), with zero network latency.

\- \*\*🛡️ Calibrated Abstention Gate:\*\* Rejects false positives by abstaining whenever confidence is below `60%`, delegating complex reasoning to standard LLMs.

\- \*\*🔄 Local Experience Replay \& On-Device SGD:\*\* Automatically adapts to your unique workflow by logging outcomes to an encrypted local SQLite buffer and running background mini-batch SGD.

\- \*\*📊 Measurable ROI Telemetry:\*\* Tracks lifetime tokens saved, developer latency eliminated, and estimated cloud cost reductions in real time.

\- \*\*🔒 100% Private \& Offline:\*\* Never transmits your code, prompts, or weights to external cloud servers.



\---



\## 🏛️ Architecture

