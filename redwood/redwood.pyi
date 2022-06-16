# type stub for redwood module
# see https://pyo3.rs/v0.16.4/python_typing_hints.html
from pathlib import Path
from typing import List

def generate_source_key_pair(passphrase: str, email: str) -> (str, str, str):
    pass

def encrypt_message(recipients: List[str], plaintext: str, destination: Path) -> None:
    pass

def encrypt_file(recipients: List[str], plaintext: Path, destination: Path) -> None:
    pass

def decrypt(ciphertext: bytes, secret_key: str, passphrase: str) -> str:
    pass
