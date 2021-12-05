from src.streamlit.purin import purin
from src.streamlit.fetch_twitter import fetch_twitter
from typing import Any

import streamlit
st = streamlit  # type: Any


def main():
    st.title("Pudding-Jigglypuff Disambiguation")
    keyword = "プリン"
    st.write(f"`{keyword}`の曖昧性解消")

    Menu = ["解析", "データ取得"]
    add_selectbox = st.sidebar.selectbox(
        "選択",
        Menu
    )
    match add_selectbox:
        case "解析":
            purin()
        case "データ取得":
            fetch_twitter(keyword)
        case _:
            pass


if __name__ == '__main__':
    main()
