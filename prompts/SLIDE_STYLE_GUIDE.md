# Slide Style Guide

## How to use this guide

Không cần đọc toàn bộ tài liệu này mỗi lần sửa slide.

### Khi tạo một deck mới

Đọc theo thứ tự:
- `Mục tiêu sư phạm`
- `Nguyên tắc không thương lượng`
- `Cấu trúc chuẩn của một deck 120 phút`
- `Pattern thường dùng (đặc thù PPLT)`
- `Quy trình chuẩn khi tạo hoặc sửa slide`

### Khi review một deck cũ

Đọc theo thứ tự:
- `Rubric rà soát một lecture`
- `Tiêu chuẩn ở mức section`
- `Tiêu chuẩn ở mức slide`
- `Quy tắc về hình ảnh`
- `Quy tắc về wording`
- `Quy tắc về code blocks`

### Khi review một slide cụ thể

Chỉ cần hỏi nhanh 4 câu:
- Slide này có đúng **một ý chính** không?
- Hình / công thức / code / bullet nào là **trung tâm**?
- Có thể bỏ bớt **20-30% chữ** mà vẫn giữ ý không?
- Caption / câu chốt và phần trung tâm có đang nói **cùng một điều** không?

Nếu bất kỳ câu nào trả lời là `không`, nên sửa slide trước khi sửa câu chữ chi tiết.

### Khi mở rộng một section stub hoặc chủ đề kỹ thuật mới

Đọc theo thứ tự:
- `Tiêu chuẩn ở mức section`
- `Tiêu chuẩn ở mức slide`
- `Quy tắc về hình ảnh`
- `Quy tắc về wording`
- các section liên quan trước đó trong cùng lecture

Mục tiêu là biến stub thành một chuỗi slide có mạch: từ vấn đề, tổng quan mô hình, từng thành phần chính, đến điểm khác so với mô hình trước.

## Phạm vi

Tài liệu này quy định tiêu chuẩn thiết kế và rà soát slide cho môn **Phương pháp luận lập trình** tại **Viện Trí tuệ nhân tạo, Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội**.

Phạm vi áp dụng:
- deck giảng lý thuyết 120 phút (mỗi tuần có thể chia thành 1-3 deck nhỏ)
- slide dùng để giảng trực tiếp trên lớp
- deck viết bằng HTML / Reveal.js

Tài liệu này **không** tối ưu trước cho:
- tutorial thực hành
- bài tập về nhà
- seminar nghiên cứu

## Mục tiêu sư phạm

Thứ tự ưu tiên:

1. **Dễ dạy trên lớp**
2. **Đúng bản chất kiến thức**
3. **Dễ cho sinh viên tự đọc lại**

Hệ quả:
- slide không phải là giáo trình thu nhỏ
- slide phục vụ nhịp giảng, không cố ghi lại mọi điều giảng viên sẽ nói
- nếu phải chọn giữa "đầy đủ" và "dễ dạy", ưu tiên "dễ dạy"
- nhưng vì PPLT có phần lý thuyết hình thức (lambda calculus, định lý Amdahl, hợp nhất Prolog), không được bóp méo bản chất để dễ giảng

## Đối tượng người học

Đối tượng chuẩn:
- sinh viên năm 2-3
- đã học lập trình cơ bản (C++ / Python)
- đã học cấu trúc dữ liệu
- chưa quen với FP thuần khiết, Prolog, lập trình song song
- thiên kỹ thuật hơn lý thuyết, nhưng đã sẵn sàng tiếp nhận khái niệm hình thức

Hệ quả:
- có thể dùng pseudocode và lập luận hình thức cơ bản (β-reduction, suy diễn Prolog…)
- nhưng không được mặc định sinh viên đã quen với ngôn ngữ của textbook nghiên cứu
- mỗi paradigm mới (FP / Logic / Parallel / AI) cần dẫn dắt bằng động lực + ví dụ trước khi vào hình thức
- mỗi slide phải có đủ trực giác để theo được trên lớp

## Nguyên tắc không thương lượng

1. **Ít chữ**
- mỗi slide chỉ giữ lượng chữ cần thiết để giảng
- không biến slide thành ghi chú bài giảng

2. **Mỗi slide một ý chính**
- một slide chỉ nên trả lời một câu hỏi hoặc chốt một thông điệp
- nếu có hai ý ngang nhau, nên tách thành hai slide

3. **Tiếng Việt tự nhiên**
- ưu tiên diễn đạt như đang giảng cho sinh viên
- không dịch sát cấu trúc câu tiếng Anh
- thuật ngữ: tiếng Việt trước, tiếng Anh trong ngoặc khi cần (xem `Translation table`)

4. **Phần phụ phải được đánh dấu**
- nội dung không cần giảng trên lớp gắn badge `📚 Nâng cao`

5. **Visual language thống nhất**
- màu sắc, spacing, caption, badge, hộp nhấn, tiêu đề phải cùng một hệ
- pattern lặp lại nhiều thì đưa vào CSS chung

6. **Chủ đề kỹ thuật quan trọng phải được bung thành chuỗi slide**
- không gói một mô hình, thuật toán, kiến trúc hoặc bước chuyển tư duy lớn vào một slide tổng quan
- mỗi chủ đề quan trọng cần đi từ vấn đề cần giải quyết, ý tưởng tổng thể, kiến trúc hoặc pipeline, từng thành phần chính, cách huấn luyện hoặc suy luận nếu có, điểm khác so với mô hình trước, rồi đến hạn chế và tình huống dễ lỗi
- slide tổng quan chỉ là cửa vào; phần quan trọng nằm ở các slide giải phẫu cơ chế

7. **Mỗi slide kỹ thuật nên có trung tâm trực quan**
- với mô hình thị giác máy tính, mạng nơ-ron, pipeline xử lý ảnh, loss hoặc metric, mỗi slide nên có hình minh họa hợp lý
- hình không được chỉ để trang trí; hình phải làm rõ dữ liệu đi đâu, tensor đổi hình dạng thế nào, module nào tác động lên thông tin nào, hoặc quyết định nào được tạo ra ở bước nào
- nếu không có hình từ paper hoặc nguồn phù hợp, có thể dùng sơ đồ tự vẽ theo style của deck, miễn là chính xác và dễ đọc

