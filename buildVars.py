# -*- coding: UTF-8 -*-
from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
    addon_name="VisionAssistant",
    # Add-on summary/title, usually the user visible name of the add-on
    # Translators: Summary/title for this add-on
    # to be shown on installation and add-on information found in add-on store
    addon_summary=_("Vision Assistant Pro"),
# Add-on description
    # Translators: Long description to be shown for this add-on on add-on information from add-on store
    addon_description=_("""An advanced AI assistant for NVDA using Gemini models.
Command Layer: Press NVDA+Shift+V, then:
- Smart Translator (T) / Clipboard (Shift+T)
- Text Refiner (R)
- Describe Object (V) / Full Screen (O)
- Online Video Analysis (Shift+V)
- Document Reader (D)
- File OCR (F)
- CAPTCHA Solver (C)
- Audio Transcription (A)
- Smart Dictation (S)
- Announce Status (I)
- Label Object (L)
- Manage/Scan Labels (Shift+L)
- UI Explorer (E)
- AI Operator (Shift+A)
- Check Update (U)
- Recall Last Result (Space)
- Commands Help (H)"""),
    addon_version="6.5.1",
    # Brief changelog for this version
    # Translators: what's new content for the add-on version to be shown in the add-on store
    addon_changelog=_("""## Changes for 6.5.0

*   **Live Assistant**: Added a real-time voice and screen assistant feature, available exclusively for the Google Gemini provider (or Gemini-compatible custom providers). Includes interactive voice and thinking depth customization directly inside the dialog, with automatic reconnection upon changing settings.
*   **MiniMax AI Provider**: Integrated MiniMax as a peer provider with full multimodal support (chat, vision, OCR), custom TTS using over 300+ dynamic voices, and automatic stripping of reasoning blocks (e.g., `<think>...</think>`) from outputs.
*   **Document Viewer Translation**: Corrected a silent translation failure for non-English NVDA users by ensuring the standard 2-letter language code is sent to Google Translate instead of the localized language name.
*   **PDF Batch Scan Retry**: Implemented a highly optimized, separate, and silent retry logic for PDF document batch scanning to prevent redundant uploads and avoid disruptive error popups during retries.
*   **Document Viewer Status**: Fixed a bug where the plugin's overall status (checked via `I`) remained stuck on "Batch Processing Started" during long document scans.
*   **Resolved Threading Crash**: Fixed a severe `IsMain() failed in wxTimerImpl` thread assertion crash when opening documents from a background thread by transitioning the GUI callback queue to `wx.CallAfter`."""),
    addon_author="Mahmood Hozhabri",
    addon_url="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_sourceURL="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_docFileName="readme.html",
    addon_minimumNVDAVersion="2025.1",
    addon_lastTestedNVDAVersion="2026.1",
    addon_updateChannel=None,
    addon_license="GPL-2.0",
    addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

pythonSources: list[str] = ["addon/globalPlugins/visionAssistant/*.py"]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = [
    "markdown.extensions.tables",
    "markdown.extensions.toc",
    "markdown.extensions.nl2br",
    "markdown.extensions.extra",
]

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}