{% include "header.html" %}

<section class="tagline">
    <div class="max">
        <h1>Hi, I am Novia!</h1>
        <h2>Researcher<br>UX Designer<br>90% Extrovert</h2>
    </div>
    <!--<div>
        <img src="{{ url_for('static', filename='logo-colored.png') }}" alt="Novia's logo">
    </div>-->
</section>
<br><br>

<hr class="max">

<div class="clear"></div>

<section id="projecthighlights">
    <div class="max">
        <h2>Projects</h2>
        <form action="{{ url_for('UX') }}" method="get"><button class="button-light">View All</button></form>
        <div id="allprojectcards">
        <div class="projectcard overlay col-5">
            <a href="{{ url_for('techsmith') }}">
                <img src="{{ url_for('static', filename='techsmith.png') }}" alt="Learn more about TechSmith internship.">
            </a>
            <p class="">UX design internship at TechSmith, where I worked on two different product teams as a UX designer. Experiences with user research, web-based dashboard design, and desktop application design.</p>
        </div>
        <div class="projectcard overlay col-5">
           <a href="{{ url_for('pianolink') }}">
            <img src="{{ url_for('static', filename='pianolink.png') }}" alt="Learn more about PianoLink project.">
           </a>
            <p>Researched problems adult college piano learners faced and ideated solutions for them. PianoLink is a portal device that piano learners could take with them as they practice outside of their homes.</p>
        </div>
        <div class="clear"></div>
        <div class="projectcard overlay col-5">
            <a href="{{ url_for('decision_aid') }}">
                <img src="{{ url_for('static', filename='Decision_Aid.png') }}" alt="Learn more about my project on redesigning a bariatric decision aid.">
            </a>
            <p>Consultant for a local health informatics company on user research and web-based decision aid design for bariatric surgery. Decision aid improves the current surgical outcomes calculator by including education and potential lifestyle changes for the users.</p>
        </div>
        <div class="projectcard overlay col-5">
            <a href="{{ url_for('thesis') }}">
                <img src="{{ url_for('static', filename='thesis.png') }}" alt="Learn more about my honor thesis.">
            </a>
            <p>A quantitative research project that looked at how users stored, managed, and created their passwords. Tested on password memorability and users' attitudes, along with habits toward their existing passwords.</p>
        </div>
        </div>
        <br class="clear"><br>
    </div>
</section>

<hr class="max">

<section id="experiences">
    <div class="max">
        <h2>Experiences</h2>
        <form action="{{ url_for('static', filename='Novia Wong_Resume.pdf') }}" method="get" target="_blank"><button class="button-light">Download Resume</button></form>
        <img src="{{ url_for('static', filename='Experiences.png') }}" alt="My undergraduate was at San Jose State University, where I earned a Bachelor of Science in Psychology, worked as a behavioral therapist, and served as a research assistant at a cyber security lab. I am currently going to the University of Michigan Ann Arbor, and I am part of the School of Information. There, I worked as a UX designer Intern, a graduate student instructor, and I focus on UX Research and Design as part of my Masters program.">
    </div>
</section>

<hr class="max">

<section id="aboutme" class="clear">
    <div class="max">
        <h2>About Me</h2>
        <br>
        <figure>
            <img id="profilepic" src="{{ url_for('static', filename='Novia_ref.png') }}" alt="Image of Novia">
        </figure>
        <br class="clear">
        <p>I am a second year master student at University of Michigan School of Information, studying user experience research and design. I also hold a Bachelor of Science in Psychology. <br><br>My passion is deeply rooted in psychology and advancing technology for the vulnerable population, such as children with special needs. Other interest areas include healthcare and education technology; through my work in teaching K-12 and college students, I have experienced first-handed the power of technology in an educational setting.<br><br>I believe good design is supported by compelling research data, and one way to get that data is through user research. Among the many different techniques, I particularly enjoy talking to and observing people. By doing these two things, I can learn a lot about people.<br><br>My strengths include empathy, communication, and mixed research methods in quantitative and qualitative methods. My time as a behavioral therapist has taught me the importance of empathy, especially since i was working with children who could not advocate for themselves effectively. I have also worked in multiple leadership positions, and have increased the organization size, productivity, and the level of positive attitudes toward events hosted by the organizations.<br><br>Outside of school and work, I also enjoy: playing the piano, baking, volunteering, and making comic strips. I also love making new friends and learning something new everyday!</p>
    </div>
</section>


{% include "footer.html" %}
