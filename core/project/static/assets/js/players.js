document.addEventListener('DOMContentLoaded', () => {
    const audio = videojs('audioPlayer', { controls: false });
    const playBtnAudio = document.getElementById('playBtnAudio');
    const pauseBtnAudio = document.getElementById('pauseBtnAudio');
    const rewindBtnAudio = document.getElementById('rewindBtnAudio');
    const forwardBtnAudio = document.getElementById('forwardBtnAudio');
    const fullScreenBtnAudio = document.getElementById('fullScreenBtnAudio');
    const progressBarAudio = document.getElementById('progressBarAudio');
    const currentTimeElAudio = document.getElementById('currentTimeAudio');
    const durationElAudio = document.getElementById('durationAudio');

    // Play audio
    function playAudio() {
        audio.play();
        playBtnAudio.disabled = true;
        pauseBtnAudio.disabled = false;
    }

    // Pause audio
    function pauseAudio() {
        audio.pause();
        playBtnAudio.disabled = false;
        pauseBtnAudio.disabled = true;
    }

    playBtnAudio.addEventListener('click', playAudio);
    pauseBtnAudio.addEventListener('click', pauseAudio);

    // Rewind
    rewindBtnAudio.addEventListener('click', () => {
        audio.currentTime(Math.max(0, audio.currentTime() - 10));
    });

    // Forward
    forwardBtnAudio.addEventListener('click', () => {
        audio.currentTime(Math.min(audio.duration(), audio.currentTime() + 10));
    });

    // Fullscreen
    fullScreenBtnAudio.addEventListener('click', () => {
        if (audio.isFullscreen()) {
            audio.exitFullscreen();
        } else {
            audio.requestFullscreen();
        }
    });

    // Update progress bar and time
    audio.on('timeupdate', () => {
        const percentage = (audio.currentTime() / audio.duration()) * 100;
        progressBarAudio.style.width = `${percentage}%`;

        const currentMinutes = Math.floor(audio.currentTime() / 60);
        const currentSeconds = Math.floor(audio.currentTime() % 60).toString().padStart(2, '0');
        currentTimeElAudio.textContent = `${currentMinutes}:${currentSeconds}`;
    });

    // Set duration on load
    audio.on('loadedmetadata', () => {
        const totalMinutes = Math.floor(audio.duration() / 60);
        const totalSeconds = Math.floor(audio.duration() % 60).toString().padStart(2, '0');
        durationElAudio.textContent = `${totalMinutes}:${totalSeconds}`;
    });

    // Reset video when modal is closed
    document.getElementById('audioPlayerModal').addEventListener('hide.bs.modal', () => {
        pauseAudio();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const video = videojs('videoPlayer', { controls: false });
    const customPlayPauseBtn = document.getElementById('customPlayPauseBtn');
    const playBtn = document.getElementById('playBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const rewindBtn = document.getElementById('rewindBtn');
    const forwardBtn = document.getElementById('forwardBtn');
    const fullScreenBtn = document.getElementById('fullScreenBtn');
    const progressBar = document.getElementById('progressBar');
    const currentTimeEl = document.getElementById('currentTime');
    const durationEl = document.getElementById('duration');

    // Play video
    function playVideo() {
        video.play();
        customPlayPauseBtn.style.display = 'none';
        playBtn.disabled = true;
        pauseBtn.disabled = false;
    }

    // Pause video
    function pauseVideo() {
        video.pause();
        customPlayPauseBtn.style.display = 'flex';
        playBtn.disabled = false;
        pauseBtn.disabled = true;
    }

    customPlayPauseBtn.addEventListener('click', playVideo);
    playBtn.addEventListener('click', playVideo);
    pauseBtn.addEventListener('click', pauseVideo);

    // Rewind
    rewindBtn.addEventListener('click', () => {
        video.currentTime(Math.max(0, video.currentTime() - 10));
    });

    // Forward
    forwardBtn.addEventListener('click', () => {
        video.currentTime(Math.min(video.duration(), video.currentTime() + 10));
    });

    // Fullscreen
    fullScreenBtn.addEventListener('click', () => {
        if (video.isFullscreen()) {
            video.exitFullscreen();
        } else {
            video.requestFullscreen();
        }
    });

    // Update progress bar and time
    video.on('timeupdate', () => {
        const percentage = (video.currentTime() / video.duration()) * 100;
        progressBar.style.width = `${percentage}%`;

        const currentMinutes = Math.floor(video.currentTime() / 60);
        const currentSeconds = Math.floor(video.currentTime() % 60).toString().padStart(2, '0');
        currentTimeEl.textContent = `${currentMinutes}:${currentSeconds}`;
    });

    // Set duration on load
    video.on('loadedmetadata', () => {
        const totalMinutes = Math.floor(video.duration() / 60);
        const totalSeconds = Math.floor(video.duration() % 60).toString().padStart(2, '0');
        durationEl.textContent = `${totalMinutes}:${totalSeconds}`;
    });

    // Reset video when modal is closed
    document.getElementById('videoPlayerModal').addEventListener('hide.bs.modal', () => {
        pauseVideo();
    });
});
