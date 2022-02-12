# X-Men
X-Men: A Mutation-Based Approach for the Formal Analysis of Security Ceremonies

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

  There is an increasing number of cyber-systems (e.g., systems for payment, transportation, voting, critical infrastructures) whose security depends intrinsically on human users. 
  A security ceremony expands a security protocol with everything that is considered out-of-band to it, including, in particular, the mistakes that human users might make when participating actively in the security ceremony. 
  <!--In this paper, we introduce a novel approach for the formal and automated analysis of security ceremonies. -->
  Our approach defines mutation rules that model possible behaviors of a human user, and automatically generates mutations in the behavior of the other agents of the ceremony to match the human-induced mutations. 
  This allows for the analysis of the original ceremony specification and its possible mutations, which may include the way in which the ceremony has actually been implemented. 
  To automate our approach, we have developed the tool X-Men, which is a prototype that extends Tamarin, one of the most common tools for the automatic unbounded verification of security protocols. 
  As a proof of concept, we have <!--%defined four mutations that formalize possible human behaviors and--> applied our approach to three real-life case studies, uncovering a number of concrete vulnerabilities.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This section list any major frameworks/libraries used to bootstrap the project. 

* [Python](https://www.python.org)
* [ANTLR](https://www.antlr.org)
* [Java](https://www.java.com/en/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is how you can set up the project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Java 13 or greater
  ```url
  https://www.oracle.com/java/technologies/javase/jdk13-archive-downloads.html
  ```
  
 * Python 3.9.10
    ```url
    https://www.python.org/downloads/release/python-3910/
    ```
    
    Python is using the following modules:
    
    * os
    * fileinput
    * ntpath
    * subprocess
    * sys
    * glob
    * shutil
    * csv
    * tqdm
    * argparse
    
* Tamarin
    ```url
    https://tamarin-prover.github.io/manual/book/002_installation.html
    ```
    
    <p align="right">(<a href="#top">back to top</a>)</p>

### Installation

Please follow the instruction below on how to run the X-Men tool:

1. Be sure that Java, Python and Tamarin are correctly installed on your machine.
2. Download the project folder on your machine.
3. Open a terminal and go to the folder which cointains the wolverine.py file
4. Execute wolverine.py using:
   ```sh
   python3 wolverine.py
   ```
4. Select one of the models you can find in the Models folder. You can choose between:
   * Oyster.spthy
   * SSO.spthy
   * CoachService.spthy
   
   The python script splits the model in three files: (filename_pre.spthy, filename.spthy and filename_post.spthy)
   
5. X-Men opens.
6. Click on "Click here to upload a model" icon and select the filename.spthy file just created by wolverine (do not consider filename_pre.spthy nor filename_post.spthy).
7. Once the model is uploaded, go in the option tab in X-Men which now is enabled.
8. Select the mutation you want to apply.
9. Go back to the previous tab and click on the icon to generate the mutated models.
10. Click on the closure button on top of X-Men to close the tool.
11. Wolverine resumes the work merging the previous splitted file with the mutated models.
12. Wolverine executes Tamarin for each of the mutated model generating a file report.csv which contains the mutated models which security properties are now falsified.

<p align="right">(<a href="#top">back to top</a>)</p>


