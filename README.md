# DSS
Hệ hỗ trợ nhập sách 
Sử dụng dữ liệu về doanh số bán hàng của các sản phẩm sách trên tiki để xây dựng hệ hỗ trợ quyết định nhập sách cho các của hàng. 
Ngoài việc phân tích dữ liệu về giá, tác giả, tôi còn sử dụng mô hình KNN để phân loại một cuốn sách xem có nên nhập hay không. 
# Mô hình KNN
Bài toán có: 
- input: thông tin của một cuốn sách: tác giả, nhà xuất bản, giá, thể loại.
- output: có hay không nên nhập cuốn sách.
Một số nhược điểm của mô hình:
- Mô hình có sử dụng feature là tác giả  ->  feature này được số hóa dựa trên việc đánh giá doanh số của tác giả trên tập trainig. -> feature này tương đối mạnh trong mô hình, đo đó dẫn đến việc các tác giả mới sẽ khó được chọn.
