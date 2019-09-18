import spaceman


def test_is_guess_in_word():
    assert spaceman.is_guess_in_word('a', 'word') == False
    assert spaceman.is_guess_in_word('o', 'word') == True
    assert spaceman.is_guess_in_word('w', 'word') == True

def test_is_word_guessed():
    assert spaceman.is_word_guessed('apple', 'apl') == False
    assert spaceman.is_word_guessed('banana', 'ban') == True
    assert spaceman.is_word_guessed('cat', 'c') == False

def test_create_index_list():
    assert spaceman.create_index_list('banana', 'a') == [1, 3, 5]
    assert spaceman.create_index_list('apparatus', 'p') == [1, 2]
    assert spaceman.create_index_list('umbrella', 'b') == [2]

def test_get_guessed_word():
    assert spaceman.get_guessed_word('apple', 'p') == '_pp__'
    assert spaceman.get_guessed_word('umbrella', 'um') == 'um______'
    assert spaceman.get_guessed_word('harry', 'hr') == 'h_rr_'