8. **Ngôn ngữ mặc định là thuần Việt**
- viết câu tự nhiên bằng tiếng Việt
- chỉ giữ nguyên công thức, ký hiệu toán học, tên mô hình, tên viết tắt chuẩn và thuật ngữ buộc phải giữ như `IoU`, `FPN`, `RoI`, `CNN`, `ViT`
- khi cần dùng thuật ngữ tiếng Anh, ưu tiên viết tiếng Việt trước; thêm tiếng Anh trong ngoặc ở lần xuất hiện đầu nếu giúp người học tra cứu

## Những điều bị cấm hoặc nên tránh mạnh

1. **Bullet dài**
- một bullet dài quá hai dòng là tín hiệu xấu
- nếu ý dài, đổi sang câu ngắn hoặc tách slide

2. **Slide dày chữ**
- nếu người xem phải đọc quá 10-12 dòng liên tục, slide đang quá nặng

3. **Nhiều ý trong một slide**
- "định nghĩa + trực giác + ví dụ + cảnh báo" trong cùng một slide thường là sai

4. **Hình / sơ đồ nhỏ**
- SVG mà phải nheo mắt mới đọc được thì xem như chưa đạt
- font trong SVG <14px là dấu hiệu phải tăng kích thước

5. **Caption mơ hồ**
- caption không được chỉ mô tả "đây là hình gì"
- caption phải chốt được "hình này cho thấy điều gì"

6. **Fragment animation** (`class="fragment"`)
- không dùng. Slide hiển thị full để giảng viên điều khiển bằng lời, sinh viên có thể review nhanh sau buổi học.

7. **`<p class="inline-code">`**
- class `.inline-code` chỉ dành cho `<span>`. Nếu cần block, viết `<p><span class="inline-code">…</span></p>`.

8. **Python cho ví dụ song song**
- GIL phá ý parallel thật sự. Dùng C++ với `std::thread`, `std::atomic`, `std::mutex`.

## Cấu trúc chuẩn của một deck 120 phút

Tuỳ tuần, 120 phút có thể chia thành 1-3 deck nhỏ. Tổng số slide cả tuần thường rơi vào **50-70 slide**, mỗi deck độc lập rơi vào **30-55 slide**.

Một deck lý thuyết chuẩn nên có:

1. **Mở bài**
- tiêu đề
- nội dung / agenda
- *(khuyến khích)* 1-2 slide tạo động lực bằng hook story cụ thể (AlphaGo, AXD301, ChatGPT, …)
- *(khuyến khích)* slide câu hỏi xuyên suốt — orange box ở đầu, trả lời dần qua các phần
- mục tiêu buổi học (kết quả mong đợi)

2. **Các phần nội dung chính**
- mỗi phần mở bằng slide h1 có đánh số phần
- *(mềm dẻo)* khi đổi chủ đề lớn: bridge slide "Nhìn lại và đi tiếp" 3-box (xem pattern)
- mỗi phần có một trục câu chuyện rõ

3. **Phần kết**
- tổng kết
- *(khuyến khích)* đóng vòng với hook story / câu hỏi xuyên suốt
- *(bắt buộc)* slide tự kiểm tra (4-6 câu)
- *(khuyến khích)* slide bài tập mở rộng (1 slide, 2-3 bài, mỗi bài cho 1 chủ đề chính)

### Số lượng slide gợi ý

- deck giảng 60 phút: 25-35 slide
- deck giảng 120 phút (1 deck duy nhất): 45-55 slide
- nếu deck > 60 slide: phải có chiến lược `📚 Nâng cao` hoặc lướt nhanh

### Nhịp hợp lý

Một phần nên đi theo nhịp:
- **động lực** (vì sao cần?)
- **ý tưởng** (cách tiếp cận chính)
- **cơ chế / công thức / code** (cách hoạt động)
- **ví dụ** (áp dụng cụ thể)
- **cảnh báo / khi nào dùng** (tradeoff)

Không nên đi theo nhịp:
- **định nghĩa**
- **định lý**
- **công thức**
- **thuật toán**
- **ví dụ**

vì như vậy sinh viên dễ mất trực giác từ sớm.

## Pattern thường dùng (đặc thù PPLT)

PPLT có nhiều paradigm + code thật + sơ đồ kiến trúc → đã hình thành một số pattern qua các bài lec06–lec10. Tài liệu hoá ở đây để áp dụng nhất quán.

### 1. Hook story + đóng vòng

**Mở bài**: chọn 1 ví dụ thật, cụ thể, gây tò mò:
- *lec09 — AXD301*: switch viễn thông Erlang 1M LOC, uptime "9 nines"
- *lec10 — AlphaGo*: 3 paradigm cùng giải Cờ Vây
- *lec07 — Head First DP*: case study quản lý đồ chơi vịt

**Đóng vòng** ở Tổng kết: quay lại hook, map từng khái niệm/paradigm với hook ban đầu. Ví dụ:
- "AlphaGo dùng Logic ở MCTS, Song song ở 1920 CPU train, AI ở policy network"
- "AXD301 đạt 9-nines nhờ FP thuần khiết → minh bạch tham chiếu → dễ chứng minh tính đúng"

### 2. Câu hỏi xuyên suốt

Slide mở bài (sau hook) đặt 1 câu hỏi mở, hiển thị trong **orange box**:

```html
<div style="background: #fff3e0; padding: 14px 18px; border-radius: 8px;
            border-left: 5px solid #ff9800;">
  <strong style="color: #e65100;">Câu hỏi xuyên suốt buổi học:</strong>
  <p style="margin-top: 0.3em; font-style: italic; font-size: 1.05em;">
    Vì sao FP cho phép ta <strong>suy luận chương trình như toán học</strong>?
  </p>
</div>
```

Trả lời dần qua các phần. Có 1 slide cuối "Quay lại câu hỏi xuyên suốt" tổng hợp câu trả lời.

### 3. Bridge slide "Nhìn lại và đi tiếp"

Khi chuyển giữa các phần lớn (hoặc đổi chủ đề), dùng pattern 3-box:

