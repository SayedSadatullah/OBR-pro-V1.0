# ═══════════════════════════════════════════════════════════
#  ORB PRO DASHBOARD — CONFIG  v6
# ═══════════════════════════════════════════════════════════

# ── Binance API (real account — read-only for balances) ────
BINANCE_API_KEY    = ""
BINANCE_API_SECRET = ""

# ── Binance Testnet (for placing practice orders) ──────────
TESTNET_API_KEY    = ""
TESTNET_API_SECRET = ""

# ── Telegram alerts ────────────────────────────────────────
TELEGRAM_TOKEN   = ""
TELEGRAM_CHAT_ID = ""

# ── Account ────────────────────────────────────────────────
ACCOUNT_SIZE = 1000.0

# ── Default chart ──────────────────────────────────────────
DEFAULT_SYMBOL    = "BTCUSDT"
DEFAULT_TIMEFRAME = "1m"
TIMEFRAMES        = ["1m", "3m", "5m", "15m", "30m", "1h", "4h", "1d"]

# ── ORB strategy ───────────────────────────────────────────
ORB_MINUTES        = 30
LONDON_RANGE_START = 8       # hour UTC
LONDON_TRADE_END   = 12
NY_RANGE_START     = 13
NY_TRADE_END       = 17
USE_VOL_FILTER     = True
VOL_MULTIPLIER     = 1.5
USE_ADX_FILTER     = True
ADX_THRESH         = 20
MIN_RANGE_ATR      = 0.5
MAX_RANGE_ATR      = 4.0
RR                 = 2.0
USE_BREAKEVEN      = True
USE_PARTIAL_TP     = True
SL_BUFFER          = 0.2
RISK_PCT           = 1.0
MAX_DAILY_DD       = 3.0
MAX_WEEKLY_DD      = 6.0

# ── Indicators ─────────────────────────────────────────────
# Moving averages: add/remove any period dynamically via the MA Manager in the chart
# Each entry: {"type": "EMA"|"SMA", "period": N, "color": hex, "enabled": True}
MA_LIST = []   # populated at runtime by MA Manager panel

# Fixed oscillator/overlay indicators (toggle via toolbar)
INDICATORS = {
    # ── Oscillators ────────────────────────────────────────────────────────
    "RSI":          {"type":"RSI",       "enabled":False, "period":14, "color":"#e67e22", "ob":70, "os":30},
    "MACD":         {"type":"MACD",      "enabled":False, "fast":12, "slow":26, "signal":9, "color":"#00d9ff"},
    "STOCH":        {"type":"STOCH",     "enabled":False, "k":14, "d":3, "color":"#ff6b6b"},
    "CCI":          {"type":"CCI",       "enabled":False, "period":20, "color":"#f1c40f"},
    "WILLIAMS_R":   {"type":"WILLIAMS_R","enabled":False, "period":14, "color":"#9b59b6"},
    # ── Trend ──────────────────────────────────────────────────────────────
    "ATR":          {"type":"ATR",       "enabled":False, "period":14, "color":"#aaaaaa"},
    "ADX":          {"type":"ADX",       "enabled":False, "period":14, "color":"#f39c12"},
    "SUPERTREND":   {"type":"SUPERTREND","enabled":False, "period":10, "mult":3.0,
                     "color_up":"#26a69a", "color_dn":"#ef5350"},
    "SAR":          {"type":"SAR",       "enabled":False, "step":0.02, "max":0.20, "color":"#e74c3c"},
    # ── Bands / Overlays ───────────────────────────────────────────────────
    "BB":           {"type":"BB",        "enabled":False, "period":20, "std":2.0, "color":"#888888"},
    "VWAP":         {"type":"VWAP",      "enabled":False, "color":"#e040fb"},
    # ── Volume ─────────────────────────────────────────────────────────────
    "OBV":          {"type":"OBV",       "enabled":False, "color":"#3498db"},
}

# ── Watchlist ──────────────────────────────────────────────
WATCHLIST = [
    "BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT",
    "XRPUSDT", "ADAUSDT", "DOGEUSDT", "AVAXUSDT",
    "ALGOUSDT", "SUIUSDT", "APTUSDT", "TRBUSDT",
    "UNIUSDT", "STXUSDT",
    # Market structure symbols (loaded as tickers if available)
    "TOTAL", "TOTAL2", "TOTAL3", "ETHBTC",
    "USDT.D", "BTC.D",
]

# ── Theme ──────────────────────────────────────────────────
# Light theme (change these to go dark: BG_COLOR="#131722" etc.)
BG_COLOR     = "#FFFFFF"
BG_SECONDARY = "#F0F2F5"
BG_TERTIARY  = "#E4E7EC"
BULL_COLOR   = "#26a69a"
BEAR_COLOR   = "#ef5350"
TEXT_COLOR   = "#1A1A2E"
TEXT_DIM     = "#6B7A99"
GRID_COLOR   = "#D8DCE8"
ACCENT_COLOR = "#0066CC"
BORDER_COLOR = "#C8CDD8"
FONT_SIZE    = 15

# ── Storage ────────────────────────────────────────────────
DB_PATH  = "orb_data.db"

# ── WebSocket / REST ───────────────────────────────────────
WS_BASE   = "wss://fstream.binance.com/ws"
REST_BASE = "https://fapi.binance.com"


def to_orb_dict():
    return {
        "orb_minutes":        ORB_MINUTES,
        "london_range_start": LONDON_RANGE_START,
        "london_trade_end":   LONDON_TRADE_END,
        "ny_range_start":     NY_RANGE_START,
        "ny_trade_end":       NY_TRADE_END,
        "use_vol_filter":     USE_VOL_FILTER,
        "vol_multiplier":     VOL_MULTIPLIER,
        "use_adx_filter":     USE_ADX_FILTER,
        "adx_thresh":         ADX_THRESH,
        "min_range_atr":      MIN_RANGE_ATR,
        "max_range_atr":      MAX_RANGE_ATR,
        "rr":                 RR,
        "use_breakeven":      USE_BREAKEVEN,
        "use_partial_tp":     USE_PARTIAL_TP,
        "sl_buffer":          SL_BUFFER,
        "risk_pct":           RISK_PCT,
        "max_daily_dd":       MAX_DAILY_DD,
        "max_weekly_dd":      MAX_WEEKLY_DD,
    }

# ── Branding (hardcoded — do not remove) ───────────────────
APP_AUTHOR     = "Your Name"          # ← change to your name
APP_VERSION    = "1.0.0"
APP_TITLE      = "ORB Pro"
APP_SUBTITLE   = "Professional Trading Dashboard"
APP_COPYRIGHT  = "© 2026 Your Name. All rights reserved."
AUTHOR_ICON    = "orb.ico"            # ← your icon file name

SHOW_SESSION_BG  = False  # keep False — backgrounds removed
SHOW_RANGE_BOXES = False  # keep False — range boxes removed

CURRENT_THEME = "Gray (Default)"

# ── Date/Time axis format ───────────────────────────────────
# Tokens: %d=day %b=month-abbr %m=month-num %Y=year %H=hour %M=min
DATE_FORMAT = "%d %b"    # e.g. "12 Mar"
TIME_FORMAT = "%H:%M"    # e.g. "14:30"

