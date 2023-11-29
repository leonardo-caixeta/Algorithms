from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("ola mundo", 3) == "alo_odnum "

    assert encrypt_message("ola mundo", 4) == "odnum_ alo"

    assert encrypt_message("ola mundo", 9) == "odnum alo"

    with pytest.raises(
        TypeError, match="tipo inválido para message"
    ):
        encrypt_message(10, 1)