```html
<section style="font-size: 0.78em;">
  <h2>Nhìn lại và đi tiếp</h2>
  <div style="background: #e8f5e9; padding: 10px; border-radius: 8px;
              border-left: 5px solid #2e7d32;">
    <strong style="color: #2e7d32;">Ta vừa biết:</strong> ...
  </div>
  <div style="margin-top: 0.6em; background: #ffebee; padding: 10px;
              border-radius: 8px; border-left: 5px solid #c62828;">
    <strong style="color: #c62828;">Câu hỏi chưa giải được:</strong> ...
  </div>
  <div style="margin-top: 0.6em; background: #e3f2fd; padding: 10px;
              border-radius: 8px; border-left: 5px solid #1565c0;">
    <strong style="color: #1565c0;">Phần này trả lời:</strong> ...
  </div>
</section>
```

Mềm dẻo: dùng khi có chuyển mạch rõ. Bài liền mạch hoặc ngắn không cần.

### 4. Card stack (badge tròn số)

Cho concept lists 3-5 mục đồng hàng (ví dụ: 3 thành phần Prolog, 4 ràng buộc Sudoku, 4 bước trace):

```html
<div style="background: #e3f2fd; border: 1px solid #90caf9;
            border-radius: 8px; padding: 8px 14px;">
  <div style="display: flex; align-items: baseline; gap: 12px;">
    <span style="background: #1565c0; color: #fff; border-radius: 50%;
                 width: 24px; height: 24px;
                 display: inline-flex; align-items: center; justify-content: center;
                 font-weight: bold; flex-shrink: 0; font-size: 0.85em;">1</span>
    <strong style="color: #0d47a1;">Tên thành phần</strong>
    <span style="color: #555;">— mô tả ngắn</span>
  </div>
</div>
```

Dùng khi cần nhấn thứ tự + visual hierarchy. Lists đơn giản dùng `<ul>` thường.

### 5. Comparison 2 cột (cũ vs mới)

Cho slide so sánh "cách quen thuộc" vs "cách mới" (imperative vs FP, làm tay vs AI, tuần tự vs song song):

```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
  <div style="background: #fff3e0; ...">
    <strong>Cách quen thuộc</strong>
    <ul>...</ul>
  </div>
  <div style="background: #e8f5e9; ...">
    <strong>Cách mới</strong>
    <ul>...</ul>
  </div>
</div>
```

Cột "cũ" → cam/vàng nhạt (chưa lý tưởng). Cột "mới" → xanh lá (lựa chọn tốt hơn).

### 6. Code-heavy slide (1 cột + caption)

Cho slide chứa code dài (>10 dòng):
- 1 cột code chính giữa
- caption ngắn dưới chốt ý chính
- nếu code >30 dòng: tách slide hoặc nén bằng comment để giấu chi tiết phụ

```html
<section style="font-size: 0.74em;">
  <h2>Tiêu đề</h2>
  <pre><code class="language-cpp" data-trim>
// code...
  </code></pre>
  <p style="margin-top: 0.4em; text-align: center;
            font-style: italic; color: #555;">
    Caption chốt ý — VD: "Đây là mẫu kinh điển reduction: chia + gộp."
  </p>
</section>
```

Khi cần so sánh 2 phiên bản code → 2 cột (xem pattern Comparison).

### 7. SVG diagram

Dùng SVG inline khi concept có cấu trúc visual rõ:
- cây AST / cây quy giản (lec09 lambda calc)
- timeline song song / đồng thời (lec10)
- agent loop, kiến trúc bộ nhớ chia sẻ (lec10)
- đồ thị Amdahl, sơ đồ kim cương Confluence (lec09-10)

Quy tắc:
- font trong SVG ≥14px (sau scale)
- caption dưới SVG chốt thông điệp
- code Unicode (├ │ └) cho cây đơn giản; SVG cho cấu trúc phức tạp

### 8. Bài tập mở rộng (cuối bài)

1 slide, 2-3 box màu, mỗi bài 1 chủ đề chính:

```html
<section style="font-size: 0.7em;">
  <h2>Bài tập mở rộng</h2>
  <div style="background: #f3e5f5; padding: 8px 12px; ...">
    <strong style="color: #4a148c;">A. Lập trình logic (Prolog)</strong>
    [đề bài...]
  </div>
  <div style="background: #e1f5fe; ...">
    <strong>B. Lập trình song song (C++)</strong>
    [đề bài...]
  </div>
  <div style="background: #fff9c4; ...">
    <strong>C. Lập trình bằng AI</strong>
    [đề bài...]
  </div>
</section>
```

## Tiêu chuẩn ở mức section

Mỗi phần lớn phải trả lời được ba câu hỏi:

1. Phần này giải quyết vấn đề gì?
2. Nó nối với phần trước ra sao?
3. Sau phần này sinh viên phải nhớ điều gì?

### Khi mở rộng một section stub hoặc chủ đề mới

Một section mới không nên chỉ có 2-3 slide giới thiệu. Với mỗi kỹ thuật hoặc chủ đề quan trọng, hãy mở rộng thành một chuỗi slide đủ để người học nhìn thấy cơ chế bên trong.

Chuỗi slide nên có:

1. **Slide đặt vấn đề**
- nêu giới hạn cụ thể của mô hình hoặc cách làm trước đó
- chỉ rõ vì sao cần kỹ thuật mới

2. **Slide trực giác tổng quan**
- cho người học thấy bức tranh lớn: dữ liệu đầu vào, các khối chính, đầu ra
- không dùng slide này để thay thế phần giải thích chi tiết

3. **Các slide giải phẫu thành phần**
- mỗi thành phần chính nên có ít nhất một slide riêng nếu nó quyết định hành vi của mô hình
- với kiến trúc mạng, cần tách các khối như encoder, decoder, skip connection, attention, proposal, head, fusion, loss hoặc post-processing khi chúng có vai trò riêng
- với thuật toán, cần tách các bước như tạo ứng viên, căn chỉnh đặc trưng, phân loại, hồi quy, gộp kết quả, lọc kết quả

4. **Slide về bước chuyển tư duy**
- bắt buộc có khi chủ đề mới thay đổi cách nhìn so với phần trước
- ví dụ: từ phân loại ảnh sang dự đoán theo pixel, từ downsample rồi upsample sang giữ chi tiết bằng skip connection, từ convolution cục bộ sang attention toàn cục, từ semantic segmentation sang instance segmentation, từ instance/semantic riêng rẽ sang panoptic segmentation thống nhất

5. **Slide về huấn luyện, suy luận hoặc hàm mất mát**
- thêm khi cơ chế học hoặc cơ chế suy luận là lý do mô hình hoạt động
- không chỉ ghi tên loss; cần nói loss kéo tham số theo hướng nào và lỗi nào sẽ bị phạt

