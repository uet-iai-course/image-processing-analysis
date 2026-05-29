# Hình minh họa cho bài 13

Các hình có tiền tố `tracking-` trong thư mục này được tự vẽ lại dưới dạng SVG để dùng ngay trong `lecture-13-object-tracking.html`.

## Hình đã chuẩn bị

- `tracking-problem.svg`: minh họa một đối tượng đi qua nhiều khung hình và giữ cùng ID.
- `detection-to-tracking.svg`: so sánh phát hiện từng ảnh với bám bắt theo thời gian.
- `tracking-taxonomy.svg`: hai bài toán SOT và MOT.
- `tracking-failure-modes.svg`: trôi hộp, che khuất, mất dấu, đổi danh tính.
- `sot-iou-metric.svg`: minh họa IoU giữa hộp thật và hộp dự đoán.
- `sot-success-auc.svg`: minh họa đường thành công và AUC theo ngưỡng IoU.
- `sot-precision-metric.svg`: minh họa khoảng cách tâm hộp cho độ đo Precision.
- `mot-mota-metric.svg`: minh họa MOTA như tổng lỗi bỏ sót, báo thừa và đổi ID.
- `mot-motp-metric.svg`: minh họa MOTP như chất lượng định vị của các cặp đã ghép đúng.
- `mot-idf1-metric.svg`: minh họa IDF1 tập trung vào giữ đúng danh tính.
- `mot-hota-metric.svg`: minh họa HOTA cân bằng phát hiện và liên kết.
- `siamfc-online-vs-offline.svg`: minh họa bước chuyển từ học trực tuyến sang học hàm so khớp ngoại tuyến.
- `siamfc-pair-crops.svg`: minh họa tạo cặp mẫu mục tiêu và vùng tìm kiếm.
- `siamfc-architecture.svg`: kiến trúc tổng quan SiamFC với hai nhánh dùng chung trọng số.
- `siamfc-cross-correlation.svg`: minh họa tương quan chéo giữa đặc trưng mẫu và đặc trưng vùng tìm.
- `siamfc-response-map.svg`: minh họa bản đồ đáp ứng và cập nhật vị trí.
- `siamfc-label-loss.svg`: minh họa nhãn vị trí cho mất mát logistic của SiamFC.
- `siamfc-inference-loop.svg`: vòng suy luận cắt vùng - so khớp - cập nhật.
- `siamfc-limitations.svg`: các giới hạn chính của SiamFC, nối sang SiamRPN.
- `siamrpn-motivation.svg`: động lực từ SiamFC sang SiamRPN.
- `siamrpn-rpn-recall.svg`: nhắc lại RPN và cách SiamRPN đổi ý nghĩa RPN.
- `siamrpn-architecture.svg`: kiến trúc tổng quan SiamRPN với hai nhánh RPN.
- `siamrpn-anchor-grid.svg`: hộp neo trên lưới vùng tìm kiếm.
- `siamrpn-branches.svg`: hai nhánh phân loại và hồi quy trong SiamRPN.
- `siamrpn-anchor-assignment.svg`: gán nhãn hộp neo bằng IoU.
- `siamrpn-box-encoding.svg`: mã hóa hồi quy hộp từ hộp neo sang hộp thật.
- `siamrpn-loss.svg`: mất mát đa nhiệm của SiamRPN.
- `siamrpn-inference.svg`: quy trình suy luận của SiamRPN.
- `siamrpn-comparison.svg`: so sánh SiamFC và SiamRPN.
- `sort-detect-associate.svg`: quy trình bám bắt dựa trên phát hiện của SORT.
- `sort-state-vector.svg`: trạng thái hình học của một quỹ đạo trong SORT.
- `sort-kalman-cycle.svg`: vòng dự báo và cập nhật của bộ lọc Kalman.
- `sort-iou-cost.svg`: ma trận chi phí IoU giữa quỹ đạo và phát hiện.
- `sort-hungarian-assignment.svg`: ghép một-một bằng thuật toán Hungarian.
- `sort-track-lifecycle.svg`: vòng đời quỹ đạo: mới, thử nghiệm, xác nhận, xóa.
- `sort-occlusion-failure.svg`: lỗi đổi ID khi SORT gặp che khuất hoặc giao cắt.
- `deepsort-motivation.svg`: động lực thêm ngoại hình từ SORT sang DeepSORT.
- `deepsort-embedding.svg`: CNN ReID trích véc-tơ ngoại hình cho mỗi hộp.
- `deepsort-mahalanobis.svg`: khoảng cách Mahalanobis và cổng chuyển động.
- `deepsort-cosine-distance.svg`: khoảng cách cosine giữa các véc-tơ ngoại hình.
- `deepsort-matching-cascade.svg`: ghép tầng ưu tiên quỹ đạo vừa được cập nhật.
- `deepsort-reid-loss.svg`: mất mát ReID kéo cùng ID gần nhau và đẩy khác ID ra xa.
- `sort-deepsort-comparison.svg`: so sánh SORT và DeepSORT.

## Hình nên lấy về khi mở rộng các section sau

Đặt file vào cùng thư mục này, ưu tiên tên bên dưới để deck có thể tham chiếu ổn định:

- `siamfc-architecture-paper.png`: sơ đồ SiamFC từ Bertinetto et al., "Fully-Convolutional Siamese Networks for Object Tracking", arXiv:1606.09549. Nên dùng để chỉ nhánh mẫu mục tiêu, nhánh vùng tìm kiếm và phép tương quan chéo.
- `siamfc-response-map.png`: minh họa bản đồ đáp ứng của SiamFC; có thể thay bằng sơ đồ tự vẽ nếu không dùng hình gốc.
Nguồn tham khảo chính: Stanford CS231n Lecture 9, SiamFC, SiamRPN, SORT và DeepSORT. Khi dùng hình gốc từ bài báo hoặc slide, cần giữ chú thích nguồn ngay dưới hình trong deck.
