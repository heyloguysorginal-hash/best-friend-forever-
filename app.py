from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For My Best Friend 💗</title>

<style>
    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        min-height: 100vh;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;

        background:
            repeating-linear-gradient(
                90deg,
                #d94b70 0px,
                #d94b70 3px,
                #cf4168 3px,
                #cf4168 7px
            );

        font-family: "Comic Sans MS", "Segoe Print", cursive;
    }

    /* Little decorative circles */
    .dot {
        position: fixed;
        width: 12px;
        height: 12px;
        background: #ffd7e1;
        border-radius: 50%;
        opacity: .7;
    }

    .d1 { top: 12%; left: 10%; }
    .d2 { top: 25%; right: 8%; }
    .d3 { bottom: 15%; left: 13%; }
    .d4 { bottom: 10%; right: 15%; }

    /* Main paper */
    .paper {
        position: relative;
        width: min(88vw, 1000px);
        height: min(78vh, 650px);

        padding: 70px 80px;

        background:
            linear-gradient(
                rgba(255,255,255,.94),
                rgba(255,255,255,.94)
            ),
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 31px,
                rgba(150,190,190,.18) 32px
            );

        /* Notebook grid */
        background-image:
            linear-gradient(rgba(100,170,170,.12) 1px, transparent 1px),
            linear-gradient(90deg, rgba(100,170,170,.12) 1px, transparent 1px);

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

        box-shadow: 0 20px 50px rgba(60,0,20,.35);

        display: flex;
        justify-content: center;
        align-items: center;

        transition:
            opacity .7s ease,
            transform .7s ease;
    }

    .content {
        width: 85%;
        text-align: center;
        color: #57313d;
    }

    .tiny {
        font-size: 20px;
        color: #c45b78;
        margin-bottom: 18px;
    }

    h1 {
        font-size: clamp(32px, 5vw, 58px);
        line-height: 1.15;
        color: #793c50;
        margin: 0 auto 22px;
        transform: rotate(-1deg);
    }

    .subtitle {
        font-size: clamp(17px, 2vw, 23px);
        color: #986070;
        margin-bottom: 42px;
    }

    .question-mark {
        display: inline-block;
        animation: wiggle 1.5s infinite;
    }

    .buttons {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 35px;
    }

    button {
        border: 0;
        font-family: inherit;
        font-size: 22px;
        padding: 15px 40px;
        border-radius: 50px;
        cursor: pointer;
        transition: transform .2s ease;
    }

    #yes {
        color: white;
        background: #e85b82;
        box-shadow: 0 8px 18px rgba(180,50,90,.25);
    }

    #yes:hover {
        transform: scale(1.1) rotate(-2deg);
    }

    #no {
        color: #784c59;
        background: #f2d9df;
        position: relative;
    }

    /* Cute doodles */
    .doodle {
        position: absolute;
        font-size: 35px;
        user-select: none;
        pointer-events: none;
    }

    .flower {
        top: 18%;
        left: 13%;
        transform: rotate(-15deg);
    }

    .heart-doodle {
        bottom: 17%;
        right: 13%;
        transform: rotate(12deg);
    }

    .star {
        top: 16%;
        right: 16%;
    }

    .smile {
        bottom: 16%;
        left: 15%;
    }

    /* Final scene */
    #finalScene {
        display: none;
        position: fixed;
        inset: 0;
        z-index: 100;
        justify-content: center;
        align-items: center;
        text-align: center;

        background:
            repeating-linear-gradient(
                90deg,
                #d94b70 0px,
                #d94b70 3px,
                #cf4168 3px,
                #cf4168 7px
            );
    }

    .final-paper {
        width: min(85vw, 900px);
        padding: 100px 40px;

        background:
            linear-gradient(rgba(255,255,255,.96), rgba(255,255,255,.96)),
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 31px,
                rgba(100,170,170,.15) 32px
            );

        background-size: 32px 32px;

        border-radius: 35% 20% 30% 15% / 20% 35% 15% 30%;

        box-shadow: 0 20px 60px rgba(60,0,20,.35);

        animation: finalAppear 1s ease forwards;
    }

    .final-paper h2 {
        color: #793c50;
        font-size: clamp(35px, 6vw, 70px);
        margin: 0;
    }

    .final-paper p {
        font-size: 22px;
        color: #a25b72;
        margin-top: 20px;
    }

    /* Hearts */
    .heart {
        position: fixed;
        bottom: -60px;
        z-index: 200;
        pointer-events: none;
        animation: floatUp linear forwards;
    }

    /* Confetti */
    .confetti {
        position: fixed;
        top: -30px;
        width: 9px;
        height: 17px;
        z-index: 150;
        pointer-events: none;
        animation: fall linear forwards;
    }

    .popper {
        position: fixed;
        font-size: 65px;
        z-index: 250;
        pointer-events: none;
        animation: popper .9s ease-out forwards;
    }

    @keyframes wiggle {
        0%,100% { transform: rotate(0deg); }
        50% { transform: rotate(10deg); }
    }

    @keyframes floatUp {
        from {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }

        to {
            transform: translateY(-115vh) rotate(360deg);
            opacity: 0;
        }
    }

    @keyframes fall {
        from {
            transform: translateY(0) rotate(0);
        }

        to {
            transform: translateY(110vh) rotate(720deg);
        }
    }

    @keyframes popper {
        0% {
            transform: scale(0) rotate(-20deg);
            opacity: 0;
        }

        40% {
            transform: scale(1.5) rotate(10deg);
            opacity: 1;
        }

        100% {
            transform: scale(1);
            opacity: 0;
        }
    }

    @keyframes finalAppear {
        from {
            opacity: 0;
            transform: scale(.7) rotate(-3deg);
        }

        to {
            opacity: 1;
            transform: scale(1) rotate(0);
        }
    }

    @media(max-width:600px) {
        .paper {
            width: 94vw;
            height: 75vh;
            padding: 40px 20px;
        }

        .content {
            width: 90%;
        }

        .buttons {
            gap: 15px;
        }

        button {
            padding: 12px 25px;
            font-size: 18px;
        }

        .doodle {
            font-size: 25px;
        }
    }