6. **Slide so sánh và nối mạch**
- kết section bằng slide so sánh với các mô hình trước hoặc slide chốt lại trade-off
- trong cùng một lecture, section mới phải tham chiếu mạch đã xây trước đó, ví dụ FCN -> U-Net -> DeepLab -> U-Net + ViT -> Mask R-CNN -> panoptic segmentation

### Slide mở phần phải làm gì

Slide mở phần không chỉ để đánh số.

Nó nên giúp sinh viên chuẩn bị tâm trí:
- đây là chủ đề gì
- tại sao phải học nó
- nó nằm ở đâu trong câu chuyện chung

Nếu phần mới mở ra một bước mới trong narrative, nên có một bridge slide ngắn (xem pattern bridge).

## Tiêu chuẩn ở mức slide

### 1. Mỗi slide phải có một câu chốt ẩn

Trước khi viết slide, phải trả lời:
- nếu sinh viên chỉ nhớ **một câu** sau slide này, câu đó là gì?

Nếu không trả lời được, slide chưa đủ rõ.

### 2. Mỗi slide chỉ nên có một loại tải chính

Một slide chỉ nên có **một thứ làm trung tâm**:
- hình / sơ đồ
- công thức
- code
- bảng so sánh
- quy trình
- ví dụ

Nếu slide có cả hình, cả công thức, cả code, cả 6 bullet, gần như chắc chắn cần tách.

### 3. Slide kỹ thuật không được dừng ở mức tổng quan

Một slide kỹ thuật đạt yêu cầu khi người học có thể chỉ vào hình hoặc công thức và giải thích được:
- input là gì
- output là gì
- thành phần chính làm biến đổi thông tin theo cách nào
- vì sao bước này giúp giải quyết lỗi hoặc giới hạn của mô hình trước

Tránh các slide chỉ liệt kê ưu điểm / nhược điểm chung chung như "hiệu quả hơn", "chính xác hơn", "học đặc trưng tốt hơn" mà không chỉ ra cơ chế.

### 4. Hình minh họa trên slide kỹ thuật

Hình minh họa nên thuộc một trong các loại sau:
- **sơ đồ pipeline**: dùng khi cần thấy luồng dữ liệu qua nhiều bước
- **sơ đồ kiến trúc**: dùng khi cần thấy module, nhánh, skip connection, attention, head hoặc fusion
- **ảnh ví dụ đầu vào / đầu ra**: dùng khi cần thấy bài toán và lỗi mô hình
- **bản đồ đặc trưng hoặc mask**: dùng khi cần giải thích dự đoán theo không gian
- **biểu đồ so sánh**: dùng khi cần nêu trade-off về độ chính xác, tốc độ, bộ nhớ hoặc loại lỗi

Mỗi hình cần có nhãn đủ rõ để tự đứng được trong lúc giảng. Caption hoặc callout nên nói insight chính, không chỉ nhắc lại tên hình.

### 5. Dấu hiệu slide đang quá tải

Slide nên bị xem là quá tải nếu có một trong các dấu hiệu:
- trên 3 bullet chính
- có bullet dài quá 2 dòng
- có nhiều hơn 1 công thức độc lập
- có 2 hình trở lên mà không có quan hệ so sánh rõ ràng
- code dài > 30 dòng + bullet bên cạnh
- có text nhỏ phải giảm font để "nhét vừa"
- có cả trực giác, chi tiết kỹ thuật, và ví dụ cùng lúc

Khi gặp các dấu hiệu này:
- tách slide
- hoặc xác định một ý là phụ và bỏ đi
- hoặc gắn `📚 Nâng cao` cho slide phụ

### 6. Mật độ chữ

#### Mức tốt
- 1 câu mở đầu ngắn
- 2-3 bullet ngắn
- hoặc 1 hình lớn + 1 caption
- hoặc 1 code block + 1 câu chốt

#### Mức chấp nhận được
- 1 đoạn ngắn + 1 công thức + 2 bullet
- 1 code block + 3-4 bullet giải thích

#### Mức xấu
- 1 đoạn dài
- 4-6 bullet
- chú thích nhỏ
- công thức dài
- hình nhỏ ở góc

## Quy tắc về wording

### 0. Thuần Việt nhưng không dịch máy móc

- viết bằng tiếng Việt tự nhiên, ngắn và chính xác
- không lạm dụng tiếng Anh khi tiếng Việt diễn đạt được rõ hơn
- không dịch ép các viết tắt, tên mô hình, tên paper, ký hiệu toán học hoặc công thức
- nếu một thuật ngữ tiếng Anh là chuẩn tra cứu, có thể giữ nguyên sau phần tiếng Việt, ví dụ: "căn chỉnh vùng quan tâm (`RoIAlign`)"
- dùng cùng một cách gọi xuyên suốt deck; không đổi qua lại giữa nhiều bản dịch cho cùng một khái niệm

### 1. Viết như đang giảng, không như đang dịch

Ưu tiên:
- câu chủ động
- nhịp nói tự nhiên
- mệnh đề ngắn

Tránh:
- câu bị động nặng
- cấu trúc "theo textbook"
- mô phỏng cú pháp tiếng Anh

Ví dụ tốt:
- `FP cho ta minh bạch tham chiếu — biểu thức luôn cho cùng giá trị bất kể cách tính.`

Ví dụ xấu:
- `Tính minh bạch tham chiếu được FP cung cấp thông qua việc đảm bảo các biểu thức cho cùng giá trị bất kể chiến lược tính toán.`

### 2. Dùng thuật ngữ tiếng Anh có chọn lọc

**Quy tắc chung**: tiếng Việt trước, tiếng Anh trong ngoặc khi cần.

Ví dụ: *"thao tác nguyên tử (atomic)"*, *"khoá loại trừ (mutex / lock)"*.

Giữ tiếng Anh khi:
- đó là tên chuẩn mà sinh viên sẽ gặp lại trong tài liệu / công nghiệp
- dịch sang tiếng Việt làm tối nghĩa hơn

Ví dụ thường nên giữ:
- FP / OOP (đã quá phổ biến)
- backtracking (cũng dịch nhưng song song)
- agent, tool use, context engineering
- pthread, OpenMP, MPI (tên công nghệ)

