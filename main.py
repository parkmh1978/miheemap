import streamlit as st
import folium
from streamlit_folium import st_folium

# 명소 및 맛집 데이터 (한글 지명 표기)
spots = [
    {
        "name": "헬싱키 대성당",
        "coords": [60.1699, 24.9527],
        "description": "핀란드 헬싱키의 대표적인 랜드마크로, 건축미가 뛰어난 대성당입니다.",
        "eat": "카피 엥겔 - 핀란드 전통 디저트와 커피"
    },
    {
        "name": "수오멘린나 요새",
        "coords": [60.1464, 24.9891],
        "description": "유네스코 세계문화유산에 등재된 바닷가 요새로, 헬싱키 앞바다에 위치합니다.",
        "eat": "수오멘린나 브루하우스 - 현지 맥주와 북유럽식 요리"
    },
    {
        "name": "템펠리아우키오 교회",
        "coords": [60.1781, 24.9225],
        "description": "암석을 깎아 만든 독특한 교회로, 훌륭한 음향효과로도 유명합니다.",
        "eat": "카페 시발라 - 핀란드식 커피와 신선한 샌드위치"
    },
    {
        "name": "뤼나린마키 놀이공원",
        "coords": [60.1937, 24.9384],
        "description": "가족과 함께 즐기기 좋은 핀란드 최대의 테마파크입니다.",
        "eat": "헤스부르거 뤼나린마키 - 핀란드 대표 햄버거"
    },
    {
        "name": "롤로삼마키 국립공원",
        "coords": [60.5666, 27.5542],
        "description": "핀란드 자연의 아름다움을 느낄 수 있는 보호구역입니다.",
        "eat": "롤로삼마키 카페 - 홈메이드 빵과 커피"
    },
]

# Streamlit 페이지 기본 설정
st.set_page_config(page_title="핀란드 명소&맛집 지도(한글)", layout="centered")
st.title("🇫🇮 유럽인이 사랑하는 핀란드 관광명소・맛집 5선 (지명 한글 표기)")
st.write("파란색 마커: 관광명소 | 빨간색 마커: 추천 맛집입니다. 지도상의 지명은 모두 한글로 제공됩니다.")

# 지도 생성 (헬싱키 중심)
finland_center = [60.1699, 24.9384]
m = folium.Map(location=finland_center, zoom_start=8, tiles="OpenStreetMap")

for spot in spots:
    # 관광명소: 파란 마커
    folium.Marker(
        location=spot["coords"],
        popup=f"<b>{spot['name']}</b><br>{spot['description']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)
    # 맛집: 빨간 마커 (좌표 약간 이동)
    shift = 0.003
    folium.Marker(
        location=[spot["coords"][0] + shift, spot["coords"][1] + shift],
        popup=f"<b>{spot['eat']}</b>",
        icon=folium.Icon(color='red', icon='cutlery')
    ).add_to(m)
# Folium 지도 스트림릿에 출력
st_data = st_folium(m, width=700, height=500)
st.info("각 마커를 클릭하면 명소 및 맛집의 한글 이름과 설명을 확인하실 수 있습니다.")
