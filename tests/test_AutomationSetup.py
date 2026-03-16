from AutomationSetup import getImagePath, isValidHealthManaStr, getTileLocation, locateImage, BASE_CONFIDENCE, ENCHANTED_CONFIDENCE, SHADOW_CONFIDENCE

def test_getImagePath_valid():
    assert getImagePath('Frenzy') == '.\\SpellImages\\Frenzy.png'
    assert getImagePath('PotionMotionButton') == '.\\SpellImages\\PotionMotionButton.png'
    assert getImagePath('StormLord') == '.\\SpellImages\\StormLord.png'

def test_getImagePath_invalid():
    assert getImagePath('EnchantedShadeOfMusicology') != '.\\SpellImages\\EnchantedSoundOfMusicology.png'
    assert getImagePath('Epic') != '.\\SpellImages\\Epic.jpg'
    assert getImagePath('Indemnity') != '\\SpellImages\\Indemnity.png'

def test_isValidHealthManaStr_valid():
    assert isValidHealthManaStr('100/100') == True
    assert isValidHealthManaStr('6947/10401') == True

def test_isValidHealthManaStr_invalid():
    assert isValidHealthManaStr('100./100') == False
    assert isValidHealthManaStr('100,100') == False
    assert isValidHealthManaStr('100\\100') == False
    assert isValidHealthManaStr('l00/l00') == False

def test_getTileLocation():

    initialX = 650
    initialY = 285
    tileWidth = 88.571
    tileHeight = 88.333

    for tileX in range(1, 7+1):
        for tileY in range(1, 6+1):
            x = initialX + tileWidth * tileX - (tileWidth / 2)
            y = initialY + tileHeight * tileY - (tileHeight / 2)

            assert getTileLocation(tileX, tileY) == (x, y)

def test_locateImage_confidence(mocker):
    
    # mock locateOnScreen info
    mockLocate = mocker.patch('AutomationSetup.pyautogui.locateOnScreen')
    mockLocate.return_value = mocker.MagicMock()

    # test base confidence
    locateImage('StormLord')
    assert mockLocate.call_args.kwargs['confidence'] == BASE_CONFIDENCE

    # test enchanted confidence
    locateImage('EnchantedStormLord')
    assert mockLocate.call_args.kwargs['confidence'] == ENCHANTED_CONFIDENCE

    # test shadow confidence
    locateImage('ShadeOfMusicology')
    assert mockLocate.call_args.kwargs['confidence'] == SHADOW_CONFIDENCE

def test_locateImage_notFound(mocker):
    
    # mock locateOnScreen info
    mockLocate = mocker.patch('AutomationSetup.pyautogui.locateOnScreen')
    mockLocate.return_value = None

    result, exists = locateImage('ImageThatDoesNotExist')

    assert exists == False