Ví dụ nên Việt hoá:
- referential transparency → minh bạch tham chiếu
- race condition → tranh chấp
- deadlock → khoá chết
- starvation → bỏ đói
- predicate → vị từ
- unification → hợp nhất
- inheritance → kế thừa

Nguyên tắc:
- hoặc Việt hoá rõ ràng
- hoặc giữ tiếng Anh có chủ đích
- không pha trộn lộn xộn trong cùng một cụm

Bảng đầy đủ → xem `Translation table` cuối tài liệu.

### 3. Không dùng câu quá mạnh khi bản chất chỉ là "thường"

Ví dụ nên tránh:
- `FP luôn tốt hơn imperative`
- `Lambda calculus là cách duy nhất hình thức hoá tính toán`
- `OOP giải quyết mọi vấn đề thiết kế`

Nên sửa thành:
- `FP có lợi thế rõ trong các bài toán song song và xử lý dữ liệu`
- `Lambda calculus là một mô hình tính toán Turing-đầy đủ`
- `OOP phù hợp khi bài toán có nhiều thực thể với hành vi rõ ràng`

### 4. Mỗi bullet phải là một ý trọn vẹn

Bullet tốt:
- `Closure cho phép hàm "nhớ" biến từ phạm vi tạo ra nó.`

Bullet xấu:
- `Nhớ biến`

Bullet xấu vì:
- không tự đứng được
- phải đoán ý

## Quy tắc về hình ảnh / SVG

### 1. Hình phải làm việc thật sự

Mỗi hình phải có ít nhất một vai trò rõ:
- tạo trực giác
- minh hoạ một cơ chế
- cho ví dụ
- so sánh hai phương pháp
- làm nổi một cảnh báo

Nếu hình chỉ để "làm slide đỡ trống", nên bỏ.

### 2. Hình phải đủ lớn

Hình tốt:
- là phần trung tâm của slide
- các chi tiết đọc được ở chế độ trình chiếu (1024×768 projector)
- text trong SVG ≥14px sau scale

Hình xấu:
- bị ép nhỏ để nhường chỗ cho quá nhiều chữ
- có text trong hình nhỏ hơn caption

Khi phải chọn:
- giảm chữ
- không giảm hình

### 3. Không dùng caption mơ hồ

Caption tốt:
- `β-reduction "ăn" từng redex từ trái qua phải, dừng ở dạng chuẩn.`
- `Tăng số lõi → speedup giảm dần do phần tuần tự cố định (Amdahl).`

Caption xấu:
- `Ví dụ minh hoạ`
- `Sơ đồ`
- `So sánh`

### 4. Hình phải khớp thông điệp của slide

Một slide có tiêu đề `Đồng thời ≠ Song song` thì hình phải giúp người xem thấy ngay:
- 1 timeline thể hiện đồng thời (1 lõi quay vòng)
- 1 timeline thể hiện song song (nhiều lõi cùng chạy)

Nếu hình không đỡ cho tiêu đề, thay hình hoặc đổi tiêu đề.

### 5. SVG inline ưu tiên

Ưu tiên SVG inline (không gọi file ngoài) cho:
- sơ đồ nhỏ-vừa (cây, timeline, kiến trúc)
- hình có thể edit nhanh khi cần đổi nội dung

File ảnh ngoài (PNG/SVG file) chỉ dùng cho:
- ảnh thật (chân dung, screenshot)
- hình phức tạp đã render từ Matplotlib/script

Nếu hình được sinh bằng script:
- giữ script trong `img/.../scripts`
- sửa bằng script, không vá ảnh bằng tay

## Quy tắc về công thức

### 1. Công thức chỉ xuất hiện khi giúp hiểu

Chỉ giữ công thức nếu nó làm được ít nhất một trong ba việc:
- định nghĩa đúng bản chất (vd: β-reduction `(λx.M) N → M[N/x]`)
- giải thích cơ chế (vd: định luật Amdahl `1/(s + p/n)`)
- kết nối với một công thức sinh viên đã biết

Nếu công thức chỉ để "đúng sách", nên lược bớt.

### 2. Một slide không nên có nhiều công thức ngang vai

Nếu có hai công thức mà cả hai đều quan trọng:
- tách slide
- hoặc một công thức chính, một công thức phụ trong lời giảng

### 3. Công thức phải có câu dẫn và câu chốt

Không được để công thức rơi từ trên trời xuống.

Cần đủ ba thành phần:
- câu dẫn: tại sao đang nhìn công thức này
- công thức
- câu chốt: công thức nói điều gì

Ví dụ:
- `Tăng số lõi $n$ liệu có giảm thời gian chạy tỉ lệ?`
- `$\text{speedup} = \dfrac{1}{s + p/n}$`
- `Phần tuần tự $s$ là cổ chai — tăng $n$ vô hạn cũng chỉ đạt $1/s$.`

### 4. Ký hiệu phải nhất quán

Nếu đã dùng:
- `expr` cho expression (không dùng `exp` để tránh nhầm với epsilon)
- `lambda` cho hàm ẩn danh trong pseudocode (không dùng `fn`)
- `\(\beta\)` cho beta-reduction trong prose, `beta` (word) trong heading

thì giữ nhất quán đến hết deck đó.

### 5. Render math (KaTeX)

- Plugin: `RevealMath.KaTeX` đăng ký trong `Reveal.initialize`.
- Inline math: `\(...\)` (an toàn trong attribute) hoặc `$...$`.
- Display math: `\[...\]` hoặc `$$...$$`.

Ký tự đặc biệt (β, α, λ, …) trong prose:
- ✅ Trong text thường: `\(\beta\)`, `\(\alpha\)`, `\(\lambda\)` — KaTeX render đẹp.
- ❌ **Không dùng `\(...\)` trong heading h1/h2/h3**: CSS `text-transform: uppercase` sẽ phá `\beta` thành `\BETA`. Dùng word: *"Quy giản beta"*, *"Tương đương alpha"*.
- ✅ Trong `<pre><code>` và `<svg><text>`: giữ char gốc β/α/λ — không cần `\(...\)`.

## Quy tắc về code blocks

PPLT có nhiều code → có quy tắc riêng quan trọng.

### 1. `data-trim` mặc định

Mọi code block phải có `data-trim` để Reveal trim whitespace đầu/cuối:

```html
<pre><code class="language-cpp" data-trim>
long long tong = 0;
for (auto x : data) tong += x * x;
</code></pre>
```

### 2. Custom highlight.js languages

