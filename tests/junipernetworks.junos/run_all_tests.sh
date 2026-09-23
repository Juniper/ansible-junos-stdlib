#!/bin/bash

echo "Starting execution of all Ansible Junos playbooks..."
echo "-----------------------------------------------------"

# File to store passed test logs
PASS_LOG="junos_passed_tests.log"
> "$PASS_LOG"  # Clear previous contents

# Loop through all *.yml playbooks
for file in pb.juniper_junos_*.yml; do
  echo "Running $file"
  ansible-playbook -i inventory "$file"
  status=$?

  if [ $status -ne 0 ]; then
    echo "❌ $file failed with status $status"
  else
    echo "✅ $file completed successfully"
    echo "$file PASSED at $(date)" >> "$PASS_LOG"
  fi

  echo "-----------------------------------------------------"
done

echo "All playbooks processed."
echo "Passed test results saved to $PASS_LOG"
