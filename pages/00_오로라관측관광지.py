import streamlit as st
import folium
from streamlit_folium import st_folium

# 오로라 명소 및 맛집(한글 표기/줄 바꿈 설명)
spots = [
    {
        "name": "로바니에미",
        "coords": [66.5039, 25.7294],
        "desc": (
            "핀란드 라플란드의 중심 도시입니다.\n"
            "산타마을과 함께 오로라 관측 명소로 사랑 받습니다."
        ),
        "eat": {
            "name": "라피시 레스토랑",
            "desc": "사슴고기, 순록 스테이크 등\n핀란드 전통요리가 인기입니다."
        }
    },
    {
        "name": "아비스코 국립공원",
        "coords": [68.3586, 18.7837],
        "desc": (
            "스웨덴 북부의 아름다운 국립공원입니다.\n"
            "맑은 하늘과 탁 트인 시야가 장점인 오로라 명소입니다."
        ),
        "eat": {
            "name": "티오르나 파노라마",
            "desc": "공원 내 위치한 레스토랑으로\n스웨덴식 가정식과 산 전망을 자랑합니다."
        }
    },
    {
        "name": "옐로나이버",
        "coords": [62.4539, -114.3718],
        "desc": (
            "캐나다 노스웨스트 준주의 오로라 명소입니다.\n"
            "고요한 호수와 하늘을 배경 삼아 오로라 촬영지로도 유명합니다."
        ),
        "eat": {
            "name": "더 우디즈 레스토랑",
            "desc": "현지 해산물과 그릴 요리가 맛있기로 유명합니다.\n한국인 여행객 사이에서도 인기입니다."
        }
    },
    {
        "name": "트롬쇠",
        "coords": [69.6496, 18.9560],
        "desc": (
            "노르웨이 북극권 최대 도시입니다.\n"
            "도심에서도 환상적인 오로라를 감상할 수 있습니다."
        ),
        "eat": {
            "name": "피스크리스트로겟",
            "desc": "노르웨이식 신선한 해산물 요리를\n드실 수 있는 명물 맛집입니다."
        }
    },
    {
        "name": "키르나",
        "coords": [67.8558, 20.2253],
        "desc": (
            "스웨덴 북부 오로라 관광의 중심지입니다.\n"
            "오로라 익스프레스 열차 종착점으로 유명합니다."
        ),
        "eat": {
            "name": "스테키하우스 키르나",
            "desc": "현지에서 잡은 순록 및 사슴 스테이크가\n전문인 스테이크하우스입니다."
        }
    },
]

st.set_page_config(page_title="오로라 명소·맛집 지도(한글)", layout="centered")
st.title("🌌 한국인이 사랑하는 오로라 관측지 & 맛집 추천 (지명 한글)")
st.write(
    "파란색 마커는 오로라 명소, 빨간색 마커는 추천 맛집입니다.\n"
    "마커를 클릭하면 상세 설명이 줄 바꿈되어 한눈에 확인하실 수 있습니다."
)

# 폴리움 지도 생성
center_coords = [66.5, 20.0]
m = folium.Map(location=center_coords, zoom_start=3)

for spot in spots:
    # 오로라 명소 마커
    folium.Marker(
        location=spot["coords"],
        popup=folium.Popup(
            f'<b>{spot["name"]}</b><br>{spot["desc"].replace(chr(10), "<br>")}',
            max_width=300
        ),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)
    # 맛집 마커 (좌표 소폭 이동)
    shift = 0.2          # 오로라 명소마다 지역이 넓으므로 shift값 크게 적용
    folium.Marker(
        location=[spot["coords"][0]+shift, spot["coords"][1]+shift],
        popup=folium.Popup(
            f'<b>{spot["eat"]["name"]}</b><br>{spot["eat"]["desc"].replace(chr(10), "<br>")}',
            max_width=300
        ),
        icon=folium.Icon(color='red', icon='cutlery')
    ).add_to(m)

st_folium(m, width=800, height=500)
st.info("각 마커를 클릭하셔서 자세한 설명을 한글로 줄 바꿈과 함께 확인해보세요.")
