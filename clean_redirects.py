# clean_redirects.py
import os
import sys

MAX_RULES = 95  # Stay safely under Cloudflare's likely limit of 100 dynamic rules
input_filepath = 'site/_redirects'
output_filepath = 'site/_redirects_cleaned'

print(f"--- Starting redirect cleanup for {input_filepath} ---")

if not os.path.exists(input_filepath):
    print(f"Warning: Input file {input_filepath} not found. Skipping cleanup.")
    sys.exit(0) # Exit cleanly if no redirects file was generated

seen_sources = set()
valid_rules = []
rule_count = 0

try:
    with open(input_filepath, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            stripped_line = line.strip()
            # Keep comments and blank lines
            if not stripped_line or stripped_line.startswith('#'):
                valid_rules.append(line.rstrip()) # Keep original line ending if possible, but strip trailing ws
                continue

            parts = stripped_line.split()
            if len(parts) >= 2:
                source = parts[0]
                destination = parts[1]

                # Basic loop check
                if source == destination:
                    print(f"Skipping self-redirect: {stripped_line}")
                    continue

                # Check duplicates and limit
                if source not in seen_sources:
                    if rule_count < MAX_RULES:
                        seen_sources.add(source)
                        valid_rules.append(stripped_line)
                        rule_count += 1
                    else:
                        # Stop adding once limit is reached
                        print(f"Max rule limit ({MAX_RULES}) reached. Skipping: {stripped_line}")
                else:
                     print(f"Skipping duplicate source: {stripped_line}")
            else:
                # Keep potentially malformed lines? Maybe skip them? Let's skip for now.
                print(f"Skipping malformed line: {stripped_line}")

    print(f"--- Writing {len(valid_rules)} lines ({rule_count} rules processed) to {output_filepath} ---")
    with open(output_filepath, 'w', encoding='utf-8') as f_out:
        for rule in valid_rules:
            f_out.write(rule + '\n') # Ensure newline at the end

    # Replace original with cleaned version
    os.replace(output_filepath, input_filepath)
    print(f"--- Redirects cleaned successfully. Kept {rule_count} rules. ---")

except Exception as e:
    print(f"Error during redirect cleanup: {e}")
    sys.exit(1) # Exit with error status