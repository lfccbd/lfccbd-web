document.querySelectorAll(".buttonContainer").forEach((container) => {
    container.addEventListener("click", function (event) {
        const button = event.target.closest("button");

        if (button) {
            // get the unique media ID
            let mediaId = button.id;
            
            fetch(`/resources/media/content/${mediaId}/`)
                .then((response) => response.json())
                .then((data) => {
                    if (data.media_content && data.media_content.format == "Audio") {
                        document.getElementById("file_title").textContent = data.media_content.file_title;
                        document.getElementById("message_date").textContent = data.media_content.message_date;
                        document.getElementById("service").textContent = data.media_content.service;
                        const audioElement = document.getElementById("audioPlayer");

                        if (!audioElement) {
                            console.error("Audio element not found!");
                            return;
                        }
                        const player = videojs(audioElement);

                        player.src({
                            src: data.media_content.media_source,
                        });

                        player.load();
                        player.play();
                    } else if (data.media_content && data.media_content.format == "Video") {
                        document.getElementById("video_file_title").textContent = data.media_content.file_title;
                        document.getElementById("video_message_date").textContent = data.media_content.message_date;
                        document.getElementById("video_service").textContent = data.media_content.service;
                        const videoElement = document.getElementById("videoPlayer");

                        if (!videoElement) {
                            console.error("Video element not found!");
                            return;
                        }
                        const player = videojs(videoElement);

                        player.src({
                            src: data.media_content.media_source,
                        });

                        player.load();
                        player.play();
                    }
                })
                .catch((error) => console.error("Error fetching media content:", error));
        }
    });
});
