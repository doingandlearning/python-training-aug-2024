class TVLicenceError(Exception):
  def __init__(self, message, code="ERR"):
    super().__init__(message) # Give me everything the parent has! (Exception)
    self.code = code


try:
  raise TVLicenceError("Needs to have a licence.", "ERR_BBC_LICENCE")
except TVLicenceError as e:
  print(e.code)
  print("I'll deal with later!")