# YazSes — free offline voice dictation & speech to text for Linux, macOS, Windows

> YazSes is free, open-source dictation software that lets you use your voice to dictate into any app. Speech to text runs entirely on your own machine with faster-whisper — no cloud, no account, no subscription. Linux (X11 & Wayland), macOS and Windows.

Source: <https://mskazemi.com/projects/yazses/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

shipping · open source · Apache-2.0

Offline voice dictation for Linux, macOS and Windows.

Free, open-source **dictation software** that lets you use your voice to dictate anywhere on your computer. Hold a key, speak, release — the **speech-to-text** runs on your own CPU and the words are typed straight into whatever app has focus. **No cloud. No account. No API key. No subscription.**

- PLATFORMS Linux (X11 & Wayland) · macOS · Windows

- ENGINE faster-whisper · CPU int8 · on-device

- LICENCE Apache-2.0 · free forever

// why it exists

## Dictation you don't have to send to somebody else's computer.

Most good voice-to-text tools are a subscription and a network round-trip: your microphone audio is uploaded, transcribed on a rented GPU, and billed per month or per minute. That is a bad trade if your words are clinical notes, legal drafts, journalism, unpublished research, or anything under an NDA — and it simply does not work on a machine with no reliable connection.

YazSes takes the opposite position. Transcription happens on the CPU you already own, with nothing uploaded and nothing to sign up for. On Linux that also fills a genuine gap: there is no built-in dictation comparable to Windows Voice Access or macOS Dictation, and almost nothing that works properly under **Wayland**.

// what it does

## Hold. Speak. Release. The text is just there.

### Types into any application

There is no dictation box to copy out of. Release the key and the text is injected into the focused window — editor, browser, terminal or chat — on X11, Wayland, macOS and Windows.

### Fully offline speech to text

faster-whisper runs locally in int8 on the CPU. No GPU, no network, no account, no API key. Nothing leaves the machine by default.

### Voice commands, not just dictation

The same key that types your words also runs commands. A fast on-device regex grammar routes _"undo that"_ or _"go to line 42"_ to real key sequences instead of typing them.

### Transcribe recordings and meetings

Turn an existing audio or video file into text with optional speaker labels, or capture a whole meeting hands-free and get a speaker-attributed transcript — offline, with no per-minute fee.

### Built for accessibility

Calibrates to your voice rather than expecting broadcast-clear speech, with a dysfluency-friendly mode, mic-level tuning, and non-keyboard activation for hands-free use.

### Learns from your corrections

An opt-in, encrypted, on-device corpus lets the tuner propose accuracy fixes from your own edits. It is off by default and never leaves the machine.

// getting started

## One command, then hold a key and talk.

YazSes installs from PyPI on any operating system with Python 3.11 or newer, and ships native packages for Debian/Ubuntu (APT), Snap, macOS and Windows.

`pipx install yazses`

The [documentation](https://mskazemi.com/yazses/) covers installation per platform, choosing a hotkey, tuning the microphone, voice commands, transcribing recordings, meeting capture, and the privacy model in full.

// write-up

## Described in an open preprint.

The design and privacy model are written up as _"YazSes: An Offline, Privacy-First, Cross-Platform Hold-to-Talk Voice-Dictation System"_, available as an open-access preprint on [arXiv:2607.28878](https://arxiv.org/abs/2607.28878).

// more

## Explore the rest of the lab.
