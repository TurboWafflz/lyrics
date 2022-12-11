CODE_OK   = 0
CODE_WARN = 1
CODE_ERR  = 2

def testForSongFilePathToAlwaysHaveFourParts(path, bytes, plaintext, lyrics, metadata, database):
  parts = path.split('/')
  return CODE_ERR if len(parts) != 4 else CODE_OK

def testForNoExtensionsInSongFileNames(path, bytes, plaintext, lyrics, metadata, database):
  parts = path.split('/')
  if len(parts) == 4:
    songFileName = parts[3]
    if songFileName.lower().endswith('.txt'):
      return CODE_WARN # Not an error because song names may produce false positives
  return CODE_OK

def testForNoSpacesWithinFileDirNames(path, bytes, plaintext, lyrics, metadata, database):
  return next(
      (CODE_ERR for part in path.split('/')
       if part.startswith(' ') or part.endswith(' ')),
      CODE_OK,
  )

def testForProperFirstSymbolInArtistDirectoryName(path, bytes, plaintext, lyrics, metadata, database):
  parts = path.split('/')
  return CODE_OK if parts[1].startswith(parts[0]) else CODE_ERR

def testForTests(*_):
  def testTheTestForSongFilePathToAlwaysHaveFourParts():
    passing = testForSongFilePathToAlwaysHaveFourParts('A/Artist/Album/Recording', b'', '', '', {}, {}) == CODE_OK
    failing = testForSongFilePathToAlwaysHaveFourParts('A/Artist/Recording', b'', '', '', {}, {}) == CODE_ERR
    return passing and failing
  def testTheTestForNoExtensionsInSongFileNames():
    passing = testForNoExtensionsInSongFileNames('A/Artist/Album/Recording', b'', '', '', {}, {}) == CODE_OK
    warning = testForNoExtensionsInSongFileNames('A/Artist/Album/Recording.txt', b'', '', '', {}, {}) == CODE_WARN
    return passing and warning
  def testTheTestForNoSpacesWithinFileDirNames():
    passing = testForNoSpacesWithinFileDirNames('A/Artist/Album/Recording', b'', '', '', {}, {}) == CODE_OK
    failing = testForNoSpacesWithinFileDirNames(' A / Artist / Album / Recording.txt ', b'', '', '', {}, {}) == CODE_ERR
    return passing and failing
  def testTheTestForProperFirstSymbolInArtistDirectoryName():
    passing = testForProperFirstSymbolInArtistDirectoryName('A/Artist/Album/Recording', b'', '', '', {}, {}) == CODE_OK
    failing = testForProperFirstSymbolInArtistDirectoryName('A/Brtist/Album/Recording', b'', '', '', {}, {}) == CODE_ERR
    return passing and failing
  if not testTheTestForSongFilePathToAlwaysHaveFourParts() \
  or not testTheTestForNoExtensionsInSongFileNames() \
  or not testTheTestForNoSpacesWithinFileDirNames() \
  or not testTheTestForProperFirstSymbolInArtistDirectoryName():
    return CODE_ERR
  return CODE_OK
