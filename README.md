# IG 貼文生成器

這個專案提供簡易的 IG 文章標題與 Hashtag 產生工具，包含 Python 後端與瀏覽器介面。

## 組成
- `generate_title.py`：依據主題與風格產生 3-5 個貼文標題。
- `hashtags.py`：依主題給出 10 個熱門 Hashtag。
- `main.py`：簡易 HTTP 伺服器，提供 `/generate` API 並回傳 JSON，亦可直接開啟 `web_ui.html`。
- `web_ui.html`：可輸入主題與選擇風格，按下按鈕即可看到產生的標題與 Hashtag。
- `examples/`：兩組範例輸入與輸出結果。

## 使用方式
1. 以 Python 執行 `main.py` 啟動伺服器：
   ```bash
   python3 main.py
   ```
   預設在 `http://localhost:8000` 提供服務。
2. 瀏覽器開啟 `web_ui.html` 或直接連到 `http://localhost:8000/`。
3. 輸入主題、選擇風格後按下「產生」，即可看到標題與 Hashtag。

僅依賴 Python 標準函式庫即可運作，方便快速展示。若要修改產生邏輯，可直接編輯相關 Python 檔案。
