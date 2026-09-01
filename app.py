import streamlit as st
from healthsage import analyze_health


st.set_page_config(
    page_title="HealthSage AI",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 0%, rgba(56, 189, 248, 0.10), transparent 40%),
        radial-gradient(circle at 85% 20%, rgba(52, 211, 153, 0.10), transparent 40%),
        #0b0f19;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}

.hero {
    text-align: center;
    padding: 48px 24px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            rgba(14, 165, 233, 0.16),
            rgba(16, 185, 129, 0.16)
        );

    border-radius: 24px;
    border: 1px solid rgba(56, 189, 248, 0.25);

    box-shadow:
        0 20px 45px rgba(0, 0, 0, 0.35),
        inset 0 1px 0 rgba(255, 255, 255, 0.06);
}

.hero::before {
    content: "";
    position: absolute;
    top: -60%;
    left: -20%;
    width: 60%;
    height: 220%;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.18), transparent 70%);
    transform: rotate(20deg);
    pointer-events: none;
}

.hero h1 {
    font-family: 'Sora', sans-serif;
    font-size: 50px;
    font-weight: 800;
    letter-spacing: -0.02em;

    background:
        linear-gradient(90deg, #38bdf8, #34d399);

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #94a3b8;
    font-weight: 500;
    letter-spacing: 0.01em;
    margin: 0;
}

.hero .badge-row {
    margin-top: 18px;
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
}

.hero .badge {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #7dd3fc;
    background: rgba(56, 189, 248, 0.10);
    border: 1px solid rgba(56, 189, 248, 0.25);
    padding: 6px 14px;
    border-radius: 999px;
}


.section-label {
    font-family: 'Sora', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: 0.02em;
    margin: 6px 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.info-card {
    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.65),
            rgba(15, 23, 42, 0.75)
        );

    padding: 22px 24px;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.08);

    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
    transition: transform 0.2s ease, border-color 0.2s ease;
    margin-bottom: 15px;
}

.info-card:hover {
    transform: translateY(-3px);
    border-color: rgba(56, 189, 248, 0.35);
}

.info-card b {
    color: #38bdf8;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.card-value {
    color: #f8fafc;
    font-size: 21px;
    font-weight: 700;
    margin-top: 8px;
}

.summary-card {
    background:
        linear-gradient(
            145deg,
            rgba(14, 165, 233, 0.10),
            rgba(30, 41, 59, 0.75)
        );

    padding: 30px 32px;
    border-radius: 18px;
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-left: 4px solid #38bdf8;

    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.3);
    margin-top: 22px;
    margin-bottom: 28px;
}

.summary-title {
    font-family: 'Sora', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 12px;
}

.summary-text {
    font-size: 17px;
    color: #e2e8f0;
    line-height: 1.7;
}


.category-card {
    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.55),
            rgba(15, 23, 42, 0.65)
        );

    padding: 24px;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    min-height: 190px;

    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.25);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.category-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 32px rgba(0, 0, 0, 0.35);
}

