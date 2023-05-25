import streamlit as st 
import numpy as np 
import ThongKe
import TimKiem
import DanhSach
import pandas as pd
import seaborn as sns


st.title("Hệ hỗ trợ quyết định nhập sách")
sidebar_radiio = st.sidebar.radio(
    'Chức Năng', 
    ("Thống Kê", "Tìm Kiếm", 'Danh Sách')
)

if sidebar_radiio == "Thống Kê": 
    tabSach, tabTacGia, tabTheLoai = st.tabs(["Theo Sách", "Theo Tác Giả", "Theo Thể Loại"])
    with tabSach: 
        add_selectbox = st.selectbox(
        "Thống kê theo sách",
        ("Top cuốn sách theo doanh số", "Top cuốn sách theo lượng review", "Top cuốn sách theo rating", "Top cuốn sách theo giảm giá"))
        Plot = ThongKe.Plot()
        k = st.number_input(label = 'Nhập k (chẳng hạn 10 thì sẽ hiển thị top 10)', min_value = 0, max_value = 100, value = 5)

        if add_selectbox == "Top cuốn sách theo doanh số": 
            fig = Plot.Topbook(k, 'quantity')
            st.pyplot(fig)
        elif add_selectbox == "Top cuốn sách theo lượng review": 
            fig = Plot.Topbook(k, 'n_review')
            st.pyplot(fig)
        elif add_selectbox == "Top cuốn sách theo rating": 
            fig = Plot.Topbook(k, 'avg_rating')
            st.pyplot(fig)
        else: 
            fig = Plot.Topbook(k, 'discount')
            st.pyplot(fig)    
        st.subheader('So sánh giữa Top {} với toàn bộ cuốn sách trong tập dữ liệu '.format(k))
        meanall, meantop = Plot.meanbook(k)
        col1, col2, col5 = st.columns(3)
        col3, col4 = st.columns(2)
        
        with col1: 
            st.metric(label="Số trang ", value= np.round((meantop.pages), 0), delta=np.round(meantop.pages - meanall.pages, 0), delta_color="normal")
        with col2:
            st.metric(label="rating", value= np.round(meantop.avg_rating, 2), delta=np.round(meantop.avg_rating - meanall.avg_rating, 2), delta_color="normal")
        with col3: 
            st.metric(label="Giá ban đầu", value= np.round(meantop.original_price, 0), delta=np.round(meantop.original_price - meanall.original_price, 0), delta_color="normal")
        with col4: 
            st.metric(label="Giá hiện tại", value= np.round(meantop.current_price, 0), delta=np.round(meantop.current_price - meanall.current_price, 0), delta_color="normal")
        with col5:
            st.metric(label="Tỷ lệ giảm giá", value= np.round(meantop.discount, 1), delta=np.round(meantop.discount - meanall.discount, 1), delta_color="normal")
        
        st.subheader("Mật độ giá hiện tại so với giá ban đầu")
        fig = Plot.price()
        st.pyplot(fig)
        st.subheader("Mật độ số trang")
        fig = Plot.pages()
        st.pyplot(fig)
    with tabTacGia: 
        j = st.number_input(label = 'Nhập k (chẳng hạn 10 thì sẽ hiển thị top 10)', min_value = 0, max_value = 100, value = 5, key='input4')
        st.subheader(' Top {} tác giả có nhiều sách nhất '.format(j))
        topTacGiaNhieuSach = Plot.topTacGiaNhieuSach(j)
        st.dataframe(topTacGiaNhieuSach)
        add_selectbox2 = st.selectbox(
        "Thống kê theo tác giả",
        ("Top tác giả theo doanh số", "Top tác giả theo lượng review", "Top tác giả theo rating", "Top tác giả theo giảm giá"))
        Plot = ThongKe.Plot()
        k = st.number_input(label = 'Nhập k (chẳng hạn 10 thì sẽ hiển thị top 10)', min_value = 0, max_value = 100, value = 5, key='input2')
        if add_selectbox2 == "Top tác giả theo doanh số": 
            fig = Plot.Topauthors(k, 'quantity')
            st.pyplot(fig)
        elif add_selectbox2== "Top tác giả theo lượng review": 
            fig = Plot.Topauthors(k, 'n_review')
            st.pyplot(fig)
        elif add_selectbox2 == "Top tác giả theo rating": 
            fig = Plot.Topauthors(k, 'avg_rating')
            st.pyplot(fig)
        else: 
            fig = Plot.Topauthors(k, 'discount')
            st.pyplot(fig)
        st.subheader('So sánh giữa Top {} với toàn bộ cuốn sách trong tập dữ liệu '.format(k))
        meanall, meantop = Plot.meanauthor(k)
        col1, col2, col5 = st.columns(3)
        col3, col4 = st.columns(2)
        
        with col1: 
            st.metric(label="Số trang ", value= np.round((meantop.pages), 0), delta=np.round(meantop.pages - meanall.pages, 0), delta_color="normal")
        with col2:
            st.metric(label="rating", value= np.round(meantop.avg_rating, 2), delta=np.round(meantop.avg_rating - meanall.avg_rating, 2), delta_color="normal")
        with col3: 
            st.metric(label="Giá ban đầu", value= np.round(meantop.original_price, 0), delta=np.round(meantop.original_price - meanall.original_price, 0), delta_color="normal")
        with col4: 
            st.metric(label="Giá hiện tại", value= np.round(meantop.current_price, 0), delta=np.round(meantop.current_price - meanall.current_price, 0), delta_color="normal")
        with col5:
            st.metric(label="Tỷ lệ giảm giá", value= np.round(meantop.discount, 1), delta=np.round(meantop.discount - meanall.discount, 1), delta_color="normal")
        


    with tabTheLoai: 
        m = st.number_input(label = 'Nhập k (chẳng hạn 10 thì sẽ hiển thị top 10)', min_value = 0, max_value = 100, value = 5, key='inputm')
        st.subheader('{} thể loại có số lượng sách bán được nhiều nhất '.format(m))
        Topcategory = Plot.categoryInTop(m)
        st.dataframe(Topcategory)
        add_selectbox2 = st.selectbox(
        "Thống kê theo thể loại",
        ("Top thể loại theo doanh số", "Top thể loại theo lượng review", "Top thể loại theo rating", "Top thể loại theo giảm giá"))
        Plot = ThongKe.Plot()
        k = st.number_input(label = 'Nhập k (chẳng hạn 10 thì sẽ hiển thị top 10)', min_value = 0, max_value = 100, value = 5, key='input3')
        if add_selectbox2 == "Top thể loại theo doanh số": 
            fig = Plot.Topcategory(k, 'quantity')
            st.pyplot(fig)
        elif add_selectbox2== "Top thể loại theo lượng review": 
            fig = Plot.Topcategory(k, 'n_review')
            st.pyplot(fig)
        elif add_selectbox2 == "Top thể loại theo rating": 
            fig = Plot.Topcategory(k, 'avg_rating')
            st.pyplot(fig)
        else: 
            fig = Plot.Topcategory(k, 'discount')
            st.pyplot(fig)
        st.subheader('So sánh giữa Top {} với toàn bộ cuốn sách trong tập dữ liệu '.format(k))
        meanall, meantop = Plot.meancategory(k)
        col1, col2, col5 = st.columns(3)
        col3, col4 = st.columns(2)
        
        with col1: 
            st.metric(label="Số trang ", value= np.round((meantop.pages), 0), delta=np.round(meantop.pages - meanall.pages, 0), delta_color="normal")
        with col2:
            st.metric(label="rating", value= np.round(meantop.avg_rating, 2), delta=np.round(meantop.avg_rating - meanall.avg_rating, 2), delta_color="normal")
        with col3: 
            st.metric(label="Giá ban đầu", value= np.round(meantop.original_price, 0), delta=np.round(meantop.original_price - meanall.original_price, 0), delta_color="normal")
        with col4: 
            st.metric(label="Giá hiện tại", value= np.round(meantop.current_price, 0), delta=np.round(meantop.current_price - meanall.current_price, 0), delta_color="normal")
        with col5:
            st.metric(label="Tỷ lệ giảm giá", value= np.round(meantop.discount, 1), delta=np.round(meantop.discount - meanall.discount, 1), delta_color="normal")