Đăng ký qua `beforeHighlight` callback trong `Reveal.initialize`. Đã có 2 ngôn ngữ tự định nghĩa:

- `mlpseudo`: ML-style pseudocode với keyword `lambda` (lec08-09).
- `prolog`: Prolog/CLP syntax (lec10).

Mẫu đăng ký:

```js
highlight: {
  beforeHighlight: function (hljs) {
    if (!hljs.getLanguage('mlpseudo')) {
      hljs.registerLanguage('mlpseudo', function () {
        return {
          name: 'ML Pseudo',
          keywords: 'fun val lambda fn let in if then else case of nil true false',
          contains: [
            { className: 'comment', begin: /\(\*/, end: /\*\)/ },
            { className: 'number', begin: /\b\d+\b/ }
          ]
        };
      });
    }
    // tương tự cho prolog...
  }
}
```

### 3. Pseudocode style cho slide PPLT

- **`lambda` thay vì `fn`** cho hàm ẩn danh — gần Python/JavaScript hơn:
  ```
  val square = lambda x => x * x;
  ```
- **`expr` thay vì `exp`** — tránh nhầm với epsilon trong toán.
- **`(* comment *)` kiểu ML** — phân biệt với `// comment` của C-style.
- Khi muốn nghiêm túc hơn (slide nâng cao): có thể chuyển sang Haskell `\x -> x*x` hoặc SML thật `fn x => x*x`.

### 4. Layout slide chứa code

**Mặc định**: 1 cột code + caption ngắn (xem pattern 6).

**Ngoại lệ — 2 cột compare**: chỉ khi so sánh 2 version code (cũ vs mới, tuần tự vs song song, sai vs đúng):

```html
<div style="display: flex; gap: 18px;">
  <div style="flex: 1;">
    <strong>Tuần tự</strong>
    <pre><code class="language-cpp" data-trim>...</code></pre>
  </div>
  <div style="flex: 1;">
    <strong>Song song</strong>
    <pre><code class="language-cpp" data-trim>...</code></pre>
  </div>
</div>
```

### 5. Code dài (>30 dòng)

- Tách slide
- Hoặc nén bằng comment giấu chi tiết phụ:
  ```prolog
  sudoku(Bang) :-
    % 1. Bàn cờ 9x9 (chi tiết bỏ qua)
    setup(Bang, CacO),
    % 2. Mỗi ô ∈ 1..9
    CacO ins 1..9,
    % 3. Mỗi hàng / cột / khối phân biệt
    constraints(Bang).
  ```
- Hoặc thay code bằng card stack mô tả high-level (xem pattern 4).

### 6. Theme

Code block dùng **monokai dark** mặc định (theme đã include trong `plugin/highlight/`). Cho code inline trong card → có thể override `style="background: none; color: inherit;"` để hoà visual.

## Quy tắc về ví dụ

### 1. Ví dụ phải phục vụ ý chính, không được mở nhánh mới

Ví dụ tốt:
- minh hoạ đúng khái niệm vừa giới thiệu
- không cần giải thích thêm 3 tầng bối cảnh

Ví dụ xấu:
- vừa giới thiệu khái niệm mới
- vừa có dataset / framework lạ
- vừa đòi giải thích domain

### 2. Mỗi ví dụ chỉ nên phục vụ một thông điệp

Ví dụ tốt:
- `Sudoku` để minh hoạ CLP(FD) ràng buộc miền hữu hạn
- `Tính tổng bình phương` để minh hoạ reduction parallel
- `parseCSV` để minh hoạ AI gợi ý ca biên

Đừng bắt một ví dụ gánh quá nhiều vai.

### 3. Ví dụ trong slide nên chốt điều rút ra

Không chỉ cho code / ảnh.

Phải có một câu kiểu:
- `Y combinator chứng minh đệ quy không cần tên — chỉ cần điểm cố định.`
- `4 thread cùng `tong += x` không khoá → kết quả mỗi lần chạy mỗi khác.`
- `Một ví dụ Sudoku hoàn chỉnh: chỉ 4 ràng buộc, máy giải trong ms.`

## Quy tắc về bảng

Bảng chỉ nên dùng khi thật sự cần so sánh theo nhiều tiêu chí.

### Bảng tốt khi:
- số cột ít (3-4)
- mỗi ô ngắn
- dùng để ra quyết định / so sánh
- có cột "khi nào dùng"

### Bảng xấu khi:
- mỗi ô là một câu dài
- người xem phải đọc như đọc văn bản
- biến bảng thành bản tóm tắt cả chương

Ví dụ bảng tốt: bảng "So sánh nhanh 3 paradigm" cuối lec10:

| Cách tiếp cận | Mạnh ở đâu | Câu hỏi điển hình |
|---|---|---|
| Logic | Suy diễn, ràng buộc | "Điều gì đúng?" |
| Song song | Tăng tốc, tăng tải | "Làm sao chạy cùng lúc?" |
| AI | Hỗ trợ quy trình | "Cộng tác với công cụ thế nào?" |

## Quy tắc về badge `📚 Nâng cao`

### Khi nào gắn

Gắn badge khi slide:
- là chi tiết kỹ thuật phụ (vd: chứng minh định lý chi tiết)
- là ví dụ mở rộng (vd: bài toán phân tán phức tạp)
- là benchmark / case phụ
- không cần để theo kịp mạch chính trên lớp

### Khi nào không gắn

Không gắn nếu slide:
- là bản lề logic
- chứa khái niệm lõi
- cần để hiểu slide sau
- là bài tập mở rộng cuối bài (đã có badge riêng kiểu khác)

### Cách dùng

Cần CSS class `.advanced-badge` (định nghĩa trong `lecture-style.css` nếu chưa có). Đặt ngay sau `<h2>`:

```html
<h2>Tên slide</h2>
<div class="slide-badge-row">
  <span class="advanced-badge">📚 Nâng cao</span>
</div>
```

Không dùng inline style riêng cho badge.

## Visual language

### 1. Color palette

PPLT standardize **6 màu + role** thống nhất qua tất cả deck:

| Màu | Hex (text/bg) | Role |
|-----|---------------|------|
| 🟢 Xanh lá | `#2e7d32` / `#e8f5e9` | "Ta vừa biết" / kết quả đúng / lựa chọn tốt |
| 🔴 Đỏ | `#c62828` / `#ffebee` | "Câu hỏi chưa giải" / SAI / cảnh báo nặng |
| 🔵 Xanh dương | `#1565c0` / `#e3f2fd` | "Phần này trả lời" / khái niệm / neutral |
| 🟠 Cam | `#ef6c00` / `#fff3e0` | Hook / câu hỏi xuyên suốt / cảnh báo nhẹ |
| 🟣 Tím | `#7b1fa2` / `#f3e5f5` | Đáp án / điểm cốt lõi / kết luận |
| 🟡 Vàng | `#f9a825` / `#fff9c4` | Highlight / starvation / bài tập C |

Không đổi mapping màu tuỳ tiện giữa các slide cùng một deck.

### 2. Hộp nhấn — `.question-box` (quy tắc nghiêm ngặt)

`.question-box` có **padding lớn, viền dày, font đậm** → tốn diện tích nhiều. Chỉ dùng khi thật sự cần *nhấn mạnh*.

**✅ Dùng `.question-box` khi:**
- **Đặt câu hỏi mở** cho sinh viên suy nghĩ (đúng tên class `question-box`).
- **Insight cốt lõi / điểm chốt** của 1 phần — câu giảng viên muốn sinh viên nhớ nhất.
- **Cảnh báo / lưu ý quan trọng** không thể bỏ qua.
- **Định nghĩa khung** (1 câu duy nhất) cho khái niệm trọng tâm của slide.

**❌ KHÔNG dùng `.question-box` cho:**
- **Liệt kê 3-5 mục đồng hàng** (vd: 4 khái niệm đồng bộ, 4 vai trò AI). → Dùng **card stack** (background nhẹ + border-left, mỗi card 1-2 dòng).
- **Mô tả thông thường** không cần nhấn mạnh. → Dùng `<p>` thường hoặc `<ul>`.
- **Caption / chú thích** dưới hình. → Dùng `<p style="font-style: italic; color: #555;">`.
- **Note nhỏ** trong slide đã có nhiều element khác. → Dùng inline span với màu nhạt.

**Quy tắc số lượng**: tối đa **1-2 question-box / slide**. Có 3+ box trong cùng slide là tín hiệu lạm dụng — cần đổi ít nhất một số sang card stack hoặc bullet thường.

**Card stack thay thế** (pattern compact, đẹp hơn cho lists):
```html
<div style="background: #e3f2fd; border: 1px solid #90caf9; border-radius: 8px; padding: 7px 14px;">
  <strong style="color: #0d47a1;">Tên thuật ngữ</strong>
  <span style="color: #555;">— định nghĩa ngắn.</span>
  <span style="color: #888; font-style: italic;">Khi nào dùng / ví dụ.</span>
</div>
```

→ 1 dòng text trong card, padding 7px 14px (mỏng hơn question-box). Lặp 3-5 card, gap 0.35em giữa các card.

### 3. Font size

Mặc định section 0.7-0.85em. Khi overflow:
- ưu tiên giảm content (bỏ caption thừa, gộp bullet)
- chỉ giảm font 0.05em sau khi đã thử nén content
- nếu phải giảm font dưới 0.65em — gần như chắc chắn cần tách slide

### 4. Căn lề và spacing

Deck phải có nhịp đều:
- khoảng cách giữa title và body (~0.5em)
- khoảng cách caption (~0.3-0.5em)
- khoảng cách giữa hai cột (`gap: 16-24px`)
- khoảng cách trong lists

Spacing không đều làm deck nhìn kém chắc tay, dù nội dung đúng.

## Tiêu chuẩn kỹ thuật cho Reveal.js / HTML

### 1. Section structure

- Top-level `<section>` = "phần lớn" (Section 1, 2, 3, ...) — có h1 với số phần.
- Inner `<section>` = vertical slide trong phần.
- Bridge slide làm thành 1 top-level `<section>` riêng giữa các phần (không phải vertical).

### 2. Không lạm dụng inline style

Inline style chấp nhận được khi:
- chỉnh đặc thù cho một slide
- layout thật sự đặc biệt
- prototype pattern mới

Không nên:
- lặp cùng một block style ở 5+ slide
- tự phát minh badge / note / callout mới bằng inline style

Khi pattern lặp lại nhiều:
- đưa vào CSS chung (`lecture-style.css`)

### 3. Asset phải có nguồn tái sinh

Nếu hình được sinh bằng code:
- giữ script trong `img/.../scripts`
- sửa bằng script, không vá ảnh bằng tay nếu tránh được

### 4. Cache busting

Khi asset SVG/PNG được render lại nhưng file name giữ nguyên:
- thêm hoặc tăng query string nếu cần để tránh cache khi preview

### 5. Tính nhất quán giữa slide và asset

Nếu slide nói:
- `MCTS / Policy Network / Value Network`

thì:
- caption
- title trong sơ đồ
- thứ tự trong cards
- màu của badge

phải cùng một mapping.

## Translation table (math/CS terms)

Bảng thuật ngữ chuẩn dùng xuyên suốt các deck PPLT đã được tách ra file riêng:

➡️ **[`glossaries.yaml`](./glossaries.yaml)**

### Quy tắc dùng

- **Mặc định**: tiếng Việt trước, tiếng Anh trong ngoặc nếu cần — ví dụ *"thao tác nguyên tử (atomic)"*, *"truyền thông điệp (message passing)"*, *"tái cấu trúc (refactor)"*.
- **`keep_en: true`** trong YAML → giữ nguyên tiếng Anh có chủ đích (vd `agent`, `context engineering`, `commit`, `diff`).
- **Tên công nghệ giữ nguyên** — xem mục `keep_en_technologies` cuối file (vd pthread, OpenMP, MPI, Spark, MapReduce, GitHub, Cursor, Claude Code…).

### Cấu trúc file

```yaml
sections:
  - title: <Tên nhóm thuật ngữ>     # vd "Lập trình logic"
    terms:
      - en: <English term>
        vi: <Bản dịch tiếng Việt>
        note: <Ghi chú khi dùng>     # tuỳ chọn
        keep_en: true                # tuỳ chọn — giữ tiếng Anh có chủ đích
keep_en_technologies:                # tên công nghệ không Việt hoá
  - <Technology>
```

Khi thêm/sửa thuật ngữ mới: chỉnh trực tiếp `glossaries.yaml`, không thêm vào file này.

## Rubric rà soát một lecture

