// 1.
const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
// cho phép server đọc dữ liệu dạng JSON
app.use(express.json());
// phục vụ thư mục staticfiles
app.use('/static', express.static(path.join(__dirname, 'staticfiles')));


// 2.
// Lấy cổng từ biến môi trường của Render (process.env.PORT), nếu không có thì dùng 3000 (cho local)
const PORT = process.env.PORT || 3000; 


// 3. Định nghĩa một API đơn giản (route)
// ví dụ: trả về một trang HTML
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'staticfiles', 'base.html'));
});

app.get('/base', (req, res) => {
  res.sendFile(path.join(__dirname, 'home', 'Templates', 'base.html'));
});

app.get('/child1', (req, res) => {
  res.sendFile(path.join(__dirname, 'home', 'Templates', 'child1.html'));
});


// 4. Khởi động Server (Server bắt đầu lắng nghe yêu cầu)
app.listen(PORT, () => {
  console.log(`✅ Server đang chạy thành công tại http://localhost:${PORT}`);
  console.log('Server này đã sẵn sàng để triển khai lên Render.');
});