.symptom-card { border-top: 3px solid #f87171; }
.cause-card { border-top: 3px solid #fb923c; }
.prevention-card { border-top: 3px solid #34d399; }


.category-title {
    font-family: 'Sora', sans-serif;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.symptom-title { color: #f87171; }
.cause-title { color: #fb923c; }
.prevention-title { color: #34d399; }


.item-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.item-list li {
    position: relative;
    padding-left: 20px;
    margin-bottom: 10px;
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.55;
}

.item-list li::before {
    content: "•";
    position: absolute;
    left: 0;
    font-weight: bold;
}

.symptom-list li::before { color: #f87171; }
.cause-list li::before { color: #fb923c; }
.prevention-list li::before { color: #34d399; }


.no-info {
    color: #64748b;
    font-size: 14px;
    margin-top: 10px;
    font-style: italic;
}


.keyword {
    display: inline-block;
    background: rgba(56, 189, 248, 0.10);
    color: #38bdf8;
    padding: 7px 16px;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.3);
    font-size: 14px;
    font-weight: 600;
    margin-right: 8px;
    margin-bottom: 8px;
    transition: background 0.2s ease, transform 0.15s ease;
}

.keyword:hover {
    background: rgba(56, 189, 248, 0.2);
    transform: translateY(-2px);
}


div.stButton > button {
    background: linear-gradient(135deg, #0ea5e9 0%, #10b981 100%);
    color: white;
    font-weight: 700;
    font-size: 16px;
    padding: 0.85rem 1.5rem;
    border-radius: 14px;
    border: none;
    box-shadow: 0 8px 22px rgba(14, 165, 233, 0.35);
    width: 100%;
    transition: transform 0.15s ease, box-shadow 0.2s ease;
    letter-spacing: 0.01em;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(14, 165, 233, 0.45);
}

div.stButton > button:active {
    transform: translateY(0px);
}

.stTextArea textarea {
    background-color: rgba(30, 41, 59, 0.55) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 16px !important;
    padding: 18px !important;
    font-size: 16px !important;
    transition: border-color 0.2s ease;
}

.stTextArea textarea:focus {
    border-color: rgba(56, 189, 248, 0.5) !important;
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.12) !important;
}


div[data-testid="stAlert"] {
    border-radius: 14px;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 55px;
    padding: 28px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    font-size: 14px;
    line-height: 1.6;
}

.footer b {
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>🏥 HealthSage</h1>
    <p>AI-Powered Health Information Analyzer</p>
    <div class="badge-row">
        <span class="badge">Symptoms</span>
        <span class="badge">Causes</span>
        <span class="badge">Prevention</span>
        <span class="badge">Keywords</span>
    </div>
</div>
""", unsafe_allow_html=True)


st.info(
    "HealthSage provides general educational information only. "
    "It does not diagnose medical conditions or replace professional medical advice."
)

st.markdown('<div class="section-label">📝 Enter Health Information</div>', unsafe_allow_html=True)


para = st.text_area(
    "Health Information",

    placeholder=(
        "Example: Type 2 diabetes is a chronic condition that affects "
        "how the body processes blood sugar. Common symptoms may include "
        "increased thirst, frequent urination, tiredness, and blurred vision."
    ),

    height=180,

    label_visibility="collapsed"
)


analyze = st.button(
    "🔍 Analyze with HealthSage",
    use_container_width=True
)



if analyze:
    if not para.strip():
        st.warning(
            "Please enter some health-related information."
        )
    else:
        with st.spinner(
            "HealthSage is analyzing your information..."
        ):
            health_data = analyze_health(para)

        if "error" in health_data:
            st.error(
                health_data["error"]
            )
        else:
            st.success(
                "Analysis completed successfully!"
            )
            st.markdown('<div class="section-label">🩺 Health Information</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                topic = health_data.get("topic") or "Not available"
                st.markdown(
                    f"""
                    <div class="info-card">
                        <b>Topic</b>
                        <div class="card-value">{topic}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                condition = health_data.get("condition") or "Not available"
                st.markdown(
                    f"""
                    <div class="info-card">
                        <b>Condition</b>
                        <div class="card-value">{condition}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            summary = health_data.get("summary") or "No summary available."
            if isinstance(summary, list):
                summary = " ".join(str(item) for item in summary)
            st.markdown(
                f"""
                <div class="summary-card">
                    <div class="summary-title">📌 Summary</div>
                    <div class="summary-text">{summary}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown('<div class="section-label">🔎 Breakdown</div>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            symptoms = health_data.get("symptoms", [])
            causes = health_data.get("causes", [])
            prevention = health_data.get("prevention", [])
            
            def create_list(items, list_class, bullet_color):
                if not items:
                    return '<p class="no-info">No information available.</p>'
                html = f'<ul class="item-list {list_class}">'
                for item in items:
                    html += f"""
                    <li>
                        <span style="position: absolute; left: 0; color: {bullet_color}; font-weight: bold;">•</span>
                        {item}
                    </li>
                    """
                html += "</ul>"
                return html

            with col1:
                symptoms_html = create_list(symptoms, "symptom-list", "#f87171")
                st.markdown(
                    f"""
                    <div class="category-card symptom-card">
                        <div class="category-title symptom-title">🔴 Symptoms</div>
                        {symptoms_html}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                causes_html = create_list(causes, "cause-list", "#fb923c")
                st.markdown(
                    f"""
                    <div class="category-card cause-card">
                        <div class="category-title cause-title">🟠 Causes</div>
                        {causes_html}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:
                prevention_html = create_list(prevention, "prevention-list", "#34d399")
                st.markdown(
                    f"""
                    <div class="category-card prevention-card">
                        <div class="category-title prevention-title">🟢 Prevention</div>
                        {prevention_html}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown('<div class="section-label">🔑 Keywords</div>', unsafe_allow_html=True)
            keywords = health_data.get("keywords", [])
            if keywords:
                keyword_html = "".join(
                    f'<span class="keyword">{keyword}</span>' for keyword in keywords
                )
                st.markdown(keyword_html, unsafe_allow_html=True)
            else:
                st.markdown(
                    '<p class="no-info">No keywords available.</p>',
                    unsafe_allow_html=True
                )
            with st.expander("📄 View JSON Response"):
                st.json(health_data)

st.markdown("""
<div class="footer">
    <b>HealthSage</b> • AI-Powered Health Information Analyzer
    <br><br>
    ⚠️ For educational purposes only.
    Always consult a qualified healthcare professional for medical advice.
</div>
""", unsafe_allow_html=True)
