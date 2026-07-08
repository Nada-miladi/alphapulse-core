import streamlit as st
import httpx

# 1. Page Configuration and Custom Corporate Styling
st.set_page_config(
    page_title="AlphaPulse Terminals | Executive Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Injecting professional custom CSS to redesign standard Streamlit components
st.markdown(
    """
    <style>
        /* General background adjustments and typography */
        .main { background-color: #0d1117; color: #c9d1d9; }
        h1, h2, h3 { color: #ffffff !important; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 700; }

        /* Premium KPI Card Box Styling */
        .metric-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 20px;
            text-align: left;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .metric-label { font-size: 0.85rem; color: #8b949e; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }
        .metric-value { font-size: 1.8rem; font-weight: 700; margin-top: 5px; color: #f0f6fc; font-family: monospace; }

        /* Signal Badges */
        .badge-bullish { color: #39d353; font-weight: 700; background-color: rgba(57, 211, 83, 0.15); padding: 4px 8px; border-radius: 4px; border: 1px solid #238636; }
        .badge-bearish { color: #f85149; font-weight: 700; background-color: rgba(248, 81, 73, 0.15); padding: 4px 8px; border-radius: 4px; border: 1px solid #da3633; }
        .badge-neutral { color: #dbab09; font-weight: 700; background-color: rgba(219, 171, 9, 0.15); padding: 4px 8px; border-radius: 4px; border: 1px solid #9e7a04; }

        /* Executive Report Block Container */
        .report-box {
            background-color: #161b22;
            border-left: 4px solid #58a6ff;
            border-radius: 0 8px 8px 0;
            padding: 25px;
            margin-top: 20px;
            line-height: 1.6;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Main Executive Header Structure
st.markdown(
    "<h1 style='margin-bottom: 0;'>ALPHAPULSE CORE</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p style='color: #8b949e; font-size: 1.05rem; margin-top: 0; font-weight: 400;'>Institutional Intelligence System & Matrix Pipeline</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<hr style='border-top: 1px solid #30363d; margin-top: 10px; margin-bottom: 30px;'>",
    unsafe_allow_html=True,
)

# 3. Sidebar Infrastructure Control Panel
st.sidebar.markdown(
    "<h3 style='color: white;'>TERMINAL CONTROLS</h3>", unsafe_allow_html=True
)
ticker_input = (
    st.sidebar.text_input("ASSET TICKER SYMBOL:", value="AAPL").upper().strip()
)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
analyze_button = st.sidebar.button(
    "EXECUTE CORE PIPELINE", type="primary", use_container_width=True
)

st.sidebar.markdown(
    "<hr style='border-top: 1px solid #30363d;'>", unsafe_allow_html=True
)
st.sidebar.markdown(
    "<div style='font-size: 0.8rem; color: #8b949e; line-height: 1.4;'>"
    "<strong>SECURITY ASSURANCE:</strong><br>"
    "End-to-end framework execution actively monitoring chronological data matrix streams. "
    "Cognitive services are isolated via Groq hardware architectures."
    "</div> division",
    unsafe_allow_html=True,
)

# 4. Main Application Execution Logic
if analyze_button or ticker_input:
    with st.spinner("Processing pipeline services..."):
        try:
            # Query backend framework over local loopback connection
            backend_url = f"http://127.0.0.1:8000/analyze/{ticker_input}"
            response = httpx.get(backend_url, timeout=25.0)

            if response.status_code == 200:
                data = response.json()

                ticker = data["ticker"]
                date = data["date"]
                metrics = data["metrics"]
                report = data["analysis_report"]

                # Assign dynamic structural layout colors based on algorithmic signals
                sig = metrics["signal"].upper()
                if sig == "BULLISH":
                    badge_html = f"<span class='badge-bullish'>{sig}</span>"
                elif sig == "BEARISH":
                    badge_html = f"<span class='badge-bearish'>{sig}</span>"
                else:
                    badge_html = f"<span class='badge-neutral'>{sig}</span>"

                # Title header for current execution snapshot
                st.markdown(
                    f"### Quantitative Asset Footprint: {ticker} <span style='font-size:1rem; color:#8b949e; font-weight:normal;'>| Execution Reference: {date}</span>",
                    unsafe_allow_html=True,
                )

                # 5. Render Beautiful Premium Metric Grid Layout
                m_col1, m_col2, m_col3 = st.columns(3)
                with m_col1:
                    st.markdown(
                        f"""
                        <div class='metric-card'>
                            <div class='metric-label'>Closing Price (USD)</div>
                            <div class='metric-value'>${metrics['close_price']:.2f}</div>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )
                with m_col2:
                    st.markdown(
                        f"""
                        <div class='metric-card'>
                            <div class='metric-label'>5-Day Simple Moving Avg</div>
                            <div class='metric-value'>${metrics['moving_average_5d']:.2f}</div>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )
                with m_col3:
                    st.markdown(
                        f"""
                        <div class='metric-card'>
                            <div class='metric-label'>Pipeline Market Signal</div>
                            <div class='metric-value' style='margin-top: 10px; font-size:1.5rem;'>{badge_html}</div>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                # 6. Render the Multi-Agent Document Block
                st.markdown("### Executive Risk & Allocation Directive")
                st.markdown(
                    f"""
                    <div class='report-box'>
                        {report.replace('\n', '<br>')}
                    </div>
                """,
                    unsafe_allow_html=True,
                )

            else:
                st.error(f"Backend Server Failure: {response.status_code}")
                st.caption(response.text)

        except Exception as e:
            st.error("Connection Interface Disrupted.")
            st.warning(
                "Please confirm your backend service environment is active by initializing: `uvicorn src.api:app --reload` in a separate terminal branch."
            )
