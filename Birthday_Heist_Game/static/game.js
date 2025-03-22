let score = 0;
const balloonContainer = document.getElementById('balloon-container');
const scoreDisplay = document.getElementById('score');

function createBalloon() {
    const balloon = document.createElement('div');
    balloon.classList.add('balloon');
    balloon.style.left = `${Math.random() * (balloonContainer.clientWidth - 50)}px`;
    balloonContainer.appendChild(balloon);

    let position = 0;
    const speed = Math.random() * 2 + 1;

    function moveBalloon() {
        if (position > balloonContainer.clientHeight) {
            balloon.remove();
        } else {
            position += speed;
            balloon.style.bottom = `${position}px`;
            requestAnimationFrame(moveBalloon);
        }
    }

    balloon.addEventListener('click', () => {
        score++;
        scoreDisplay.textContent = `Score: ${score}`;
        balloon.remove();
    });

    moveBalloon();
}

setInterval(createBalloon, 1000);
