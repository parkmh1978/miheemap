import streamlit as st
import folium
from streamlit_folium import st_folium

# 관광명소 및 맛집 데이터(한글 지명/줄 바꿈 설명)
spots = [
    {
        "name": "헬싱키 대성당",
        "coords": [60.1699, 24.9527],
        "desc": "핀란드의 랜드마크입니다.\n아름다운 녹색 돔과\n하얀 외벽이 돋보이는 루터교 대성당이에요.",
        "eat": {
            "name": "카피 엥겔",
            "desc": "전통 핀란드 케이크와 커피로 유명합니다.\n고풍스러운 분위기에서 휴식을 느껴보세요."
        }
    },
    {
        "name": "수오멘린나 요새",
        "coords": [60.1464, 24.9891],
        "desc": "유네스코 세계문화유산에 지정된\n바다 위 섬의 역사가 가득한 요새입니다.",
        "eat": {
            "name": "수오멘린나 브루하우스",
            "desc": "현지 수제 맥주와 핀란드식 생선 요리가\n환상적입니다."
        }
    },
    {
        "name": "템펠리아우키오 교회",
        "coords": [60.1781, 24.9225],
        "desc": "암석 내부에 세워진 독특한 교회입니다.\n탁월한 음향 효과로도 유명합니다.",
        "eat": {
            "name": "카페 시발라",
            "desc": "신선한 샌드위치와 핀란드식 커피가 일품입니다.\n차분하고 쾌적한 분위기에서 여유를 즐기세요."
        }
    },
    {
        "name": "뤼나린마키 놀이공원",
        "coords": [60.1937, 24.9384],
        "desc": "핀란드에서 가장 오래되고 인기있는 테마파크입니다.\n다양한 놀이기구와 멋진 도시 전망을 즐길 수 있습니다.",
        "eat": {
            "name": "헤스부르거 뤼나린마키",
            "desc": "핀란드 대표 햄버거 체인입니다.\n신선한 식재료와 다양한 메뉴를 경험하세요."
        }
    },
    {
        "name": "누크시오 국립공원",
        "coords": [60.3073, 24.4993],
        "desc": "헬싱키 근교 최대의 자연공원입니다.\n아름다운 숲과 호수를 따라 걷기 좋아요.",
        "eat": {
            "name": "카페 할틱카",
            "desc": "직접 구운 빵과 수프가 인기입니다.\n하이킹 후 간단히 한 끼로 좋아요."
        }
    },
]

st.set_page_config(page_title="핀란드 명소・맛집 지도(한글)", layout="centered")
st.title("유럽인 인기 핀란드 관광명소 & 맛집 5선")
st.write("파란 마커: 관광명소 | 빨간 마커: 추천 맛집\n\n마커를 클릭하면 상세 설명이 나타납니다.")

# 지도 생성 (헬싱키 중심)
map_center = [60.1699, 24.9384]
m = folium.Map(location=map_center, zoom_start=8)

for spot in spots:
    # 관광명소 파란색 마커
    folium.Marker(
        location=spot["coords"],
        popup=folium.Popup(
            f'<b>{spot["name"]}</b><br>{spot["desc"].replace(chr(10), "<br>")}',
            max_width=300,
        ),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)
    # 맛집 빨간색 마커 (좌표 소폭 이동)
    shift = 0.003
    folium.Marker(
        location=[spot["coords"][0]+shift, spot["coords"][1]+shift],
        popup=folium.Popup(
            f'<b>{spot["eat"]["name"]}</b><br>{spot["eat"]["desc"].replace(chr(10), "<br>")}',
            max_width=300,
        ),
        icon=folium.Icon(color='red', icon='cutlery')
    ).add_to(m)

st_folium(m, width=750, height=500)
st.info("각 마커를 클릭하시면 관광명소와 추천 맛집에 대한 설명을 한글로 줄 바꿈하여 보실 수 있습니다.")
