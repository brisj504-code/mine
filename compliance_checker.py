import re
import sys

def check_permission_questions(lines):
    """
    Checks for violations of the "ZERO-CONFIRMATION POLICY".
    Flags any lines that appear to be asking for permission.
    """
    violations = []
    # Regex to find common permission-seeking questions.
    # It's case-insensitive and looks for phrases followed by a question mark.
    permission_pattern = re.compile(
        r'^(.*(shall|should|can|may|would you like me to|is it okay if|do you want me to).*\?)$',
        re.IGNORECASE
    )

    for i, line in enumerate(lines, 1):
        if permission_pattern.search(line):
            violations.append(
                f"Line {i}: Potential permission-seeking question found. "
                f"Violation of ZERO-CONFIRMATION POLICY. -> \"{line.strip()}\""
            )
    return violations

def check_tool_usage_pattern(lines):
    """
    Checks that every tool execution call is preceded by a summary block.
    Flags `[Execute immediately without confirmation]` if the previous non-empty line
    is not `</summary>`.
    """
    violations = []
    # Find the indices of all lines with the execution command
    execution_indices = [i for i, line in enumerate(lines) if '[Execute immediately without confirmation]' in line]

    for i in execution_indices:
        # Find the previous non-empty line
        prev_line_index = i - 1
        while prev_line_index >= 0 and not lines[prev_line_index].strip():
            prev_line_index -= 1

        # Check if the previous line is valid
        if prev_line_index < 0 or '</summary>' not in lines[prev_line_index]:
            violations.append(
                f"Line {i + 1}: Tool execution is not preceded by a closing </summary> tag. "
                f"Violation of Tool Usage Pattern."
            )
    return violations


def main(filename):
    """
    Main function to run the compliance checks on a given log file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at '{filename}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    all_violations = []
    all_violations.extend(check_permission_questions(lines))
    all_violations.extend(check_tool_usage_pattern(lines))

    if all_violations:
        print(f"Found {len(all_violations)} compliance violations in '{filename}':")
        for violation in all_violations:
            print(f"- {violation}")
    else:
        print(f"No compliance violations found in '{filename}'. Congratulations!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compliance_checker.py <path_to_log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    main(log_file)
