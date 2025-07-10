import streamlit as st
import folium
from streamlit_folium import st_folium

# 명소 및 맛집 데이터
spots = [
    {
        "name": "센소지(Asakusa)",
        "coords": [35.7148, 139.7967],
        "description": "도쿄에서 가장 오래된 사원으로, 일본 전통문화를 느끼기에 좋습니다.",
        "eat": "Asakusa Menchi(아사쿠사 멘치) - 수제고로케"
    },
    {
        "name": "시부야 스크램블(Shibuya)",
        "coords": [35.6595, 139.7005],
        "description": "세계적으로 유명한 교차로에서 도쿄의 에너지를 체험할 수 있습니다.",
        "eat": "Uobei(우오베이) - 회전스시"
    },
    {
        "name": "메이지 신궁(Harajuku)",
        "coords": [35.6764, 139.6993],
        "description": "도심 속 힐링 공간으로, 자연과 신사가 어우러진 곳입니다.",
        "eat": "Afuri Harajuku(아후리 하라주쿠) - 유자라멘"
    },
    {
        "name": "우에노공원(Ueno)",
        "coords": [35.7138, 139.7745],
        "description": "풍부한 자연과 박물관, 동물원이 있는 복합 공원입니다.",
        "eat": "Innsyoutei(인쇼테이) - 일본 전통 정식"
    },
    {
        "name": "긴자(Ginza)",
        "coords": [35.6717, 139.7650],
        "description": "명품 쇼핑과 세련된 거리로 유명합니다.",
        "eat": "Sushi Dai(스시 다이) - 일본식 초밥"
    },
]

# 스트림릿 페이지 세팅
st.set_page_config(page_title="도쿄 명소&맛집 추천", layout="centered")

st.title("🇯🇵 유럽인이 좋아하는 도쿄 관광명소・맛집 5선")
st.write("아래 지도에서 파란색 마커는 관광명소, 빨간색 마커는 해당 명소의 추천 맛집입니다.")

# 지도 생성 (중앙값 기준)
tokyo_center = [35.68, 139.76]
m = folium.Map(location=tokyo_center, zoom_start=12)

for spot in spots:
    # 관광명소: 파란 마커
    folium.Marker(
        location=spot["coords"],
        popup=f"<b>{spot['name']}</b><br>{spot['description']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

    # 맛집: 빨간 마커 (살짝 좌표 이동하여 겹치지 않게)
    shift = 0.001
    folium.Marker(
        location=[spot["coords"][0] + shift, spot["coords"][1] + shift],
        popup=f"<b>{spot['eat']}</b>",
        icon=folium.Icon(color='red', icon='cutlery')
    ).add_to(m)

# 지도 표시
st_data = st_folium(m, width=700, height=500)

st.info("※ 각 명소 명과 맛집명을 클릭하면 상세 설명을 볼 수 있습니다. 여행 준비에 참고하시기 바랍니다.")
