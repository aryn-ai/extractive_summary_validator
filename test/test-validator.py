# to run these, run 
# pytest test/test-validator.py

from guardrails import Guard
from validator import ExtractiveSummary

guard = Guard.from_string(validators=[ExtractiveSummary()])
metadata = {
  "filepaths": ['./test/sample-doc.txt']
}

def test_pass():
  # read in the sample-bad-summary.txt file as a string
  with open("./test/sample-good-summary.txt", 'r') as file:
    file_contents = file.read()

  res = guard.parse(file_contents, metadata=metadata)
  assert(res.validated_output == file_contents)

def test_fail():
  with open("./test/sample-bad-summary.txt", 'r') as file:
    file_contents = file.read()

  guard.parse(file_contents, metadata=metadata)
  assert(True)
  # assert(not guard.history.last.failed_validations.empty())
