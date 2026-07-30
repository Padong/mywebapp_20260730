import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="맞춤형 MBTI & 직업 추천기",
    page_icon="✨",
    layout="centered"
)

# MBTI별 대표 특징 및 추천 직업 데이터베이스
MBTI_DATA = {
    "INTJ": {"label": "용의주도한 전략가", "jobs": ["데이터 분석가", "소프트웨어 아키텍트", " 경영 컨설턴트", "연구원"]},
    "INTP": {"label": "논리적인 사색가", "jobs": ["백엔드 개발자", "물리학자", "시스템 엔지니어", "철학 연구원"]},
    "ENTJ": {"label": "대담한 통치자", "jobs": ["CEO / 기업가", "투자 은행가", "프로젝트 매니저(PM)", "변호사"]},
    "ENTP": {"label": "뜨거운 논쟁을 즐기는 변론가", "jobs": ["스타트업 창업가", "마케팅 기획자", "크리에이티브 디렉터", "정치인"]},
    "INFJ": {"label": "통찰력 있는 선도자", "jobs": ["심리상담사", "작가 / 카피라이터", "인사(HR) 전문가", "특수교사"]},
    "INFP": {"label": "잔망스러운 잔망루피형 중재자", "jobs": ["일러스트레이터", "콘텐츠 크리에이터", "시인/소설가", "번역가"]},
    "ENFJ": {"label": "정의로운 사회운동가", "jobs": ["선생님 / 교사", "시민단체 활동가", "라이프 코치", "홍보(PR) 전문가"]},
    "ENFP": {"label": "재기발랄한 활동가", "jobs": ["이벤트 기획자", "방송 PD", "여행 작가", "광고 기획자"]},
    "ISTJ": {"label": "청렴결백한 논리주의자", "jobs": ["회계사", "공무원", "데이터베이스 관리자", "품질 관리자"]},
    "ISFJ": {"label": "용감한 수호자", "jobs": ["간호사", "초등교사", "사회복지사", "자산 관리사"]},
    "ESTJ": {"label": "엄격한 관리자", "jobs": ["경영 관리자", "군인 / 경찰", "재무 분석가", "운영 이사"]},
    "ESFJ": {"label": "사교적인 외교관", "jobs": ["호텔 지배인", "고객 성공 매니저(CSM)", "행사 진행자", "승무원"]},
    "ISTP": {"label": "만능 재주꾼", "jobs": ["기계 공학자", "데이터 엔지니어", "응급구조사", "카레이서"]},
    "ISFP": {"label": "호기심 많은 예술가", "jobs": ["패션 디자이너", "조경사", "음악가", "수의사"]},
    "ESTP": {"label": "모험을 즐기는 사업가", "jobs": ["영업 대표", "부동산 중개인", "스포츠 코치", "투자자"]},
    "ESFP": {"label": "자유로운 영혼의 연예인", "jobs": ["연기자 / 배우", "이벤트 MC", "여행 가이드", "패션 스타일리스트"]}
}

# UI 타이틀 & 설명
st.title("✨ 맞춤형 MBTI & 직업 추천기")
st.write("당신의 MBTI와 수식어(형용사)를 입력하면, 나만의 특별한 직업 타이틀을 만들어 드립니다!")

st.divider()

# 사용자 입력 영역
col1, col2 = st.columns([1, 2])

with col1:
    selected_mbti = st.selectbox(
        "MBTI를 선택하세요",
        options=list(MBTI_DATA.keys()),
        index=0
    )

with col2:
    adjective_input = st.text_input(
        "원하는 수식어/형용사를 입력하세요",
        placeholder="ex) 귀엽고 깜찍하고 사랑스러운"
    )

# 결과 출력 버튼
if st.button("✨ 나만의 맞춤 직업 확인하기", use_container_width=True):
    # 입력값 세척 및 기본값 설정
    adj_text = adjective_input.strip() if adjective_input.strip() else "특별하고 유일무이한"
    mbti_info = MBTI_DATA[selected_mbti]
    
    st.divider()
    
    # 결과 하이라이트 카드가 들어갈 영역
    st.balloons()  # 축하 효과 애니메이션
    
    st.subheader(f"🎉 [{selected_mbti}] 당신을 위한 맞춤 추천 결과")
    st.caption(f"MBTI 유형 특징: **{mbti_info['label']}**")
    
    st.markdown("---")
    
    # 입력받은 형용사와 추천 직업 조합
    st.markdown("### 🌟 당신만을 위한 수식어 커스텀 직업")
    for job in mbti_info["jobs"]:
        st.markdown(f"- **{adj_text}** `{job}`")
        
    st.info("💡 **팁:** 상단의 형용사를 바꾸어 입력하면 매번 새로운 분위기의 타이틀을 만들 수 있어요!")
