---
name: slide-text-style-editor
description: >-
  Chỉnh văn bản trên slide bài giảng tiếng Việt, đặc biệt là deck HTML/Reveal.js,
  theo phong cách trong slide style guide của dự án: ngắn gọn, tự nhiên, mỗi
  slide một ý chính, thuật ngữ tiếng Việt trước, tránh lộ văn AI. Dùng khi Codex
  cần sửa wording, rút gọn bullet, Việt hoá chữ trên slide, chỉnh caption/tiêu
  đề, kiểm tra và sửa chữ bị tràn khỏi vùng hiển thị, hoặc làm văn bản slide bớt
  máy móc nhưng vẫn giữ đúng công thức, code, tên viết tắt, tên mô hình và nội
  dung kỹ thuật.
---

# Slide Text Style Editor

## Mục tiêu

Chỉ chỉnh lớp chữ của deck, trừ khi người dùng yêu cầu đổi cấu trúc. Khi có `prompts/SLIDE_STYLE_GUIDE.md`, đọc các phần "Nguyên tắc không thương lượng", "Quy tắc về wording" và rubric wording trước khi sửa.

## Quy trình

1. Đọc các slide liên quan và nhận diện phần chữ hiển thị: tiêu đề, bullet, caption, hộp nhấn, nhãn, mục lục, câu hỏi và chữ dùng để giảng.
2. Giữ nguyên nội dung kỹ thuật: công thức, ký hiệu toán học, code, tên API, tên file, tên mô hình, tên paper, tên dataset và tên viết tắt chuẩn.
3. Tìm một ý chính của từng slide. Nếu chữ đang gánh nhiều ý ngang nhau, rút về ý trung tâm hoặc nêu rõ slide nên tách.
4. Viết lại bằng tiếng Việt ngắn, tự nhiên. Ưu tiên câu chủ động, động từ cụ thể và nhịp nói như đang giảng cho sinh viên.
5. Rà thuật ngữ cho nhất quán. Dùng tiếng Việt trước; chỉ đặt tiếng Anh trong ngoặc khi cần tra cứu hoặc tránh hiểu nhầm.
6. Gỡ chữ đệm kiểu AI, câu quá mạnh, giọng quảng cáo và câu bị động nặng.
7. Đọc lại từng slide để kiểm tra độ dày chữ: bullet không được thành đoạn văn; caption phải nói hình chứng minh điều gì, không chỉ gọi tên hình.
8. Kiểm tra chữ có bị tràn, chồng lấn hoặc vượt khỏi vùng slide không. Nếu có, sửa ngay theo thứ tự: rút chữ, tách bullet, xuống dòng có chủ đích, rồi mới chỉnh nhẹ kích thước/spacing nếu thật cần.

## Quy tắc chữ

Áp dụng mặc định:

- Viết bằng tiếng Việt mặc định.
- Giữ nguyên công thức, ký hiệu, code, định danh, tên viết tắt, tên mô hình, tên kiến trúc, tên dataset, tên paper, tên thư viện và tên công nghệ.
- Dùng tiếng Việt trước tiếng Anh: `căn chỉnh vùng quan tâm (RoIAlign)`, `thao tác nguyên tử (atomic)`.
- Không dịch máy móc tên viết tắt. Giữ các cụm như `IoU`, `FPN`, `RoI`, `CNN`, `ViT`, `API`, `GPU`, `OpenCV`, `PyTorch`.
- Ưu tiên câu ngắn và bullet đủ ý. Mỗi bullet nên tự đứng được.
- Tránh bullet dài quá hai dòng. Nếu dài, tách hoặc nén ý.
- Tránh khẳng định tuyệt đối khi bản chất chỉ là thường đúng. Đổi "luôn", "duy nhất", "tốt nhất" thành "thường", "phù hợp khi", "có lợi trong" nếu đúng hơn.
- Dùng một cách gọi ổn định cho cùng một khái niệm trong toàn deck.

## Lượt gỡ văn AI

Xoá hoặc viết lại các cụm chung chung, phồng chữ hoặc nghe như được sinh tự động:

- "đóng vai trò quan trọng trong việc..."
- "giúp nâng cao hiệu quả..."
- "một cách mạnh mẽ / toàn diện / tối ưu"
- "trong bối cảnh hiện đại..."
- "khám phá / đi sâu vào / tận dụng sức mạnh của..."
- "mang lại khả năng vượt trội..."
- "được sử dụng để thực hiện việc..."

Ưu tiên cách nói thẳng:

- "Mô hình dự đoán nhãn cho từng pixel."
- "Bộ mã hoá giảm kích thước ảnh và giữ đặc trưng chính."
- "IoU đo mức chồng khớp giữa dự đoán và nhãn đúng."
- "FPN ghép đặc trưng ở nhiều tỉ lệ để bắt cả vật nhỏ và vật lớn."

## Sửa HTML/Reveal

Khi sửa deck HTML:

- Chỉ sửa chữ hiển thị trong `h1`-`h4`, `p`, `li`, `span`, `strong`, `em`, `figcaption`, nhãn, hộp nhấn và ô bảng.
- Giữ nguyên cấu trúc HTML, tên class, inline style, data attribute, khối toán, hình học SVG và code block, trừ khi người dùng yêu cầu đổi.
- Không thêm class `fragment`.
- Giữ caption ngắn và có ý giải thích: nói hình cho thấy điều gì hoặc vì sao điều đó quan trọng.
- Nếu câu ngắn làm bố cục thoáng hơn, ưu tiên câu ngắn thay vì câu đầy đủ nhưng nặng.

## Kiểm tra tràn chữ

Sau khi sửa wording, phải kiểm tra khả năng hiển thị của slide, đặc biệt với tiêu đề dài, bullet nhiều dòng, bảng, nhãn trong SVG, caption và hộp nhấn.

Dấu hiệu cần sửa:

- Chữ vượt khỏi cạnh slide, cạnh box, bảng, button hoặc vùng SVG.
- Chữ chồng lên hình, công thức, code block hoặc nội dung kế tiếp.
- Bullet bị ép quá sát nhau sau khi xuống dòng.
- Tiêu đề chiếm quá nhiều chiều cao làm phần chính bị đẩy xuống.
- Một từ/cụm dài không xuống dòng được, ví dụ tên mô hình, định danh hoặc thuật ngữ tiếng Anh.

Thứ tự xử lý:

1. Rút chữ trước. Bỏ trạng từ, cụm đệm, câu dẫn và phần giải thích có thể giảng miệng.
2. Tách ý dài thành 2 bullet ngắn hoặc chuyển sang caption/callout ngắn hơn nếu đúng ngữ cảnh.
3. Xuống dòng có chủ đích ở cụm dễ đọc; không chèn ngắt dòng vào công thức, code, tên API hoặc định danh.
4. Nếu vẫn tràn, chỉnh layout tối thiểu: giảm `font-size` nhẹ, tăng vùng chứa, giảm `gap`/`margin`, hoặc đổi cột/bảng để chữ có chỗ thở.
5. Nếu phải giảm chữ nhỏ đến mức khó đọc, không tiếp tục nén. Nêu rõ slide nên tách hoặc cần đổi bố cục.

Khi có thể chạy slide trong trình duyệt, dùng ảnh chụp hoặc quan sát trực tiếp để kiểm tra lại sau chỉnh sửa. Nếu không thể render, rà bằng HTML/CSS và ưu tiên câu ngắn để giảm rủi ro tràn.

## Ví dụ

Trước: `Mạng tích chập đóng vai trò quan trọng trong việc trích xuất các đặc trưng thị giác từ ảnh đầu vào.`

Sau: `Mạng tích chập trích xuất đặc trưng thị giác từ ảnh đầu vào.`

Trước: `Các proposal được sử dụng để thực hiện việc xác định các vùng có khả năng chứa đối tượng.`

Sau: `Proposal gợi ý vùng có thể chứa đối tượng.`

Trước: `Semantic segmentation là một kỹ thuật quan trọng trong computer vision để gán nhãn cho từng pixel trong ảnh.`

Sau: `Phân đoạn ngữ nghĩa (semantic segmentation) gán nhãn cho từng pixel trong ảnh.`

Trước: `Kỹ thuật này luôn tốt hơn phương pháp cũ trong mọi trường hợp.`

Sau: `Kỹ thuật này thường tốt hơn khi ảnh có nhiều vật thể ở các tỉ lệ khác nhau.`

## Kiểm tra cuối

Trước khi kết thúc, xác nhận:

- Mỗi slide vẫn có một ý chính rõ.
- Chữ ngắn hơn trước, trừ khi cần thêm ngữ cảnh để đúng kỹ thuật.
- Tiếng Việt là ngôn ngữ mặc định.
- Tiếng Anh chỉ còn ở công thức, định danh, tên riêng, tên viết tắt chuẩn hoặc thuật ngữ tra cứu trong ngoặc.
- Không còn chữ tràn khỏi vùng hiển thị, chồng lấn hoặc bị ép đến mức khó đọc.
- Code, toán, cấu trúc SVG và hành vi slide không bị đổi ngoài ý muốn.
- Kết quả nghe như giảng viên nói thẳng, không giống bản tóm tắt do máy sinh ra.
