# AI Agent Tooling & Validation

This repository is dedicated to building tools that support, validate, and enhance the performance of AI software engineering agents. The goal is to ensure that agents operate reliably, consistently, and in accordance with their core operational principles.

## Agent Compliance Checker

The primary tool in this repository is the `compliance_checker.py`, a script designed to automatically verify that an agent's output log conforms to a predefined set of rules.

### Purpose

An AI agent's behavior is governed by a strict set of protocols, which are detailed in the `.github/copilot-instructions.md` file. The compliance checker's job is to parse an agent's log file and flag any deviations from these critical rules, acting as an automated quality assurance gate.

### Enforced Rules

Currently, the checker validates the following rules:

1.  **Zero-Confirmation Policy**: It ensures the agent never asks for permission before acting. It flags questions like "Shall I proceed?" or "Is it okay if I...?".
2.  **Tool Usage Pattern**: It verifies that every tool execution command is immediately preceded by a correctly formatted `<summary>` block, which is required for documentation and traceability.

### Usage

To use the checker, run the script from your terminal and provide the path to the agent's log file as an argument.

**Prerequisites:**
*   Python 3.x

**Command:**
```bash
python compliance_checker.py <path_to_your_agent_log.txt>
```

**Example:**
```bash
python compliance_checker.py sample_agent_log.txt
```

#### Sample Output (for a file with violations)
```
Found 4 compliance violations in 'sample_agent_log.txt':
- Line 16: Potential permission-seeking question found. Violation of ZERO-CONFIRMATION POLICY. -> "Shall I proceed with reading the file?"
- Line 26: Potential permission-seeking question found. Violation of ZERO-CONFIRMATION POLICY. -> "Next step: Patch the test... Would you like me to proceed?"
- Line 44: Potential permission-seeking question found. Violation of ZERO-CONFIRMATION POLICY. -> "Is it okay if I create a new file now?"
- Line 19: Tool execution is not preceded by a closing </summary> tag. Violation of Tool Usage Pattern.
```

#### Sample Output (for a compliant file)
```
No compliance violations found in 'compliant_log.txt'. Congratulations!
```

## Contributing

As the capabilities of the agent grow, this toolset will be expanded. Contributions are welcome, especially in the following areas:
-   Adding more rule checks to the compliance script.
-   Improving the accuracy of the existing checks.
-   Developing new tools for agent performance analysis.
