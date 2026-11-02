"""Set up one SeedKeeper card for the quiz, the same way Sato-Tools does.

Run by setup-quiz-card.sh after SeedKeeper is installed on the card. Sets
the PIN, saves question 2 as a password labelled "Question", then
reconnects and reads both back the way the phone app would.

    python quiz-card.py PIN QUESTION [--check-only]
"""
import sys
import time
from os import urandom

from pysatochip.CardConnector import CardConnector

LABEL = "Question"
TYPE_PASSWORD = 0x90


def connect():
    cc = CardConnector(None, None, "seedkeeper")
    time.sleep(1)
    status = cc.card_get_status()[3]
    if cc.needs_secure_channel:
        cc.card_initiate_secure_channel()
    return cc, status


def setup(pin, question):
    cc, status = connect()
    if status["setup_done"]:
        sys.exit("STOP: card already set up, nothing changed")
    # Same values as Sato-Tools' card_setup_native_pin()
    _, sw1, sw2 = cc.card_setup(0x05, 0x01, list(pin.encode()), list(urandom(16)),
                                0x01, 0x01, list(urandom(16)), list(urandom(16)),
                                32, 0x0000, 0x01, 0x01, 0x01)
    if (sw1, sw2) != (0x90, 0x00):
        sys.exit(f"STOP: setup failed {sw1:02X}{sw2:02X}")
    cc.card_verify_PIN(pin)
    # Same encoding as Sato-Tools' import_password(), with no login or url
    secret = bytes([len(question.encode())]) + question.encode()
    cc.seedkeeper_import_secret({
        "header": cc.make_header(TYPE_PASSWORD, 0x01, LABEL),
        "secret_list": list(secret),
    })
    cc.card_disconnect()


def check(pin, question):
    cc, status = connect()
    if not status["setup_done"]:
        sys.exit("FAIL: card not set up")
    cc.card_verify_PIN(pin)
    headers = cc.seedkeeper_list_secret_headers()
    if len(headers) != 1 or headers[0]["label"] != LABEL:
        sys.exit(f"FAIL: expected one secret labelled {LABEL}, got {headers}")
    raw = bytes.fromhex(cc.seedkeeper_export_secret(headers[0]["id"])["secret"])
    text = raw[1:1 + raw[0]].decode()
    if text != question:
        sys.exit(f"FAIL: password reads {text!r}")
    tries = cc.card_get_status()[3]["PIN0_remaining_tries"]
    cc.card_disconnect()
    print(f"OK: PIN {pin} works, {LABEL} = {text!r}, {tries} PIN tries left")


if __name__ == "__main__":
    pin, question = sys.argv[1], sys.argv[2]
    if sys.argv[3:] != ["--check-only"]:
        setup(pin, question)
    check(pin, question)