### A. Ở mức deck

1. Deck có một câu chuyện rõ từ đầu đến cuối không?
2. Có phần nào bị nặng hơn nhu cầu dạy thực tế không?
3. Có slide nào là "notes" trá hình không?
4. Phần nào nên gắn `📚 Nâng cao`?
5. Có slide tổng kết đủ thực dụng không?
6. Có hook story và đóng vòng không (nếu deck đủ lớn)?

### B. Ở mức section

1. Mỗi phần có mục tiêu rõ không?
2. Phần mới có được nối với phần trước không?
3. Có bridge slide khi đổi chủ đề lớn không?
4. Slide mở phần có giúp sinh viên chuẩn bị tâm trí không?
5. Nếu section mở rộng một kỹ thuật quan trọng, nó có đủ chuỗi slide từ tổng quan đến thành phần chính không?
6. Có slide làm rõ bước chuyển tư duy so với mô hình hoặc cách làm trước không?

### C. Ở mức slide

1. Slide này có một ý chính rõ không?
2. Hình / công thức / code / bullet nào là trung tâm?
3. Nội dung có quá dày không?
4. Có thể bỏ bớt 30% chữ mà vẫn giữ ý không?
5. Caption có thật sự nói điều hình đang chứng minh không?
6. Code có data-trim chưa? Language class đúng chưa?
7. Với slide kỹ thuật, hình minh họa có thật sự giải thích cơ chế không?
8. Slide có trả lời được input, output, biến đổi chính và lý do kỹ thuật đó cần thiết không?

### D. Ở mức wording

1. Có câu nào dịch sát tiếng Anh không?
2. Có câu nào khẳng định quá mạnh không?
3. Thuật ngữ có nhất quán với Translation table không?
4. SV năm 2-3 có theo được câu này khi nghe trên lớp không?
5. Ngôn ngữ có thuần Việt không, trừ công thức, ký hiệu, tên mô hình và viết tắt chuẩn?

### E. Ở mức visual

1. Hình / SVG có đủ lớn không (text ≥14px sau scale)?
2. Có chỗ nào chồng lấn / quá sát / khó đọc không?
3. Màu có nhất quán với palette 6 màu + role không?
4. Hộp nhấn có dùng đúng chỗ không?
5. Code block có syntax color đúng không?
6. Section structure (top-level vs vertical) có đúng không?
7. Với mỗi kỹ thuật hoặc chủ đề quan trọng, đã có hình phù hợp cho các slide then chốt chưa?

### F. Ở mức kỹ thuật (PPLT-specific)

1. Có dùng `class="fragment"` không? (không được)
2. Có `<p class="inline-code">` không? (sai — phải `<span>`)
3. Math trong heading dùng word "beta" thay `\(\beta\)` chưa?
4. Code parallel dùng C++ chưa, hay nhầm Python?
5. Pseudocode dùng `lambda` chưa, hay còn `fn`?

## Quy trình chuẩn khi tạo hoặc sửa slide

### Khi tạo slide mới

1. Viết câu chốt của slide
2. Chọn loại slide:
   - hình / sơ đồ
   - công thức
   - code
   - bảng
   - ví dụ
   - quy trình
3. Bỏ mọi ý không phục vụ câu chốt
4. Viết wording ngắn và tự nhiên
5. Kiểm tra xem có cần tách slide không

### Khi mở rộng section stub

1. Đọc các section liên quan trước đó để nắm mạch giảng, thuật ngữ, mức chi tiết và style hình minh họa
2. Xác định các kỹ thuật hoặc thành phần quan trọng trong section mới
3. Lập chuỗi slide:
   - đặt vấn đề
   - tổng quan mô hình hoặc pipeline
   - từng thành phần chính
   - bước chuyển tư duy so với mô hình trước
   - huấn luyện / suy luận / loss nếu cần
   - so sánh và chốt phần
4. Viết nội dung bằng tiếng Việt tự nhiên; chỉ giữ công thức, viết tắt và tên chuẩn
5. Chọn hoặc vẽ hình minh họa cho từng slide kỹ thuật quan trọng
6. Soát lại để chắc chắn không có slide nào chỉ dừng ở mức "mô hình này tốt hơn" mà thiếu cơ chế

### Khi review slide cũ

1. Xác định slide đang cố làm mấy việc
2. Nếu hơn một việc, tách hoặc bỏ
3. Kiểm tra sự khớp giữa title, body và hình
4. Kiểm tra chỗ nào là textbook-speak
5. Kiểm tra section balance (`<section>` / `</section>`) sau khi sửa
6. Đánh dấu `📚 Nâng cao` nếu không phải lõi

### Khi sửa slide bị overflow

1. Đếm: bao nhiêu loại tải trên slide? Nếu >1 → tách trước
2. Nén content trước:
   - bỏ caption thừa (đã nói ở title)
   - gộp 2 bullet ngắn cùng ý
   - giảm padding `0.4 → 0.3em`
3. Giảm font 0.05em nếu vẫn tràn
4. Nếu vẫn tràn → tách slide hoặc gắn `📚 Nâng cao`

## Câu hỏi tự kiểm cuối cùng

Trước khi chốt một slide, tự hỏi:

1. Slide này có một ý chính rõ không?
2. Sinh viên có nhìn vào và biết mình đang học cái gì không?
3. Nếu bỏ bớt 20-30% chữ, slide có tốt hơn không?
4. Hình có đủ lớn để làm việc thật không?
5. Caption có chốt đúng thông điệp không?
6. Code có đúng convention (data-trim, language, lambda thay fn)?
7. Nếu giảng trên lớp, slide này giúp mình nói dễ hơn hay làm mình phải giải thích hộ slide?

Nếu câu 7 trả lời là:
- `phải giải thích hộ slide`

thì slide chưa đạt.

## Kết luận

Một deck tốt cho môn Phương pháp luận lập trình không phải là deck đầy đủ nhất.

Nó là deck:
- giúp giảng viên giữ được câu chuyện qua nhiều paradigm khác nhau
- giúp sinh viên bám được logic + có trực giác trước khi vào hình thức
- và làm nổi bật đúng những ý đáng nhớ

Trong ngữ cảnh môn này, ưu tiên luôn là:
- **dễ dạy**
- **đúng bản chất** (đặc biệt với các phần lý thuyết hình thức)
- **ít chữ nhưng rõ ý**
