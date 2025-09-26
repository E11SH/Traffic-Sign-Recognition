document.addEventListener('DOMContentLoaded', function () {
    //UI Elements
    const uploadForm = document.getElementById('upload-form');
    const videoFileInput = document.getElementById('videoFile');
    const fileNameSpan = document.getElementById('file-name');
    const loader = document.getElementById('loader');
    const statusText = document.getElementById('status-text');
    const resultsCard = document.getElementById('results-card');
    const processedVideo = document.getElementById('processed-video');
    const submitButton = uploadForm.querySelector('button');

    //Model Training History Data
    const history = {
        accuracy: [0.3680, 0.8589, 0.9284, 0.9566, 0.9621, 0.9681, 0.9757, 0.9750, 0.9779, 0.9778, 0.9825, 0.9852, 0.9843, 0.9729, 0.9872],
        val_accuracy: [0.7978, 0.9629, 0.9797, 0.9782, 0.9569, 0.9875, 0.9879, 0.9930, 0.9930, 0.9908, 0.9893, 0.9884, 0.9890, 0.9946, 0.9921],
        loss: [2.4144, 0.4381, 0.2248, 0.1383, 0.1163, 0.1019, 0.0751, 0.0795, 0.0722, 0.0730, 0.0549, 0.0458, 0.0520, 0.0926, 0.0428],
        val_loss: [0.6721, 0.1136, 0.0631, 0.0704, 0.1285, 0.0400, 0.0421, 0.0230, 0.0232, 0.0293, 0.0307, 0.0408, 0.0375, 0.0163, 0.0268]
    };
    const epochs = Array.from({ length: 15 }, (_, i) => i + 1);

    //Chart Rendering
    function createChart(canvasId, label, trainData, valData, trainColor, valColor) {
        const ctx = document.getElementById(canvasId).getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: epochs,
                datasets: [{
                    label: `Training ${label}`,
                    data: trainData,
                    borderColor: trainColor,
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    tension: 0.1
                }, {
                    label: `Validation ${label}`,
                    data: valData,
                    borderColor: valColor,
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' },
                    title: { display: true, text: `Model ${label} per Epoch` }
                },
                scales: {
                    x: { title: { display: true, text: 'Epoch' } },
                    y: { title: { display: true, text: label } }
                }
            }
        });
    }

    createChart('accuracyChart', 'Accuracy', history.accuracy, history.val_accuracy, 'rgba(0, 123, 255, 1)', 'rgba(40, 167, 69, 1)');
    createChart('lossChart', 'Loss', history.loss, history.val_loss, 'rgba(255, 193, 7, 1)', 'rgba(220, 53, 69, 1)');

    //File Input Handler
    videoFileInput.addEventListener('change', () => {
        fileNameSpan.textContent = videoFileInput.files.length > 0 ? videoFileInput.files[0].name : 'No file selected';
    });

    // Form Submission Handler
    uploadForm.addEventListener('submit', function (event) {
        event.preventDefault();
        
        const formData = new FormData();
        if (videoFileInput.files.length === 0) {
            alert("Please select a video file first.");
            return;
        }
        formData.append('videoFile', videoFileInput.files[0]);

        //Update UI for processing state
        loader.style.display = 'block';
        statusText.textContent = 'Processing video... This may take a few moments.';
        submitButton.disabled = true;
        resultsCard.style.display = 'none';

        // Send file to backend
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            
            statusText.textContent = 'Processing complete!';
            resultsCard.style.display = 'block';
            processedVideo.src = data.processed_video_url; // Flask serves the static file
            processedVideo.load();
        })
        .catch(error => {
            statusText.textContent = `Error: ${error.message}`;
            console.error('Error:', error);
        })
        .finally(() => {
            loader.style.display = 'none';
            submitButton.disabled = false;
        });
    });
});