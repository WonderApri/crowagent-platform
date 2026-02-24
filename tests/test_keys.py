import pytest
from app import main


def test_encrypt_decrypt_roundtrip(monkeypatch):
    # basic round‑trip property regardless of whether a Fernet key is
    # configured.  When no encryption key is supplied the helpers behave
    # as identity functions, which is acceptable for the prototype.
    assert main._decrypt(main._encrypt("hello")) == "hello"

    # simulate a real Fernet key and ensure ciphertext is different from
    # plaintext but still decodes correctly
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        pytest.skip("cryptography not installed; skipping key encryption test")

    fake_key = Fernet.generate_key()
    monkeypatch.setattr(main, "_FERNET", Fernet(fake_key))
    plaintext = "supersecret"
    cipher = main._encrypt(plaintext)
    assert cipher != plaintext
    assert main._decrypt(cipher) == plaintext
