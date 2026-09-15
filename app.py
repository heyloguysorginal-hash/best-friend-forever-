from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For My Best Friend 💖</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    font-family: "Comic Sans MS", "Segoe Print", cursive;
    background: #d94b70;
}

/* =========================================================
   GENERAL SCENES
========================================================= */

.scene {
    position: fixed;
    inset: 0;
    display: none;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.scene.active {
    display: flex;
}


/* =========================================================
   CUTE BACKGROUND
========================================================= */

.cute-bg {
    background:
        repeating-linear-gradient(
            90deg,
            #d94b70 0px,
            #d94b70 3px,
            #cf4168 3px,
            #cf4168 7px
        );
}


/* =========================================================
   PAPER
========================================================= */

.paper {
    position: relative;

    width: min(88vw, 1000px);
    height: min(78vh, 650px);

    padding: 70px;

    background-color: #fffdf7;

    background-image:
        linear-gradient(
            rgba(100, 170, 170, 0.13) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(100, 170, 170, 0.13) 1px,
            transparent 1px
        );

    background-size: 32px 32px;

    clip-path: polygon(
        5% 4%,
        15% 1%,
        27% 3%,
        39% 1%,
        52% 4%,
        66% 1%,
        80% 5%,
        94% 2%,
        98% 15%,
        96% 28%,
        99% 43%,
        96% 58%,
        99% 75%,
        94% 96%,
        80% 93%,
        65% 97%,
        49% 94%,
        35% 98%,
        20% 94%,
        6% 98%,
        3% 83%,
        5% 68%,
        2% 53%,
        5% 38%,
        2% 22%
    );

    box-shadow: 0 25px 60px rgba(50, 0, 20, .35);

    display: flex;
    justify-content: center;
    align-items: center;
}

.content {
    width: 85%;
}

.small-text {
    color: #c45b78;
    font-size: 20px;
    margin-bottom: 15px;
}

h1 {
    color: #743b4d;
    font-size: clamp(30px, 5vw, 58px);
    line-height: 1.2;
    margin: 0 auto 20px;
}

.subtitle {
    color: #9a6172;
    font-size: 20px;
    margin-bottom: 40px;
}


/* =========================================================
   BUTTONS
========================================================= */

.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px;
}

button {
    border: none;
    padding: 14px 35px;
    border-radius: 50px;
    font-family: inherit;
    font-size: 20px;
    cursor: pointer;
    transition: transform .2s ease;
}

.yes-btn {
    background: #e85b82;
    color: white;
    box-shadow: 0 8px 20px rgba(180, 50, 90, .25);
}

.yes-btn:hover {
    transform: scale(1.08);
}

.no-btn {
    background: #f0d9df;
    color: #754a57;
}


/* =========================================================
   DOODLES
========================================================= */

.doodle {
    position: absolute;
    font-size: 35px;
    pointer-events: none;
}

.d1 {
    top: 17%;
    left: 12%;
}

.d2 {
    top: 16%;
    right: 15%;
}

.d3 {
    bottom: 15%;
    left: 14%;
}

.d4 {
    bottom: 15%;
    right: 14%;
}


/* =========================================================
   HEART TRANSITION
========================================================= */

.heart {
    position: fixed;
    bottom: -70px;
    z-index: 999;
    pointer-events: none;
    animation: heartUp linear forwards;
}

@keyframes heartUp {

    from {
        transform:
            translateY(0)
            rotate(0deg)
            scale(.7);
        opacity: 1;
    }

    to {
        transform:
            translateY(-115vh)
            rotate(360deg)
            scale(1.3);
        opacity: 0;
    }
}


/* =========================================================
   SAD SCENES
========================================================= */

.sad-bg {
    background:
        radial-gradient(
            circle at center,
            #454545,
            #1e1e1e 70%,
            #050505
        );

    color: white;
}

.sad-paper {
    width: min(85vw, 850px);
    padding: 80px 45px;

    background: rgba(25,25,25,.88);

    border: 1px solid #555;

    box-shadow:
        0 25px 70px rgba(0,0,0,.7);

    border-radius: 18px;

    animation: sadAppear .8s ease;
}

