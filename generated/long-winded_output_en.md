# Kühn András Gábor
### Long-winded CV for a detailed overview

###### _See the rest on my GitHub page:_ _[http://github.com/kuhnandrasgabor/cv ](http://github.com/kuhnandrasgabor/cv)_
###### _Or chat with me / about my CV with my GPT chatbot:_ _[https://chatgpt.com/g/g-CwjQO2tT5-curriculum-virtuale](https://chatgpt.com/g/g-CwjQO2tT5-curriculum-virtuale)_


# Personal info

 * **Location:** [Szeged, Hungary](https://maps.app.goo.gl/HrTJQS68Pcr1mWZY9)

 * **Email:** [kuhnandrasgabor@gmail.com](mailto:kuhnandrasgabor@gmail.com)

 * **Social:** [LinkedIn](https://www.linkedin.com/in/andrew-k%C3%BChn-58251070/)

 * **Visuals:** [Gallery](https://drive.google.com/drive/u/1/folders/17BtC\_NqO1VWdKJ8OTOcvbAuNRcr1uOjr)

<img src="../images/profile.jpg" alt="profile_picture" width="200">


## Objectives & Aspirations

I seek a company where I can build a long-term career and where hard work and dedication are rewarded. My goal is to find a role that engages my interests, provides opportunities for growth, and allows me to contribute meaningfully to the company's success. I want to leverage my skills in a challenging environment that values autonomy, yet fosters collaboration with passionate professionals. Ideally, I envision a workplace where I **_want to be_**, whether working remotely or on-site by choice. I value a healthy work-life balance, flexibility, and the opportunity to take pride in my work.

* Long-term career in a field aligned with my passions
* Clear opportunities for growth and advancement
* Work-life balance with remote work or flexible hours
* Competitive compensation
* Involvement in meaningful and engaging projects
* Opportunities for continuous learning and professional development
* A balance of autonomy and collaborative teamwork

# Professional experience

I'm a professional with over a decade of diverse experience spanning various fields, ranging from **machine learning** and **web development** through **3D visualizations** to professional **photography**.

I have experience in leadership roles in **smaller teams**, including CEO of a tech startup, where I led a
complex multiplayer **online game development** project, and later as CTO of a startup doing **AI powered industrial data management** and SaaS solutions for aviation MROs and other heavy industries.

I have some experience in business negotiation and project management, but am my *very best* at **creative design and problem-solving**, where I can make the most of my wide spanning technical background I gathered throughout my work and hobbies. I am a very firm believer in the pareto principle, and try to equip myself with knowledge among various fields, while relying on specialits in matters where I am not an expert of.

Thanks to my english skills, I excel in multicultural environments.

Committed to **continuous learning and improvement**, with an eye for detail and a passion for technology and innovation, I try to use technology to improve all aspects of my personal and professional life, such as using AI tools when justified/appropriate.


- Over a decade of diverse professional experience spanning various fields:
  - **Machine learning**
  - **Web development**
  - **3D visualizations**
  - Professional **photography**
- Experience in leadership roles in **smaller teams**, including:
  - CEO of a tech startup, leading a complex multiplayer **online game development** project
  - CTO of a startup providing **AI-powered data management** and SaaS solutions for aviation and heavy industries
- Very best at **creative design and problem-solving**
- Excel in multicultural environments due to strong English skills
- Eye for detail and passion for technology and innovation


## 2020 – Present: Data Science, Machine Learning, Full-Stack Developer & Acting CTO at Pzartech Ltd.


I Initially joined as a freelance developer, wound up acting as CTO, overseeing all development and architecture decisions.

I was tasked with the **re-development** of a **data management software** prototype and subsequent deployment as an **SaaS solution** designed for aerospace MRO's and heavy industry.

During my tenure I was collaborating on strategic planning, technical decision-making, and future company growth, including equity stake for my contributions.

A few bigger milestones iclude an **SAP S4/HANA** integration prototype, **ElasticSearch** analytics prototype, **Azure storage** management with media services **video streaming** prototype, and the project's core value add: development and implementation of **visual search and OCR** solutions.


* Full-stack web development on .Net Core, Blazor, Razor, MongoDB, MAUI
* ML/AI development with Python
* Image classifier and OCR system training and deployment
* CI/CD with Azure DevOps, Azure Portal
* Version control with Git through Azure DevOps

### Web based data management software

The project was managed in **Azure DevOps** using a **CI/CD** pipeline implementation, hosted in Azure.
We decided on **.Net Core** with **Blazor Razor** pages, **MongoDB** for database and **MAUI** for Android and WebClient build targets.
The project was a complete rewrite of the existing software, with a focus on **modularity** and **scalability**, so we used 
a microservice architecture with a frontend server, core server, and various recognition module servers.

* SaaS software structure and design consultation for ERP software
* Azure cloud resource deployment and management
* Azure DevOps project management, CI/CD
* .Net Blazor Razor pages based project with MAUI multiplatform build targets
  * Azure bucket storage integration and management
  * API connections between
    * frontend server
    * core server
    * various recognition module servers
  * Image and Character recognition development and integration
  * Responsive UI with MudBlazor (although I'm not really a front-end developer)
  * ElasticSearch based page and usage analytics prototype
  * Media storage and streaming prototype with Azure media services
  * SAP integration prototype for SAP HANA S/4 Product Master Data

#### Skills used/developed
  * C#, Python, HTML
  * .Net Core, Blazor, Razor, MongoDB, MAUI
  * Azure DevOps, Azure Portal, CI/CD
  * Version control with Git through Azure DevOps

### Machine learning and training

I was tasked with improving the results and scope of the **image classifier network** we were using for **industrial part recognition**. The original idea proved to be too difficult to optimize in the long term, so with a little push from a consulting expert I began to train a new network from scratch, marking my foray into the world of machine learning.

Increasing the difficulty was the fact that the **data quality was sporadic**, **without** a realistic **chance to re-capture any video** footage, and several mislabellings both in the training and testing data, so I had to put a lot of effort into visualizing the performance of each training run to find out what the issues were.

Uncovering these errors in the datasets forced me to engineer various ways to detect and fix them, ultimately creating an **ingestion and processing toolchain** in python, utilizing several steps of **quality assurance** along the way, like custom neural networks trained to detect issues and mark files before handing them off to later processing steps.

The result was a model that proved capable in real-world tests and performed well above the expectations: 84% accuracy in single-image top-4 scenarios, and **perceptually 100% accuracy** as the system was upgraded to enable multi-image prediction.

Another task of mine was the prototyping of an **OCR software** solution, where we had to detect writing from stamped machine parts to hand-engraved dotmatrix serial numbers.

While this project never got out of the prototype phase, the solution I came up with, (along with the pre-processing, hyperparameters, and prospective fine-tuning method) resulted in our version mostly keeping up with, and in some more niche and difficult cases even surpassing industry standard solutions, such as Azure's AI Vision. The fine-tuning solution's prototype was also completed: a **synthetic data generation script** written from scratch for Blender, opening the gateway to fine-tune the model incredibly well for specific scenarios if needed.

* ML dataset generation
  * Raw video processing, segmentation, enhancement, evaluation for semi-synth data
  * Realistic generation of labeled synthetic images
  * Dataset management and tooling
* ML Training
  * Image quality assessment network for training data evaluation
  * Bounding box generation network for training data evaluation
  * Image classifier network for industrial part recognition
  * Optical character recognition system
* Integrating with existing SaaS architecture in Azure’s cloud
* Performance charting and analysis


#### Skills used/developed
  * C# for the API, but mostly Python for training and inference
  * FastAi, PyTorch, TensorFlow, Jupyter notebooks and Paperspace Gradient
  * Flask, seaborn, matplotlib, pandas, numpy
  * Docker, Docker-Compose

## 2011 – Present: Freelance Professional (Photography, 3D Graphics, Webdesign, Architectural Visualization)


I have over the years gathered experience across various industries from **photography**, and **programming** to real-estate **renovation**.

On the computer side of things I was part of a team tasked with building a multilanguage **checklist app for iOs**, and I had worked on a **Magento based online** furniture **store** mostly written in PHP.

On the visuals front, I worked on interactive, real-time **3D architectural visualization** projects using **Unreal Engine 4 and Blender** for both personal and client projects. 

I did **3D modeling and animation** work in Blender, and **branding, advertising, logo and web design** work in Adobe Creative Suite.

For personal projects and changing things up, I did some remodeling and renovation work, and also worked for quite some time as a freelance **photographer** just for fun and to keep my skills sharp.

* Designing and modeling houses and environments
* Creating 3D models and animations
* PHP3 and Magento-based online store
* Multilanguage checklist app for iOS
* Branding, advertising, logo and web design
* Freelance photography
* Remodeling and renovation work

#### *3D modelling and visual effects*

I had the opportunity to work on some 3D visualizations for interactive training material related to natural disasters.
I had to come up with ways to illustrate, then model and render various **natural disasters**, such as floods, earthquakes, wildfires and wildfires. 
To do this, I used **Blender's physics simulation** for **fluids**, and **smoke**, along with **rigidbody** **collisions**, and destruction. 
In order to meet tight deadlines, I had the **rendering** running on seven computers in the office **simultaneously** after baking the sims.

* visualizing and rendering various natural disasters
* distributed rendering locally on several machines
* physics simulation including fluids, smoke, collisions, and destruction


### [Go to 3D gallery](../sections/experience/freelance/3d/freelance-3d-gallery_en.md)

#### Interactive Architectural Visualization

A contractor friend of mine approached me with an offer to help him with a family house he was building soon. We decided to see if prototyping a realistic **interactive 3D walk around showcase** for the project was worth it. 

I was provided some CAD drawings and a floorplan on which I modeled the house in **Blender**, designed some **realistic PBR materials and textures**, and set up a scene in Unreal Engine 4. The result was a realistic interactive 3D walk around showcase of the house, that you can still try out [here](https://drive.google.com/file/d/18HLLP1rOycEmTNhTGDjkPf6v8MJuqwSk/view?usp=sharing) or just watch another one of these projects [on youtube](https://youtu.be/XRm1u-OF0CA). I even built custom model generators for kitchen cabinets and a solar gain based 3D plant-growth model in **Houdini**, just for giggles.


* Real-time interactive demo software using Unreal Engine 4
* Hybrid lighting, using both real-time reflections and switchable dynamic lights, with pre-baked lightmaps
* Realistic PBR materials and textures
* Custom model generators for kitchen cabinets and a sunlight based 3D plant-growth model in Houdini

### [Go to interactive gallery](../sections/experience/freelance/archviz-interactive/freelance-archviz-interactive-gallery_en.md)

#### Realistic Architectural Visualization

I had been designing and rendering my house for some time when an opportunity to do do some freelance work came up. I had a 1-day deadline to create 3D renderings to apply to a government grant for renovating a condo's yard. I took some photos of the sites, measured them and sketched it out in **Blender**, quickly made some materials and textures, and rendered it out in **Cycles**. The result was a realistic rendering of the yard. The grant was won, and the yard was renovated for two different buildings.

* Realistic rendering
* Solar gain analysis 
* Quick and dirty mockup from on-site photos and measurements


### [Go to realistic gallery](../sections/experience/freelance/archviz-realistic/freelance-archviz-realistic-gallery_en.md)

## 2014\. – 2020\. Stoneglass Labs KFT., Szeged (CEO)


Headed a software development team in a small company developing an ambitious online multiplayer game.

* Corporate administration
* Project management
* Business negotiation
* Software and hardware acquisition
* Network and sysadmin tasks
* Administrative tasks

### *Stars End (MMORPG game software project)*



Led development and design of an ambitious **multiplayer online game** involving large-scale, space-themed gameplay. I handled virtually all aspects of **game logic, engine customization (Unity 3D and Unreal Engine 4) from AI logic to shader programming**. Built over 300 custom **icons, volumetric effects, and modular 3D spaceship models, UI elements** and a myriad of tools. The project required self-learning of various skills from writing the background lore to refining of business models for monetization, a creation pipeline for assets, including all **graphics both 2D and 3D, procedural geometry generation logic, VFX and sound design**.

* Creative lead design
* Software design and development
  * Engine customization
    * Unity 3D
    * Unreal Engine 4
  * Architecture
  * Network communication
  * Data security
  * Scalability
* Gamedesign
  * Graphics design
    * Brand
    * 2D, 3D assets
    * UI/UX
    * VFX, shaders
    * AI, FSM
  * Sound and music
  * Level design
  * Story, missions and background info
* Development of content generation tools and additional software

### [Go to starsend gallery](../sections/experience/starsend/starsend-gallery_en.md)

<!-- PAGEBREAK -->

# Relevant Projects

## Homing Szeged - Real Estate Agency (2017 – Present)

* Developed the brand identity and all marketing materials for a family-owned real estate business.
* Created a logo reflecting the city of Szeged and its landmarks while incorporating visual elements like keys and target reticles.
* Designed a user-friendly website with a dark theme, matching modern UI trends, and integrated a QR code system into business cards for ease of contact.
* Managed various print materials, forms, and signage to align with the brand's design language.

## Star’s End - MMORPG (2013 – 2020)

* Led development and design of an ambitious multiplayer online game involving large-scale, space-themed, team-based gameplay.
* Handled all aspects of game logic, engine customization (Unity 3D and Unreal Engine 4), AI design, and shader programming.
* Built over 300 custom icons, volumetric effects, and modular 3D spaceship models.
* Project required self-learning of game mechanics, business modeling, and pipeline creation, including procedural geometry generation and VFX design.


## Real Time ArchViz with Unreal Engine 4 (2020)

* Developed a real-time 3D architectural visualization for a contractor using Unreal Engine 4.
* Modeled in Sketchup, textured in Blender and Substance Painter, baked lightmaps, and implemented navigation via Blueprints.
* Created a realistic, interactive demo of the house with high hardware requirements, demonstrating photorealism within engine constraints.
* Delivered a downloadable, high-quality, executable version with real-time lighting and walk-through controls (WASD + mouse).+
* Download the demo: [Download Executable](https://drive.google.com/file/d/18HLLP1rOycEmTNhTGDjkPf6v8MJuqwSk/view?usp=sharing)

## Waterfront House - Personal Project (2019)

* Designed and modeled a concept house in Sketchup, later refined and rendered photorealistically in Blender.
* Applied procedural materials and HDRI lighting for realistic exterior and interior scenes.
* Integrated custom foliage and architectural assets to produce a detailed, lifelike render of the house concept.

# Studies
* **Business Coaching** *(2013 – 2014\)*
  Basic business workflow and management training through Támop 2.3.6 grant.
* **Tripont Light Academy 1-2-3** *(2011 – 2013\)*
  Comprehensive training in lighting techniques, various photography disciplines, and project management.
* **SZTE JGYPK, Web Programmer Certificate** *(2010 – 2011, Incomplete)*
  Gained foundational skills in web development, including HTML, Java, SQL, and graphic design. Lost interest and
  shifted to photography and entrepreneurship.
* **SZTE TTIK, Computer Engineering BSc.** *(2008 – 2010, Incomplete)*
  Attended courses in programming (C, Assembly), computer architecture, discrete mathematics, and algorithms. Did not
  complete the degree, switched career focus.

<!-- PAGEBREAK -->

# Skills and competencies

## Technical Skills

### Programming Languages
  * **Experienced:** C#, Python
  * **Proficient:** C++, HTML, CSS, SQL, PHP
  * **Familiar:** Java, JavaScript, TypeScript, C, Google Script, assembly

### Frameworks and Technologies
  * **Web Development Frameworks:**
    * **Experienced:** .NET Core, Blazor, Razor, MAUI, MudBlazor
    * **Proficient:** Angular
    * **Familiar:** Flask

  * **Machine Learning Frameworks and Tools:**
    * **Familiar:** FastAI, PyTorch, TensorFlow, Scikit, Jupyter Notebooks, Paperspace Gradient

  * **DevOps and Containerization:**
    * **Experienced:** Azure DevOps
    * **Proficient:** CI/CD pipeline implementation
    * **Familiar:** Docker, Docker Compose

  * **Data Analysis and Visualization:**
    * **Familiar:** Pandas, NumPy, Matplotlib, Seaborn

### Databases and Data Management

* **Proficient:** MongoDB, SQL databases (e.g., MySQL, SQL Server)
* **Familiar:** ElasticSearch

### Cloud Services and DevOps

* **Experienced:** Azure DevOps, Portal, Storage, App services and VMs
* **Proficient:** Azure Resource Management, CI/CD pipeline implementation
* **Familiar:** Docker, Docker Compose, Azure Media Services

### Software and Tools

* **Version Control:**
  * **Experienced:** with Git (Azure DevOps, GitHub)
  * **Familiar:** with SVN

* **3D Graphics and Modeling:**
  * **Experienced:** Blender 3D, Unreal Engine 4, Unity 3D
  * **Proficient:** Substance Painter, Substance Designer, SketchUp, V*Ray
  * **Familiar:** Houdini, SolidWorks CAD, ArchiCAD, CATIA, Fusion 360

* **Adobe Creative Suite:**
  * Experienced with Adobe Photoshop and Adobe Lightroom

### Creative Design and Game Development

* 2D/3D asset creation, vector graphics, modeling, texturing, lighting, and rendering
* UI/UX design for web and applications
* Visual storytelling and game design
* VFX, shaders, and procedural/parametric modeling
* Experience with game development and engine customization in Unity 3D and Unreal Engine 4
* Animation and physics simulation


## Professional Skills:

* **Project Management:**
  Experience managing projects from conception to completion, including software development, marketing campaigns, and
  creative projects. Familiar with Agile methodologies and Azure DevOps for CI/CD pipeline management.
* **Business and Negotiation:**
  Experience in business negotiation, client management, and corporate administration. Skilled in developing and
  executing strategic business plans.
* **Creative and Design Skills:**
  Strong background in creative design, including 2D/3D asset creation, UI/UX design, and visual storytelling for gaming
  and simulation. Experienced in VFX, shaders, and procedural/parametric modeling.

## Soft Skills:

* **Leadership:**
Experience in managing smaller cross-functional teams in mostly startup environments. Capable of mediating
  conflicts and fostering a collaborative workplace.
* **Communication:**
  Fluent in English (C2) and beginner in German (A1). Skilled in clear and effective communication with both technical and non-technical stakeholders.
* **Problem-Solving and Adaptability:**
  Strong analytical skills with a demonstrated ability to solve complex problems and adapt to new challenges.
  Comfortable learning new technologies and tools independently.

# Interests

## Creation

Creating and altering things has grown to be a fundamental part of my life. Whether it's a piece of software, a 3D model, furniture, or a photo, I have enjoyed the process of creation and the satisfaction of seeing the results of my work since early childhood.

## Creativity and Design

A strong passion for creativity, from legos to VR to simulation and design, this passion fuels my interest in software development and design.

## Mechanics and Electronics

What started out as hobby R/C models has kept up with me throughout my life, as I have built (and repaired) various electronic devices. This hands-on experience of taking things apart, understanding how they work, and putting them back together enhances my understanding of hardware-software integration.

## Technology and Futurism

I am deeply interested in emerging technologies and their potential impacts on society, such as AI, quantum computing, and space exploration. This forward-thinking mindset gives me perspective when I approach my software development and data science endeavours.

## Nature, Elements, Exploration

Since as long as I can remember, I have always enjoyed water and am a certified scuba diver. For most of my adult life, I have been a rock climber and outdoor enthusiast. Lately I picked up paragliding, adding an additional element to my interests. In my life, I seem to gravitate towards activities that reward me with a sense of exploration and connection to the natural world, while demanding personal responsibility and self-reliance.