</style>
</head>

<body>

<div class="dot d1"></div>
<div class="dot d2"></div>
<div class="dot d3"></div>
<div class="dot d4"></div>

<div class="paper" id="paper">

    <div class="doodle flower">🌸</div>
    <div class="doodle heart-doodle">💗</div>
    <div class="doodle star">✦</div>
    <div class="doodle smile">☻</div>

    <div class="content">

        <div class="tiny">a very important question...</div>

        <h1>
            Will you be my<br>
            best friend forever?
            <span class="question-mark">💭</span>
        </h1>

        <div class="subtitle">
            Choose wisely... 👀
        </div>

        <div class="buttons">
            <button id="yes" onclick="sayYes()">
                Yes 💗
            </button>

            <button id="no">
                No 😭
            </button>
        </div>

    </div>
</div>


<div id="finalScene">

    <div class="final-paper">
        <h2>Thanks for choosing me 🥹✨</h2>
        <p>Best friends forever it is 💗</p>
    </div>

</div>


<script>

const noButton = document.getElementById("no");


/* Make NO escape */
function escapeNo() {

    const padding = 20;

    const maxX =
        window.innerWidth -
        noButton.offsetWidth -
        padding;

    const maxY =
        window.innerHeight -
        noButton.offsetHeight -
        padding;

    const x =
        padding +
        Math.random() * Math.max(1, maxX - padding);

    const y =
        padding +
        Math.random() * Math.max(1, maxY - padding);

    noButton.style.position = "fixed";
    noButton.style.left = x + "px";
    noButton.style.top = y + "px";

    noButton.style.transform =
        `rotate(${Math.random() * 25 - 12}deg)`;
}


/* Desktop */
noButton.addEventListener("mouseenter", escapeNo);


/* Mobile */
noButton.addEventListener("touchstart", function(event) {
    event.preventDefault();
    escapeNo();
});


/* If they somehow click it */
noButton.addEventListener("click", function(event) {
    event.preventDefault();
    escapeNo();
});


/* YES */
function sayYes() {

    const paper = document.getElementById("paper");

    paper.style.opacity = "0";
    paper.style.transform = "scale(.7) rotate(4deg)";

    /* Party poppers */
    createPopper("🎉", 8);
    createPopper("🎊", 88);

    /* Hearts */
    for (let i = 0; i < 45; i++) {
        setTimeout(createHeart, i * 45);
    }

    /* Confetti */
    for (let i = 0; i < 120; i++) {
        setTimeout(createConfetti, i * 10);
    }

    /* Show final scene */
    setTimeout(() => {
        document.getElementById("finalScene").style.display = "flex";
    }, 900);
}


function createHeart() {

    const heart = document.createElement("div");

    const choices = [
        "💗",
        "💖",
        "💕",
        "💓",
        "💞",
        "❤️",
        "✨"
    ];

    heart.className = "heart";

    heart.innerHTML =
        choices[Math.floor(Math.random() * choices.length)];

    heart.style.left =
        Math.random() * 100 + "vw";

    heart.style.fontSize =
        20 + Math.random() * 40 + "px";

    heart.style.animationDuration =
        2 + Math.random() * 3 + "s";

    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 5500);
}


function createConfetti() {

    const confetti = document.createElement("div");

    confetti.className = "confetti";

    confetti.style.left =
        Math.random() * 100 + "vw";

    confetti.style.background =
        `hsl(${Math.random() * 360}, 80%, 70%)`;

    confetti.style.animationDuration =
        2 + Math.random() * 3 + "s";

    document.body.appendChild(confetti);

    setTimeout(() => confetti.remove(), 5500);
}


function createPopper(symbol, side) {

    const popper = document.createElement("div");

    popper.className = "popper";

    popper.innerHTML = symbol;

    popper.style.left = side + "%";
    popper.style.top = "40%";

    document.body.appendChild(popper);

    setTimeout(() => popper.remove(), 1000);
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