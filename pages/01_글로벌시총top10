import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

def get_top_10_stocks():
    return [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 
        'META', 'TSLA', 'ASML', 'AVGO', 'ADBE'
    ]

@st.cache_data
def fetch_stock_data(tickers):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=3*365)
    
    try:
        data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
        return data
    except Exception as e:
        st.error(f"데이터 로딩 중 오류: {e}")
        return None

def plot_stock_prices(data):
    fig = go.Figure()
    
    for ticker in data.columns:
        fig.add_trace(go.Scatter(
            x=data.index, 
            y=data[ticker], 
            mode='lines', 
            name=ticker
        ))
    
    fig.update_layout(
        title='글로벌 Top 10 기업 주가 변동',
        xaxis_title='날짜',
        yaxis_title='주가 (조정)',
        height=600
    )
    
    return fig

def main():
    st.title('글로벌 Top 10 기업 주가 분석')
    
    tickers = get_top_10_stocks()
    stock_data = fetch_stock_data(tickers)
    
    if stock_data is not None:
        fig = plot_stock_prices(stock_data)
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()
