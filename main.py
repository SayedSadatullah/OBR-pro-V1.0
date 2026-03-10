"""
ORB Pro Trading Dashboard — Entry Point (Lightweight Charts Integration)
"""
import sys
import os

# 1. Setup Paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtWidgets, QtCore, QtGui
import config
from ui.theme_manager import apply_theme
from core.indicator_engine import compute_all
from core.binance_rest import fetch_ohlcv_paginated

# 2. Import the new Chart Panel bridge
from ui.chart_panel import ChartPanel 

class MainWindow(QtWidgets.QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ORB Pro v38 - TradingView Engine")
        self._dfs = {}
        self._active_symbol = config.DEFAULT_SYMBOL
        self._active_tf = config.DEFAULT_TIMEFRAME

        # Initialize the New Chart Engine
        self.chart = ChartPanel()
        self.setCentralWidget(self.chart)
        
        # Load initial data
        QtCore.QTimer.singleShot(100, lambda: self._load_symbol_data(self._active_symbol, self._active_tf))

    def _load_symbol_data(self, symbol, tf):
        """Called when a symbol is selected."""
        self._active_symbol = symbol
        self._active_tf = tf
        
        # 1. Fetch data
        df = fetch_ohlcv_paginated(symbol, tf, total=1000)
        if df.empty: 
            print(f"No data found for {symbol}")
            return
        
        self._dfs[(symbol, tf)] = df
        
        # 2. Update the Lightweight Chart
        self.chart.set_candles(df)
        
        # 3. Calculate and push indicators
        inds = compute_all(df, config.INDICATORS, config.MA_LIST)
        self.chart.update_indicators(inds)

    def _on_ws_kline(self, symbol, tf, kline):
        """Live updates from WebSocket."""
        if symbol != self._active_symbol or tf != self._active_tf:
            return
            
        # Push to the new chart bridge
        self.chart.update_candle(kline)

def main():
    # Application setup
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QtWidgets.QApplication(sys.argv)
    
    # Apply theme
    apply_theme(getattr(config, 'CURRENT_THEME', 'Gray (Default)'), app)
    
    win = MainWindow()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()