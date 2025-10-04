# Future Enhancement Ideas for Villancicos Website

## Bouncing Ball / Karaoke-Style Sing-Along Videos

### Current State of Technology:

**Manual Tools (Most Common):**
- Video editing software (Adobe Premiere, Final Cut Pro, DaVinci Resolve) with text animation
- Karaoke-specific software like KaraFun Studio, Karaoke Builder Studio
- You manually time when each word/syllable should highlight by listening and placing markers

**Semi-Automated:**
- **Audio-to-text alignment tools** can analyze audio and sync it to existing lyrics
- Software like Aegisub (subtitle editor) with timing helpers
- Some AI tools can detect vocal onsets and suggest timing

**Emerging AI Approaches:**
- **Forced alignment** algorithms (like Montreal Forced Aligner) can match phonemes in audio to text
- **Music Information Retrieval (MIR)** tools can detect vocals, beats, and structure
- Some experimental systems combine speech recognition with music source separation

### Implementation Approach for This Site:

For the Spanish Christmas carols, would likely want:
1. **Manual timing** in a tool like Aegisub or a simple video editor - most reliable
2. **Export as web format** - HTML5 video with timed text tracks (WebVTT), or JavaScript-based timing
3. **Integration** - Could add to existing HTML page with synchronized highlighting

**Note:** The technology exists but typically requires manual fine-tuning for music (unlike speech, which auto-aligns better). Most professional karaoke is still hand-timed because music phrasing is more complex than speech.

## English Translations

Add parallel English translations to display alongside Spanish lyrics while singing:
- Could show side-by-side or toggle between Spanish/English
- Helps non-Spanish speakers understand meaning while learning songs
- Useful for bilingual groups
