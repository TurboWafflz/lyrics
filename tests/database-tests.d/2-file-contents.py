CODE_OK   = 0
CODE_WARN = 1
CODE_ERR  = 2

def testForNewlineAtEndOfFile(path, bytes, plaintext, lyrics, metadata, database):
  return CODE_OK if plaintext.endswith('\n') else CODE_ERR

def testForNoCarriageReturns(path, bytes, plaintext, lyrics, metadata, database):
  return CODE_ERR if '\r' in plaintext else CODE_OK

def testForNoEmptyFiles(path, bytes, plaintext, lyrics, metadata, database):
  return CODE_ERR if len(plaintext) == 0 else CODE_OK

def testForNoUnusualCharacters(path, bytes, plaintext, lyrics, metadata, database):
  unusualChars = ['`', '©']
  return next((CODE_ERR for char in unusualChars if char in plaintext), CODE_OK)

def testForTests(*_):
  def testTheTestForNewlineAtEndOfFile():
    passing = testForNewlineAtEndOfFile('', b'', 'La la la\n', '', {}, {}) == CODE_OK
    failing = testForNewlineAtEndOfFile('', b'', 'La la', '', {}, {}) == CODE_ERR
    return passing and failing
  def testTheTestForNoCarriageReturns():
    passing = testForNoCarriageReturns('', b'', 'La la la\n', '', {}, {}) == CODE_OK
    failing = testForNoCarriageReturns('', b'', 'La la\r\nLa\r\nLa\r\n\r\n', '', {}, {}) == CODE_ERR
    return passing and failing
  def testTheTestForNoEmptyFiles():
    passing = testForNoEmptyFiles('', b'', 'La la la\n', '', {}, {}) == CODE_OK
    failing = testForNoEmptyFiles('', b'', '', '', {}, {}) == CODE_ERR
    return passing and failing
  def testTheTestForNoUnusualCharacters():
    passing = testForNoUnusualCharacters('', b'', 'La la la\n', '', {}, {}) == CODE_OK
    failing = testForNoUnusualCharacters('', b'', '`La la`\n© Some Publishing Company, LLC', '', {}, {}) == CODE_ERR
    return passing and failing
  if not testTheTestForNewlineAtEndOfFile() \
  or not testTheTestForNoCarriageReturns() \
  or not testTheTestForNoEmptyFiles() \
  or not testTheTestForNoUnusualCharacters():
    return CODE_ERR
  return CODE_OK
