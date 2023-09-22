# DS5111_FALL2023_SW2_Lab
1.   In the env command, I created the virtual environment then pip installed the packages in the requirements.txt file. In the run command, in order to suppress the echo of the command, I added "@" at the beginning of the line. Then I basically just had to indicate where exactly the clockdeco_param.py file was in order for it to be executed.
2.   I had resolved the python3 -m venv env error message previously on this instance, so this particular command didn't throw an error for me. I don't remember how exactly I resolved this before, but I did rely on the error message plus stack overflow to overcome the error.
3.   I don't quite know the answer to this, and now I'm worried my run command in the makefile is incorrect. But my code passes the test.
4.   I would make run a .PHONY command so that it runs regardless of a name collision.
5.   The first line imports the python package "sys". It seems like the second line just appends "." to the path.
   
EXTRA CREDIT
1. tree -I *env
2. The **/ indicates to ignore files with the pattern *__pycache__ across ALL directories.
3. I used the command: pip freeze | grep -i pytest >> requirements.txt in order to populate the requirements file with the versions for both pytest and pylint.
