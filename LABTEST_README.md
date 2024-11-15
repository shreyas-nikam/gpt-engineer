# Test 1

1. Launched gpt-engineer on github codespaces
2. Installed requirements by running: `poetry install`
3. Activated the environment by running `poetry shell`
4. Created a new project `portfolio-return-atrribution` and added the business requirements from https://docs.google.com/document/d/1qdPDZ9me3r90rh2hMzsQFl2CxyD721hhRH1VQklFhkg/edit?usp=sharing in the prompt
5. Ran `gpte projects/portfolio-return-attribution`
6. Said `y` to run the commands.
7. Failed. Nothing happened.
8. Manually navigated to the project folder (`cd projects/portfolio-return-attribution`) and launched the streamlit application by running `streamlit run main.py`
9. Fixed errors which were related to the relative imports and another error related to a value being treated as a variable while plotting.
10. Launched the streamlit applicaton after fixing errors.
