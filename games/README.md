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
- 💻 Before the event only: your laptop and a **smartcard reader**, with the tools from
  [Step 1 of the javacard guide](https://github.com/DIYbitcoin/guides/tree/main/javacards)
- 📱 Players' own phones with **NFC**
- 💬 A **group chat** everyone is in, to post question 1

### 🛠️ Before the event, on each card

⚠️ **Flashing only puts a blank applet on the card.** `gp --install`
leaves no PIN and no secret, so use the script below, which also sets
both.

1. Download `SeedKeeper-v0.2-0.1.cap`
   ([javacard guide, Step 4](https://github.com/DIYbitcoin/guides/tree/main/javacards))
   and open the Terminal in that folder.
2. Run [setup-quiz-card.sh](setup-quiz-card.sh) and type your PIN and
   question 2 when it asks. Keep them off GitHub and anywhere players
   can see before the event.

   ```bash
   bash /path/to/setup-quiz-card.sh
   ```

3. Put a card in the reader and press **Enter**. It wipes the card,
   flashes SeedKeeper, sets the PIN, saves question 2 with the label
   `Question`, then reads both back.

   ✅ It prints `OK` for a good card. Swap cards and press **Enter**
   again, or type `q` when you're done.
4. ✅ Open the first card in the SeedKeeper phone app. Check it asks for
   your PIN (not to set up a new one) and shows question 2.

### 🙋 At the event, players

1. Install the SeedKeeper app: from the App Store on iPhone, or on
   Android from the
   [SeedKeeper Android release](https://github.com/Toporin/Seedkeeper-Android/releases/latest).
2. Answer question 1 from the group chat. The answer is the card's PIN.
3. In the app, press **Click and scan**, hold the card on the back of the
   phone and type the PIN.
4. Open the saved secret to read question 2.
5. The first person in each group to tell you its answer wins.

⚠️ Too many wrong PINs lock the card. A locked card isn't bricked: run
the script on it again.

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

The winning group(s) then play the SeedKeeper quiz with the cards you set
up before the event, to pick who in each group gets the device.

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
