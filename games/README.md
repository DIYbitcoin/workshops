# 🎮 Workshop games

An activity during the workshop where attendees play a proof of work
game to win a device or a javacard. Keep the prizes separate from the
devices used to play.

- 🗝️ **SeedKeeper quiz:** the easiest, and enough on its own. One winner
  per group.
- 💻 **Optional group rounds:** a team race first picks the winning
  group(s), then they play the SeedKeeper quiz to pick who in each group
  wins the device.

## 🗝️ Main activity: SeedKeeper quiz

One SeedKeeper card per player, played on their own phones, one winner
per group. There are two questions:

- ❓ **Question 1** goes in the group chat. Its answer is the card's PIN.
- 🔐 **Question 2** is hidden on the card as a password. Players only see
  it after unlocking the card, and the first to answer it wins.

### 🧰 What you need to have

- 💳 One **J3H145** card per player
- 💻 Your own laptop and a **smartcard reader**, with the tools from
  [Step 1 of the javacard guide](https://github.com/DIYbitcoin/guides/tree/main/javacards) and **Sato-Tools**
- 📱 Players' own phones with **NFC**
- 💬 A **group chat** everyone is in, to post question 1

### 🛠️ Before the event, on each card

⚠️ **Flashing only puts a blank applet on the card.** `gp --install`
leaves no PIN and no secret, so every card also needs steps 2 and 3, one
by one.

1. Flash SeedKeeper ([javacard guide, Step 4](https://github.com/DIYbitcoin/guides/tree/main/javacards)).
2. In Sato-Tools, press **Setup my card** and set the PIN to the answer
   of question 1, for example `2008`.
3. Press **Import secret**, then **Password**. Type `Question` as the
   **Label** and question 2 as the **Password**, for example
   `Bitcoin's max supply?`, then press **Import to card**.
4. ✅ Open **every** card in the SeedKeeper phone app. Check it asks for
   your PIN (not to set up a new one) and shows question 2.

Bring your laptop and reader to the event too, so you can wipe a card a
player locks with wrong PINs and flash it again.

### 🙋 At the event, players

1. Install the SeedKeeper app: from the App Store on iPhone, or on
   Android from the
   [SeedKeeper Android release](https://github.com/Toporin/Seedkeeper-Android/releases/latest).
2. Answer question 1 from the group chat, for example "What year was the
   bitcoin white paper published?". The answer is the card's PIN.
3. In the app, press **Click and scan**, hold the card on the back of the
   phone and type the PIN.
4. Open the saved secret to read question 2.
5. The first person in each group to tell you its answer (21 million)
   wins.

⚠️ Too many wrong PINs lock the card. A locked card isn't bricked: wipe
it with `gp --uninstall SeedKeeper-v0.2-0.1.cap` and flash it again.

## 💻 Optional group rounds

Each group works together as one team, so nobody waits for a turn or
learns by watching. The first group(s) to finish win the round, and their
members then play the SeedKeeper quiz to pick who in each group gets the
device.

### 💳 Round A: flash Satochip and set it up in Sparrow

**What you need to have, per group:**

- 💻 A laptop (Mac or Linux) set up with
  [Step 1 of the javacard guide](https://github.com/DIYbitcoin/guides/tree/main/javacards), with **Sparrow Wallet**
  installed and `SatoChip-v0.15-0.1.cap` downloaded
- 🔌 A **smartcard reader**
- 💳 A blank **J3H145** card

**The race:** the first group to flash Satochip and show you the finished
wallet in Sparrow wins
([javacard guide, Steps 4 and 5a](https://github.com/DIYbitcoin/guides/tree/main/javacards)).

**Then, on the same card:** remove Satochip and flash SeedKeeper:

```bash
gp --uninstall SatoChip-v0.15-0.1.cap
```

```bash
gp --install SeedKeeper-v0.2-0.1.cap
```

Set it up for the quiz in Sato-Tools (Main activity: SeedKeeper quiz,
before the event, steps 2 to 4), and the winning group(s) play the quiz to
pick who in each group gets the device.

### 🔋 Round B: passphrase riddle on a signer

**What you need to have, per group:**

- 📟 Any **signer** that can load 12 seed words, take a passphrase and
  show the fingerprint, like SeedSigner, Kern or Krux. KISS Signer's setup
  asks for a passphrase of 12 or more characters mixing capitals, numbers
  and symbols, so on KISS make the riddle's answer one, like
  `Satoshi@2009`.
- 🔋 A **powerbank** that stays on with the signer plugged in: check by
  leaving one running for 15 minutes before the event
- 🌱 A different set of 12 practice seed words, loaded on the signer
  before the event

**Before the event, on each signer:** load the 12 seed words, type the
riddle's answer as the passphrase, write down the fingerprint it shows,
then go back so the signer waits on the passphrase screen.

**The race:** post the riddle in the group chat. The first group to type
the right answer as the passphrase and read you their fingerprint wins.
