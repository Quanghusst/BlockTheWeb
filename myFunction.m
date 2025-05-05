fs = 44100; % Tần số mẫu (Hz)
nBits = 16; % Số bit
nChannels = 1; % Số kênh (1 cho mono, 2 cho stereo)

% Khởi tạo đối tượng thu âm
recObj = audiorecorder(fs, nBits, nChannels);

% Bắt đầu thu âm
disp('Bắt đầu thu âm.');
recordblocking(recObj, 5); % Thu âm trong 5 giây
disp('Kết thúc thu âm.');

% Phát lại âm thanh đã thu
play(recObj);

% Lấy dữ liệu âm thanh
audioData = getaudiodata(recObj);

% Lưu dữ liệu vào file
audiowrite('myVoice.wav', audioData, fs);

% Tạo vector thời gian
time = (0:length(audioData)-1) / fs;

% Vẽ đồ thị
figure;
plot(time, audioData);
title('Tín hiệu âm thanh đã thu');
xlabel('Thời gian (s)');
ylabel('Biên độ');