elif sidebar_radiio == "Tìm Kiếm": 
    col1, col2 = st.columns(2)

    with col1:
        radio_search = st.radio(
            "Tìm kiếm theo 👇",
            ("Tên Sách", "Tác Giả"), 
            key= 'TimKiem'
        )

    with col2:
        text_input = st.text_input(
            "Enter some text 👇",
        )
    Tim = TimKiem.Tim()
    if radio_search == "Tên Sách": 
        result = Tim.TimTheoTen(text_input)
        result = result.reset_index(drop=True)
        st.dataframe(result)
    else: 
        result = Tim.TimTheoTacGia(text_input)
        result = result.reset_index(drop=True)
        st.dataframe(result)
        #st.pyplot(fig)
    selected_indices = st.multiselect('Chọn hàng:', result.index)
    selected_rows = result.loc[selected_indices]
    selected_rows_id = result.loc[selected_indices]['product_id']
    st.write('### Sách đã chọn', selected_rows)  
    Ds = DanhSach.DanhSach()
    DsThuVien = Ds.showDSThuVien()
    selectbox = st.selectbox('Chọn danh sách', DsThuVien.Name)
    if st.button('Thêm vào danh sách'): 
        for id in selected_rows_id: 
            Ds.addnewbook(id, selectbox)
        st.success('Đã lưu')
else: 
    st.button("Re-run")
    st.subheader("Các danh sách")
    Ds = DanhSach.DanhSach()
    DsThuVien = Ds.showDSThuVien()
    st.dataframe(DsThuVien)
    col1Ds, col2Ds = st.columns(2)
    with col1Ds: 
        textboxList = st.text_input('Tên Danh Sách mới')
    with col2Ds: 
        btcreateList = st.button('Thêm', type= 'primary')
    if btcreateList: 
        Ds.createListbook(textboxList)
        st.success("Đã tạo danh sách")
    st.subheader("Chi tiết danh sách ")
    selectList = st.selectbox('Chọn danh sách', DsThuVien.Name)
    st.write('{}'.format(selectList))
    Listbook = Ds.showThuVien(selectList)
    st.dataframe(Listbook)
    
    
    
        
    







    







