Link to Learning: https://www.linkedin.com/learning/full-stack-deep-learning-with-python/introducing-mlops?autoSkip=true&resume=false&u=2101305<br>
Description: Brief intro to tools used for end to end machine learning in python. Taught by a AWS Data Engineer.

Course Notes:
MLOps
    - Used in the last two steps of Full Stack Machine Learning (Model Training --> Deploying, Testing, Maintaining)
    - Model Training WorkFlow (see image.png)
    - CI/CD includes both pipelines for data and code there fore if code or data changes, the model needs to update. 
      This can be automated.

MLFlow
    - Steamlines end to end of development, training, and deploying ML models
    - Components:
        - Tracking Runs
            - Experiments are logical containers for organizing each model run. 
        - Organize Model Artifacts
            - Each model is a directory with model files
            - MLmodel file defines the type of model and charcteristics
            - Env files 
        - Setup Projects
            - Standard way to package share and execute ml workflows (not covered in this course)
        - Model Registry
            - Centralized repo for managing models
            - Deploy multi versions of a model
            - Stage models between different environments (i.e. test and production)
        - Model Deployment
            - Model Serving: host models on a local machine or cloud provider


Ngrok
    - Very little work to expose a server running locally to the internet.