.sad-paper h2 {
    color: #e4e4e4;
    font-size: clamp(30px, 5vw, 55px);
    margin: 0 0 20px;
}

.sad-paper p {
    color: #aaa;
    font-size: 19px;
    margin-bottom: 40px;
}

.sad-buttons {
    display: flex;
    justify-content: center;
    gap: 25px;
}

.sad-buttons button {
    background: #d5d5d5;
    color: #202020;
}

.sad-buttons button:hover {
    transform: scale(1.07);
}

@keyframes sadAppear {

    from {
        opacity: 0;
        transform: scale(.85);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}


/* =========================================================
   RAIN
========================================================= */

.rain {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
    z-index: 10;
}

.raindrop {
    position: absolute;
    top: -30px;

    width: 1px;
    height: 80px;

    background: rgba(210,210,210,.35);

    transform: rotate(12deg);

    animation: rainFall linear infinite;
}

@keyframes rainFall {

    from {
        transform:
            translateY(-100px)
            rotate(12deg);
    }

    to {
        transform:
            translateY(110vh)
            rotate(12deg);
    }
}


/* =========================================================
   FINAL MESSAGE
========================================================= */

.final-message {
    position: relative;
    z-index: 20;

    width: min(88vw, 950px);

    padding: 65px 45px;

    color: #d8d8d8;

    animation: finalAppear 1.2s ease;
}

.final-message h2 {
    font-size: clamp(25px, 4vw, 45px);
    line-height: 1.35;
    font-weight: normal;
}

@keyframes finalAppear {

    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* =========================================================
   MOVING YES
========================================================= */

#movingYes {
    position: fixed;
    z-index: 100;
}


/* =========================================================
   MOBILE
========================================================= */

@media(max-width:600px) {

    .paper {
        width: 94vw;
        height: 76vh;
        padding: 40px 15px;
    }

    .content {
        width: 92%;
    }

    .buttons,
    .sad-buttons {
        gap: 12px;
    }

    button {
        padding: 12px 24px;
        font-size: 18px;
    }

    .doodle {
        font-size: 25px;
    }

    .sad-paper {
        padding: 60px 20px;
    }
}

</style>
</head>


<body>


<!-- =====================================================
     SCENE 1
===================================================== -->

<div id="scene1" class="scene active cute-bg">

    <div class="paper">

        <div class="doodle d1">🌸</div>
        <div class="doodle d2">✦</div>
        <div class="doodle d3">♡</div>
        <div class="doodle d4">🎀</div>

        <div class="content">

            <div class="small-text">
                Chal Buddhi Bata 😭
            </div>

            <h1>
                Will you be my<br>
                best friend forever? 💖🥹
            </h1>

            <div class="subtitle">
                Choose wisely... 👀
            </div>

            <div class="buttons">

                <button
                    class="yes-btn"
                    onclick="firstYes()">
                    Yes 💖
                </button>

                <button
                    class="no-btn"
                    onclick="firstNo()">
                    No 😭
                </button>

            </div>

        </div>

    </div>

</div>


<!-- =====================================================
     SCENE 2
===================================================== -->

<div id="scene2" class="scene sad-bg">

    <div class="sad-paper">

        <h2>
            So i'm not your best friend 😞?
        </h2>

        <p>
            Really? After everything? 😭
        </p>

        <div class="sad-buttons">

            <button onclick="secondNo()">
                No 😭
            </button>

            <button onclick="secondYes()">
                Yes 💗
            </button>

        </div>

    </div>

</div>


<!-- =====================================================
     SCENE 3
===================================================== -->

<div id="scene3" class="scene cute-bg">

    <div class="paper">

        <div class="doodle d1">💗</div>
        <div class="doodle d2">✨</div>
        <div class="doodle d3">🌷</div>
        <div class="doodle d4">💖</div>

        <div class="content">

            <h1>
                Thanks for choosing me as your
                best friend Priyanjali 🥹✨
            </h1>

            <p class="subtitle">
                Okay... now I have something to tell you.
            </p>

        </div>

    </div>

</div>


<!-- =====================================================
     SCENE 4
===================================================== -->

<div id="scene4" class="scene sad-bg">

    <div class="sad-paper">

        <h2>
            RICHAAAA you sure?
        </h2>

        <p>
            You can still change your mind... 👀
        </p>

        <div class="sad-buttons">

            <button id="movingYes">
                Yes 💗
            </button>

            <button onclick="finalNo()">
                No 😭
            </button>

        </div>

    </div>

</div>


<!-- =====================================================
     SCENE 5
===================================================== -->

<div id="scene5" class="scene sad-bg">

    <div class="rain" id="rain"></div>

    <div class="final-message">

        <h2>
            so you hate me ? well that's sad :(
        </h2>

    </div>

</div>


<script>


/* =========================================================
   SCENE SWITCHER
========================================================= */

function showScene(id) {

    document
        .querySelectorAll(".scene")
        .forEach(scene => {
            scene.classList.remove("active");
        });

    document
        .getElementById(id)
        .classList.add("active");
}


/* =========================================================
   HEART TRANSITION
========================================================= */

function heartTransition(callback) {

    const hearts = [
        "💗",
        "💖",
        "💕",
        "💓",
        "💞",
        "❤️",
        "✨"
    ];

    for (let i = 0; i < 55; i++) {

        setTimeout(() => {

            const heart =
                document.createElement("div");

            heart.className = "heart";

            heart.innerHTML =
                hearts[
                    Math.floor(
                        Math.random() *
                        hearts.length
                    )
                ];

            heart.style.left =
                Math.random() * 100 + "vw";

            heart.style.fontSize =
                20 +
                Math.random() * 40 +
                "px";

            heart.style.animationDuration =
                2 +
                Math.random() * 2.5 +
                "s";

            document.body.appendChild(heart);

            setTimeout(
                () => heart.remove(),
                5000
            );

        }, i * 35);
    }

    setTimeout(callback, 900);
}


/* =========================================================
   FIRST YES
========================================================= */

function firstYes() {

    heartTransition(() => {

        showScene("scene3");

    });

    setTimeout(() => {

        const message =
            document.querySelector(
                "#scene3 .content"
            );

        message.innerHTML = `

            <h1>
                Thanks for choosing me as your
                best friend Priyanjali 🥹✨
            </h1>

            <p class="subtitle">

                You know when you first called me
                your best friend, i was like
                "why is this girl calling her best
                friend when i CLEARLY don't matter
                to her"

                <br><br>

                i doubted you that you were the
                "fake friend" who's definitely gonna
                use me for their own profit😭.

                <br><br>

                So thanks for choosing me yawr 💖✨✨

            </p>

        `;

    }, 2900);
}


/* =========================================================
   FIRST NO
========================================================= */

function firstNo() {

    showScene("scene2");

    startSadMusic();
}


/* =========================================================
   SECOND SCENE — YES
========================================================= */

function secondYes() {

    showScene("scene3");

    setTimeout(() => {

        const message =
            document.querySelector(
                "#scene3 .content"
            );

        message.innerHTML = `

            <h1>
                Thanks for choosing me as your
                best friend Priyanjali 🥹✨
            </h1>

            <p class="subtitle">

                You know when you first called me
                your best friend, i was like
                "why is this girl calling her best
                friend when i CLEARLY don't matter
                to her"

                <br><br>

                i doubted you that you were the
                "fake friend" who's definitely gonna
                use me for their own profit😭.

                <br><br>

                So thanks for choosing me yawr 💖✨✨

            </p>

        `;

    }, 2000);
}


/* =========================================================
   SECOND NO
========================================================= */

function secondNo() {

    showScene("scene4");

    setupMovingYes();
}


/* =========================================================
   MOVING YES — EXACTLY TWO MOVES
========================================================= */

function setupMovingYes() {

    const yes =
        document.getElementById("movingYes");

    let moveCount = 0;

    const maximumMoves = 2;


    function moveYes() {

        /*
         * Once it has moved twice,
         * STOP MOVING.
         */

        if (moveCount >= maximumMoves) {
            return;
        }

        moveCount++;


        /*
         * Keep the button completely
         * inside the visible browser.
         */

        const padding = 35;

        const buttonWidth =
            yes.offsetWidth;

        const buttonHeight =
            yes.offsetHeight;


        const maxX =
            window.innerWidth -
            buttonWidth -
            padding;

        const maxY =
            window.innerHeight -
            buttonHeight -
            padding;


        const x =
            padding +
            Math.random() *
            Math.max(
                1,
                maxX - padding
            );


        const y =
            padding +
            Math.random() *
            Math.max(
                1,
                maxY - padding
            );


        yes.style.left =
            x + "px";

        yes.style.top =
            y + "px";

        yes.style.transform =
            "scale(1.1)";


        setTimeout(() => {

            yes.style.transform =
                "scale(1)";

        }, 200);
    }


    /*
     * First touch / hover → move.
     */

    yes.addEventListener(
        "mouseenter",
        moveYes
    );


    yes.addEventListener(
        "touchstart",
        function(event) {

            /*
             * If it hasn't moved twice,
             * prevent the click and run away.
             */

            if (moveCount < maximumMoves) {

                event.preventDefault();

                moveYes();

            }

        }
    );


    /*
     * After TWO escapes, clicking YES
     * finally works.
     */

    yes.addEventListener(
        "click",
        function() {

            if (moveCount >= maximumMoves) {

                finalYes();

            }

        }
    );


    /*
     * Initial position.
     */

    yes.style.position = "fixed";

    yes.style.left = "50%";

    yes.style.top = "60%";

    yes.style.transform =
        "translate(-50%, -50%)";
}


/* =========================================================
   FINAL YES
========================================================= */

function finalYes() {

    showScene("scene5");

    createRain();

    const message =
        document.querySelector(
            "#scene5 .final-message"
        );

    message.innerHTML = `

        <h2>
            so you hate me ? well that's sad :(
        </h2>

    `;
}


/* =========================================================
   FINAL NO
========================================================= */

function finalNo() {

    showScene("scene5");

    createRain();

    const message =
        document.querySelector(
            "#scene5 .final-message"
        );

    message.innerHTML = `

        <h2>
            after this many rejection you
            finally chose no? 😭
        </h2>

    `;
}


/* =========================================================
   RAIN
========================================================= */

function createRain() {

    const rain =
        document.getElementById("rain");

    rain.innerHTML = "";

    for (
        let i = 0;
        i < 160;
        i++
    ) {

        const drop =
            document.createElement("div");

        drop.className =
            "raindrop";

        drop.style.left =
            Math.random() * 100 + "%";

        drop.style.animationDuration =
            .5 +
            Math.random() * .8 +
            "s";

        drop.style.animationDelay =
            Math.random() * 1.5 +
            "s";

        rain.appendChild(drop);
    }
}


/* =========================================================
   SAD MUSIC
========================================================= */

let audioContext;
let musicStarted = false;

function startSadMusic() {

    if (musicStarted) return;

    musicStarted = true;

    audioContext =
        new (
            window.AudioContext ||
            window.webkitAudioContext
        )();

    const notes = [
        196.00,
        174.61,
        164.81,
        146.83,
        164.81,
        174.61
    ];

    let index = 0;


    function playNote() {

        if (!audioContext) return;

        const oscillator =
            audioContext.createOscillator();

        const gain =
            audioContext.createGain();


        oscillator.type =
            "sine";

        oscillator.frequency.value =
            notes[index];


        gain.gain.setValueAtTime(
            0,
            audioContext.currentTime
        );


        gain.gain.linearRampToValueAtTime(
            0.045,
            audioContext.currentTime + .15
        );


        gain.gain.linearRampToValueAtTime(
            0,
            audioContext.currentTime + 1.4
        );


        oscillator.connect(gain);

        gain.connect(
            audioContext.destination
        );


        oscillator.start();

        oscillator.stop(
            audioContext.currentTime + 1.5
        );


        index =
            (index + 1) %
            notes.length;


        setTimeout(
            playNote,
            1200
        );
    }


    playNote();
}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)