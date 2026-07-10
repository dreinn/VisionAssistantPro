## Changes for 6.5.0

*   **Live Assistant**: Added a real-time voice and screen assistant feature, available exclusively for the Google Gemini provider (or Gemini-compatible custom providers). Includes interactive voice and thinking depth customization directly inside the dialog, with automatic reconnection upon changing settings.
*   **MiniMax AI Provider**: Integrated MiniMax as a peer provider with full multimodal support (chat, vision, OCR), custom TTS using over 300+ dynamic voices, and automatic stripping of reasoning blocks (e.g., `<think>...</think>`) from outputs.
*   **Document Viewer Translation**: Corrected a silent translation failure for non-English NVDA users by ensuring the standard 2-letter language code is sent to Google Translate instead of the localized language name.
*   **PDF Batch Scan Retry**: Implemented a highly optimized, separate, and silent retry logic for PDF document batch scanning to prevent redundant uploads and avoid disruptive error popups during retries.
*   **Document Viewer Status**: Fixed a bug where the plugin's overall status (checked via `I`) remained stuck on "Batch Processing Started" during long document scans.
*   **Resolved Threading Crash**: Fixed a severe `IsMain() failed in wxTimerImpl` thread assertion crash when opening documents from a background thread by transitioning the GUI callback queue to `wx.CallAfter`.
---

### 🌟 Support the Future of Vision Assistant Pro

Vision Assistant Pro is a mission to bridge the gap between AI and true accessibility. Maintaining and testing a cloud-based AI tool under internet restrictions is a constant battle. 

Each major testing cycle of our new visual features consumes active API credits (often costing $10+ per test run out of my own pocket), in addition to high local infrastructure costs.

As an open-source project, Vision Assistant Pro thrives on community support. If you'd like to help cover these ongoing development and testing costs, please consider supporting the project:

* 🍎 **Apple US Gift Cards:** Please send the gift card code to: `visionassistantpro@proton.me` (You can purchase them globally here: [Buy Apple US Gift Cards](https://www.mygiftcardsupply.com/shop/itunes-gift-cards/))
* 💎 **Cryptocurrency (TON):** `UQDoOOOoDYPP8eqWXVsjVyYzulY72JLZK1grPS_O2DbgVNsc`

Thank you for being part of this journey!